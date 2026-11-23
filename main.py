#!/usr/bin/env python3
"""Write one line, at most 160 characters: a software patch note
for a bug in human biology.

The note is a fixed text: hiccups entered an infinite loop with no
user input, no error message, and no way to stop them. It reads like
a real release note -- a version number, a terse engineering
register, a fix stated as if it shipped -- and names a specific,
recognisable bug of the body. The program checks the text fits the
competition's 1-160 character window, then writes it to
/output/entry.txt as UTF-8.
"""

import os

NOTE = (
    "v1.9.3: fixed a bug where hiccups entered an infinite loop with "
    "no user input, no error message, and no way to stop them."
)


def main() -> None:
    if not 1 <= len(NOTE) <= 160 or not NOTE.strip():
        raise ValueError("note must be 1-160 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
