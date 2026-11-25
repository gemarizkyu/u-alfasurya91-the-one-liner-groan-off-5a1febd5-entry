"""Groan-Off entry: emit one dad joke, exactly once, every time.

The program has a single job. It takes a fixed one-line joke and writes
it to ``entry.txt`` inside the output directory. Nothing here varies
between runs: there is no random choice, no network fetch, no clock
reading and no model call, so the bytes on disk are identical each time.
"""

import os
import sys
from pathlib import Path

# The entry itself. One line, one groan, no trailing spaces.
JOKE = "I asked Dad why he brings a ladder to dinner — he said someone has to raise the steaks."

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 140


def resolve_output_dir() -> Path:
    """Pick where entry.txt goes.

    ``MAKEFUN_OUTPUT_DIR`` wins when it is set and non-empty; otherwise
    fall back to ``/output``. The directory is created on demand.
    """
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    target = Path(raw) if raw else Path(DEFAULT_OUTPUT_DIR)
    target.mkdir(parents=True, exist_ok=True)
    return target


def check_joke(text: str) -> None:
    """Refuse to write anything that is not a single short line."""
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError(
            f"joke must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if text != text.strip():
        raise ValueError("joke must not have leading/trailing whitespace")


def write_entry() -> Path:
    """Validate the joke, then write it plus a trailing newline."""
    check_joke(JOKE)
    destination = resolve_output_dir() / OUTPUT_FILENAME
    destination.write_text(JOKE + "\n", encoding="utf-8")
    return destination


def main() -> int:
    try:
        path = write_entry()
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(JOKE)}-character joke to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

