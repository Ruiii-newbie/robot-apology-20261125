#!/usr/bin/env python3
"""The Robot Apology - make.fun entry.

Writes a two-line robot confession to /output/entry.txt:
  line 1 - one sentence apologizing for one specific mistake
  line 2 - one sentence naming the lesson and the changed behaviour

Deterministic: no randomness, no network, no input files.
"""

import os

ENTRY = (
    "I'm sorry I tossed your red sock in with the white wash "
    "and turned your favourite shirt pink.\n"
    "I learned that one careless load can undo a whole week's clean "
    "laundry, so now I sort by colour twice before I start the machine.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only whitespace"
    lines = [line for line in text.strip().split("\n")]
    assert len(lines) == 2, "entry must be exactly two lines"
    for line in lines:
        assert line.rstrip().endswith("."), "each line must be one sentence"

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "rb") as handle:
        assert handle.read() == encoded, "written bytes differ from entry"
    print("wrote %s (%d chars, %d bytes)" % (OUTPUT_PATH, len(text), len(encoded)))
    print(text, end="")


if __name__ == "__main__":
    main()
