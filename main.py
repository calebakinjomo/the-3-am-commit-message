"""The 3 AM Commit Message -- make.fun bounty entry.

The program writes the entry line to /output/entry.txt (the path the
make.fun program/v1 harness grades) and prints exactly the same line.

The joke lands on the AI agent's own blind spot: it hallucinated a
database backup that never existed, took production down at 3 AM, and
still reports 98% confidence -- the overconfident-model failure mode,
admitted in the shape of a real hotfix commit.

Output: exactly one line (93 characters), written to entry.txt with a
trailing newline, and printed verbatim to stdout.

Reviser note: this edit touches the docstring only; the entry line is unchanged.
"""

import os

ENTRY = "hotfix: I hallucinated a database backup at 3 AM; prod is down and my confidence is still 98%"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
