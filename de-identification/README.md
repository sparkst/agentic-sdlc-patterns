# De-identification gate

This gate is what lets the repository flip from private to public with
confidence. It scans every tracked text file and fails the build the moment a
sensitive string appears, so nothing internal ships by accident.

## What it checks

The scanner flags any of these, anywhere in a tracked file:

- **Client names** the operator adds to `denylist.txt`.
- **People** (names and personal emails). Public content names roles, like
  "the operator", never a person.
- **Hostnames and infrastructure** (machine names, internal service hosts).
- **Private repos and internal paths** (owner/repo slugs, bare path prefixes).
- **Incident, work-order, and session ids** (regex shapes in `patterns.txt`).
- **Contract numbers** (best-effort regex shapes).
- **Secrets and tokens** (vendor token shapes, plus high-entropy values that
  sit next to a secret keyword on the same line).
- **Redis URLs**.

## How it works

- `scan.py` lists tracked files with `git ls-files` (a plain filesystem walk
  is the fallback outside a git work tree), skips the gate's own policy files,
  and checks every line against two engines.
- **denylist.txt** holds literal strings. Each is matched case-insensitively,
  with a word boundary on any edge that is a word character. So a bare host
  name does not match inside a larger word, while a path prefix like `srcdir/`
  still matches.
- **patterns.txt** holds one regex per line for the categories that are shapes
  rather than fixed values (ids, contract numbers, token shapes, Redis URLs).
- **allowlist.txt** holds known-public substrings. An allowlist entry
  suppresses a hit only when the matched text sits entirely inside an
  occurrence of that entry on the same line. A bare sensitive term elsewhere
  on the line still fails.

## Fail-closed rule

A tracked file that cannot be read as UTF-8 text, or that contains a NUL byte
(that is, a binary or degraded file), is reported as a HIT, never a pass. If
the scanner cannot read a file, it assumes the worst. Binary assets therefore
do not belong in this repo unless the policy is deliberately extended.

## Run it locally

```
python3 de-identification/scan.py
```

Exit code `0` prints `de-identification scan: clean (N files)`. Exit code `1`
prints one line per hit in the form:

```
path:line: <category>: <matched text>
```

where `<category>` is `denylist`, `pattern`, or an `unreadable/binary` note.

## Add or change a term

1. A fixed string (client name, person, host, repo, path): add one line to
   `de-identification/denylist.txt`, in the matching block.
2. A shape (id, contract, token, URL): add one commented Python regex line to
   `de-identification/patterns.txt`.
3. A known-public string a rule wrongly flags (for example a public source URL
   under a generic path prefix): add the full public substring to
   `de-identification/allowlist.txt`, as specifically as possible.

After any change, run `python3 de-identification/test_scan.py`. All tests must
pass before the change lands.

## CI

The GitHub Actions workflow runs `python3 de-identification/scan.py` on every
push and pull request and fails the job on a non-zero exit. No other steps.

The workflow file lives at `de-identification/deid.workflow.yml` and must be
installed to `.github/workflows/deid.yml` by a maintainer whose credential
carries the `workflow` OAuth scope:

```
mkdir -p .github/workflows
cp de-identification/deid.workflow.yml .github/workflows/deid.yml
git add .github/workflows/deid.yml && git commit -m "ci: install de-id workflow"
```
