#!/usr/bin/env python3
"""De-identification gate for a repo about to go public.

Walks the tracked text files of a git repository and fails (exit 1) when any
sensitive string appears: a client name, a person, a hostname, an internal
repo or path, an incident or work-order id, a contract number, a secret or
token, or a Redis URL. Exits 0 and prints a one-line summary when clean.

Zero dependencies: Python 3 standard library only.

Policy lives in three sibling files (denylist.txt, patterns.txt,
allowlist.txt). Override their directory for testing with DEID_POLICY_DIR.

Fail-closed rule: a tracked file that cannot be read as UTF-8 text, or that
contains a NUL byte (binary), is reported as a HIT, never silently passed.

Usage:
    python3 de-identification/scan.py [ROOT]
ROOT defaults to the current working directory.
"""

import os
import re
import subprocess
import sys

# Policy files at the repo root, relative to ROOT, that the scanner must skip:
# they are the gate's own machinery and legitimately hold sensitive literals.
SELF_SKIP = frozenset(
    os.path.normpath(p)
    for p in (
        "de-identification/denylist.txt",
        "de-identification/patterns.txt",
        "de-identification/allowlist.txt",
        "de-identification/test_scan.py",
    )
)


def policy_dir():
    return os.environ.get("DEID_POLICY_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )


def read_policy_lines(name):
    """Read a policy file, dropping blank lines and '#' comments."""
    path = os.path.join(policy_dir(), name)
    out = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for raw in fh:
                line = raw.rstrip("\n")
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                out.append(line)
    except FileNotFoundError:
        pass
    return out


def _word(ch):
    return ch.isalnum() or ch == "_"


def term_to_regex(term):
    """A denylist literal, matched case-insensitively with a word boundary
    only on the side whose edge character is itself a word character. This
    keeps a bare host name from matching inside a larger word while still
    matching a path prefix like 'srcdir/' that ends in a non-word char."""
    esc = re.escape(term)
    prefix = r"(?<!\w)" if _word(term[0]) else ""
    suffix = r"(?!\w)" if _word(term[-1]) else ""
    return prefix + esc + suffix


def build_matchers():
    """Return (matchers, errors). Each matcher is (category, compiled_regex).
    Denylist terms are combined case-insensitively; patterns are compiled as
    written (case-sensitive) so secret shapes stay exact."""
    matchers = []
    errors = []

    deny = read_policy_lines("denylist.txt")
    if deny:
        combined = "|".join(term_to_regex(t) for t in deny)
        matchers.append(("denylist", re.compile(combined, re.IGNORECASE)))

    for pat in read_policy_lines("patterns.txt"):
        try:
            matchers.append(("pattern", re.compile(pat)))
        except re.error as exc:
            errors.append("bad pattern %r: %s" % (pat, exc))

    return matchers, errors


def allowed_spans(line, allow_terms):
    """Character ranges on this line that are known-public. A hit is
    suppressed only when its whole span sits inside one of these ranges."""
    spans = []
    for term in allow_terms:
        start = 0
        while True:
            idx = line.find(term, start)
            if idx < 0:
                break
            spans.append((idx, idx + len(term)))
            start = idx + 1
    return spans


def _suppressed(start, end, spans):
    return any(s <= start and end <= e for (s, e) in spans)


def tracked_files(root):
    """Tracked files via `git ls-files` when ROOT is a git work tree; else a
    filesystem walk skipping .git. Returns repo-relative POSIX-ish paths."""
    inside = subprocess.run(
        ["git", "-C", root, "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        text=True,
    )
    if inside.returncode == 0 and inside.stdout.strip() == "true":
        res = subprocess.run(
            ["git", "-C", root, "ls-files", "-z"],
            capture_output=True,
            text=True,
            check=True,
        )
        return [p for p in res.stdout.split("\0") if p]
    # Fallback: not a git repo.
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            full = os.path.join(dirpath, name)
            files.append(os.path.relpath(full, root))
    return files


def scan_file(root, rel, matchers, allow_terms):
    """Return a list of hit strings for one file. A file that is binary or
    not valid UTF-8 yields a single fail-closed hit."""
    full = os.path.join(root, rel)
    try:
        with open(full, "rb") as fh:
            data = fh.read()
    except OSError as exc:
        return ["%s:0: unreadable: %s (fail-closed)" % (rel, exc)]

    if b"\x00" in data:
        return ["%s:0: unreadable/binary: NUL byte (fail-closed)" % rel]
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return ["%s:0: unreadable/binary: not UTF-8 (fail-closed)" % rel]

    hits = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        spans = allowed_spans(line, allow_terms) if allow_terms else []
        for category, rx in matchers:
            for m in rx.finditer(line):
                if _suppressed(m.start(), m.end(), spans):
                    continue
                hits.append("%s:%d: %s: %s" % (rel, lineno, category, m.group(0)))
    return hits


def main(argv):
    root = argv[1] if len(argv) > 1 else os.getcwd()
    root = os.path.abspath(root)

    matchers, errors = build_matchers()
    for err in errors:
        print("de-identification scan: policy error: %s" % err, file=sys.stderr)
    if errors:
        return 2

    allow_terms = read_policy_lines("allowlist.txt")

    files = tracked_files(root)
    all_hits = []
    scanned = 0
    for rel in files:
        if os.path.normpath(rel) in SELF_SKIP:
            continue
        scanned += 1
        all_hits.extend(scan_file(root, rel, matchers, allow_terms))

    if all_hits:
        for hit in all_hits:
            print(hit)
        print(
            "de-identification scan: FAILED (%d hit(s) across %d files)"
            % (len(all_hits), scanned),
            file=sys.stderr,
        )
        return 1

    print("de-identification scan: clean (%d files)" % scanned)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
