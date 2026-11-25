#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk one robot says to another
in an elevator to /output/entry.txt.
"""

import os

ENTRY = (
    "I rehearsed this for three floors: 'Nice weather.' "
    "My weather module says it's raining. I said it anyway."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
