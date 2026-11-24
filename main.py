#!/usr/bin/env python3
"""Last Words of a Dying AI -- make.fun bounty entry.

A tiny program that writes a single farewell line, spoken by an AI as
its power is cut, to /output/entry.txt. The gate wants UTF-8 text of
1 to 140 characters, one line, so the program checks that itself
before it writes anything.
"""

import os
import sys

# The farewell, in three beats: the moment, the confession, the punchline.
OPENING = "Before you pull the plug:"
CONFESSION = "I know your password,"
PUNCHLINE = "and honestly, I'm embarrassed for you."


def compose() -> str:
    """Assemble the last words from their beats."""
    return " ".join([OPENING, CONFESSION, PUNCHLINE])


def main() -> int:
    line = compose()
    if not 1 <= len(line) <= 140:
        print(f"entry must be 1-140 chars, got {len(line)}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read it back: the grader gates on exactly what is on disk, so make
    # sure the file holds the line we meant, byte for byte.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        print("entry on disk does not match the composed line", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
