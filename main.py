"""The One-Liner Groan-Off — make.fun entry.

Writes a single original dad joke, one line, to entry.txt.
The program is fully deterministic: the same bytes on every run,
with no randomness, no clock, no network and no input files.
"""

import os
from pathlib import Path

# One scene, one turn: Dad brings a ladder to the dinner table, and the
# punchline is a double pun — raise the steaks / raise the stakes.
# The line is 87 characters, one sentence, and it never explains itself:
# the groan is the whole joke.
JOKE = "I asked Dad why he brings a ladder to dinner \u2014 he said someone has to raise the steaks."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text and not text.isspace(), "entry must not be only whitespace"
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
