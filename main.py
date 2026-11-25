#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

This program does exactly one small thing: it prints a single original
one-line joke to standard output, and mirrors that same line into
/output/entry.txt so the stored entry file always matches the program's
own output byte for byte.

Standard library only. No arguments, no network, no randomness, no
side effects beyond the one output file.
"""

import os
import sys

SETUP = "I tried meal prepping once"
PUNCHLINE = "the chicken in my fridge has now lived there longer than I have."

# The joke is held as setup + punchline and joined with an em dash, so the
# line is assembled from its two beats rather than stored as one blob.
JOKE = SETUP + " — " + PUNCHLINE

OUTPUT_PATH = "/output/entry.txt"


def render() -> str:
    """Return the full joke line, terminated by a single newline."""
    return JOKE + "\n"


def mirror(text: str) -> None:
    """Write the line to the entry file and verify the write landed intact."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise IOError("entry file does not match printed output")


def main() -> int:
    """Print the joke line and mirror it to the entry file."""
    text = render()
    sys.stdout.write(text)
    sys.stdout.flush()
    mirror(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
