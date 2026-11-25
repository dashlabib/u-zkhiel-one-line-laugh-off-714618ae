#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Prints exactly one original joke line to stdout and writes the same
line to /output/entry.txt, where the make.fun program/v1 harness
reads it. Standard library only, no network, no randomness: the
line below is the whole entry, and every run produces it byte
for byte.
"""

import os

JOKE = "I tried meal prepping once \u2014 the chicken in my fridge has now lived there longer than I have."


def main() -> None:
    print(JOKE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(JOKE + "\n")
    except OSError:
        # The harness reads stdout too; a missing /output must never
        # stop the line itself from being printed.
        pass


if __name__ == "__main__":
    main()
