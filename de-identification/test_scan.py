#!/usr/bin/env python3
"""Failing-first tests for the de-identification scanner.

Zero dependencies: stdlib unittest only. Run with:

    python3 de-identification/test_scan.py

Every test builds its own tmp git repo and fixture files, so nothing here
depends on the content of the real repository. Engine behavior (denylist
word boundaries, regex patterns, allowlist span suppression, fail-closed on
binary, exit codes) is exercised against hermetic policy files supplied via
the DEID_POLICY_DIR override. A second block proves the real seeded policy
files actually catch one representative value per category.
"""

import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCAN = os.path.join(HERE, "scan.py")


def _git(root, *args):
    subprocess.run(
        ["git", "-C", root, *args],
        check=True,
        capture_output=True,
        text=True,
    )


def _init_repo(root):
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "t@example.com")
    _git(root, "config", "user.name", "Test")


def _write(root, relpath, content, binary=False):
    full = os.path.join(root, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    mode = "wb" if binary else "w"
    with open(full, mode) as fh:
        fh.write(content)
    return full


def _run_scan(root, policy_dir=None):
    env = dict(os.environ)
    if policy_dir is not None:
        env["DEID_POLICY_DIR"] = policy_dir
    proc = subprocess.run(
        [sys.executable, SCAN, root],
        capture_output=True,
        text=True,
        env=env,
    )
    return proc.returncode, proc.stdout + proc.stderr


class HermeticEngineTests(unittest.TestCase):
    """Engine behavior against policy files we control entirely."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = os.path.join(self.tmp.name, "repo")
        self.policy = os.path.join(self.tmp.name, "policy")
        os.makedirs(self.root)
        os.makedirs(self.policy)
        _init_repo(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def _policy(self, denylist="", patterns="", allowlist=""):
        with open(os.path.join(self.policy, "denylist.txt"), "w") as fh:
            fh.write(denylist)
        with open(os.path.join(self.policy, "patterns.txt"), "w") as fh:
            fh.write(patterns)
        with open(os.path.join(self.policy, "allowlist.txt"), "w") as fh:
            fh.write(allowlist)

    def _track(self, relpath, content, binary=False):
        _write(self.root, relpath, content, binary=binary)
        _git(self.root, "add", "-A")

    def test_clean_repo_exits_zero(self):
        self._policy(denylist="SecretCorp\n")
        self._track("readme.md", "This is a public file about the operator.\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 0, out)
        self.assertIn("clean", out)

    def test_denylist_literal_trips(self):
        self._policy(denylist="SecretCorp\n")
        self._track("doc.md", "We worked with SecretCorp last year.\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)
        self.assertIn("doc.md", out)
        self.assertIn("SecretCorp", out)

    def test_denylist_word_boundary_no_substring_match(self):
        # "arvis" inside "jarvis" style: term must not match inside a word.
        self._policy(denylist="cat\n")
        self._track("doc.md", "The concatenation was educational.\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 0, out)

    def test_denylist_case_insensitive(self):
        self._policy(denylist="jarvis\n")
        self._track("doc.md", "ran it on JARVIS overnight\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)

    def test_path_prefix_term_with_trailing_slash(self):
        self._policy(denylist="fleet/\n")
        self._track("doc.md", "see fleet/ for details\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)

    def test_pattern_regex_trips(self):
        self._policy(patterns=r"fleet#\d+" + "\n")
        self._track("doc.md", "tracked as fleet#4213 yesterday\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)
        self.assertIn("fleet#4213", out)

    def test_pattern_comments_and_blanks_ignored(self):
        self._policy(patterns="# a comment\n\n" + r"redis(s)?://\S+" + "\n")
        self._track("doc.md", "url redis://cache.internal:6379/0 here\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)
        self.assertIn("redis://", out)

    def test_allowlist_suppresses_when_match_inside_allowed_substring(self):
        # "sources/" would trip, but the public URL is allowlisted.
        self._policy(
            denylist="sources/\n",
            allowlist="https://example.com/sources/data.json\n",
        )
        self._track("credits.md", "See https://example.com/sources/data.json\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 0, out)

    def test_allowlist_does_not_suppress_match_outside_allowed_span(self):
        # Same term appears both inside an allowed URL and standalone.
        self._policy(
            denylist="sources/\n",
            allowlist="https://example.com/sources/data.json\n",
        )
        self._track(
            "credits.md",
            "ok https://example.com/sources/data.json but also raw sources/ leak\n",
        )
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)

    def test_binary_file_is_hit_fail_closed(self):
        self._policy(denylist="SecretCorp\n")
        self._track("blob.bin", b"\x00\x01\x02binarydata\x00", binary=True)
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)
        self.assertIn("blob.bin", out)

    def test_undecodable_file_is_hit_fail_closed(self):
        self._policy(denylist="SecretCorp\n")
        # Invalid UTF-8 byte sequence, no NUL.
        self._track("bad.txt", b"good text \xff\xfe more\n", binary=True)
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)
        self.assertIn("bad.txt", out)

    def test_reports_path_line_category_format(self):
        self._policy(denylist="SecretCorp\n")
        self._track("a.md", "line one\nnow SecretCorp appears\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 1, out)
        # Expect path:line: ... with line number 2.
        self.assertRegex(out, r"a\.md:2:")

    def test_self_policy_files_are_skipped(self):
        # Files at de-identification/{denylist,patterns,allowlist}.txt and
        # test_scan.py are the gate's own machinery and must be skipped even
        # though they legitimately contain sensitive literals.
        self._policy(denylist="SecretCorp\n")
        self._track("de-identification/denylist.txt", "SecretCorp\n")
        self._track("de-identification/test_scan.py", "x = 'SecretCorp'\n")
        code, out = _run_scan(self.root, self.policy)
        self.assertEqual(code, 0, out)


class RealSeededPolicyTests(unittest.TestCase):
    """One representative value per required category, using the SHIPPED
    denylist.txt / patterns.txt (default policy dir). Fixtures live in a tmp
    repo, so this depends on the policy seeds, never on repo content."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = os.path.join(self.tmp.name, "repo")
        os.makedirs(self.root)
        _init_repo(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def _assert_trips(self, content):
        _write(self.root, "fixture.md", content)
        _git(self.root, "add", "-A")
        code, out = _run_scan(self.root)  # default (real) policy dir
        self.assertEqual(code, 1, "expected hit for %r\n%s" % (content, out))

    def test_client_name(self):
        self._assert_trips("engagement with Cardinal Health for Q3\n")

    def test_person(self):
        self._assert_trips("owner is Travis Sparks per the notes\n")

    def test_person_email(self):
        self._assert_trips("contact sparkst@gmail.com for access\n")

    def test_hostname(self):
        self._assert_trips("deployed on jarvis last night\n")

    def test_private_repo(self):
        self._assert_trips("cloned from sparkst/fleet earlier\n")

    def test_incident_id(self):
        self._assert_trips("fixed in fleet#399 finally\n")

    def test_contract_number(self):
        self._assert_trips("under SOW-1207 the scope covers\n")

    def test_secret_token(self):
        self._assert_trips("token ghp_abcdefghijklmnopqrstuvwxyz012345\n")

    def test_redis_url(self):
        self._assert_trips("REDIS_URL=redis://default:pw@cache:6379/0\n")

    def test_public_repo_reference_is_clean(self):
        # The public skills repo must not trip the gate.
        _write(self.root, "credits.md",
               "Adapted from sparkst/sparkry-claude-skills (MIT).\n")
        _git(self.root, "add", "-A")
        code, out = _run_scan(self.root)
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
