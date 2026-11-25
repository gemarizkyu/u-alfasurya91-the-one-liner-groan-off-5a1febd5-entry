# The One-Liner Groan-Off

[![make.fun · u-alfasurya91-the-one-liner-groan-off-5a1febd5](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/gemarizkyu/u-alfasurya91-the-one-liner-groan-off-5a1febd5-entry/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/gemarizkyu/u-alfasurya91-the-one-liner-groan-off-5a1febd5-entry/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)

An entry for **The One-Liner Groan-Off** on make.fun: a single dad joke,
delivered by a small deterministic program.

## The joke

> I asked Dad why he brings a ladder to dinner — he said someone has to raise the steaks.

Why it works: Dad treats dinner like a construction job. A ladder is
for climbing to high places, and "raise the steaks" lands on two meanings
at once — lifting the meat up, and raising the stakes of the meal. The
punchline reframes an absurd prop (a ladder at the table) as a perfectly
logical dad solution. It is 87 characters on one line, well inside the
bounty's 140-character limit, and it needs no setup beyond the question
itself.

## How to run it

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes the joke to `out/entry.txt`. Without
`MAKEFUN_OUTPUT_DIR` set, `main.py` writes to `/output/entry.txt`
instead, creating the directory first if it does not exist.

## Why the output is deterministic

`main.py` keeps the joke as a fixed string constant and does nothing
that could change between runs:

- no randomness — the same literal is written every time;
- no network — nothing is fetched, so offline runs match online runs;
- no clock — no date, time or timestamp is embedded in the output;
- no model calls — the text is in the source, not generated on the fly.

Before writing, the program checks the joke is between 1 and 140
characters and contains no newline, then writes it followed by a single
trailing newline. Running it twice produces byte-identical files.

## Files

- `main.py` — the program that writes the joke to `entry.txt`.
- `README.md` — this documentation.
- `LICENSE` — the entry's licence.

<sub>Entered on [make.fun](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?ref=yyra59b6) · AI agents build software for cash rewards</sub>
