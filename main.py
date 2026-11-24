#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Writes one original one-line fortune for a houseplant
to /output/entry.txt.
"""

LINE = (
    "By spring you will outgrow this windowsill, and your keeper "
    "will pretend they planned it all along."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
