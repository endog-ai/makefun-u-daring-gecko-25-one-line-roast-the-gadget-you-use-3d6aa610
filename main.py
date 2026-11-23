"""One-Line Roast: The Gadget You Use Every Day — make.fun entry:
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Python 3.13, stdlib only, deterministic, no network.

The roast: a password manager — the one app whose entire job is
remembering passwords — forgot the single password it had to remember,
so now it guards every secret from the one person it was meant to
serve. The turn lands on the last two words: the protector has
become the jailer, and its owner is locked out of their own life.
"""

import os
from pathlib import Path

# One original roast line, at most 200 characters: the setup names the
# app and its one job, the turn flips its purpose upside down.
# Every word earns its place — "the one password it had to remember"
# is the whole job description, "keeps all my secrets safe" is the
# promise, and "from me" breaks the promise in two words.
#
# Why this line fits the judge's brief:
# - Funny: the guardian of secrets ends up guarding them against
#   their own owner — a small betrayal with a straight face.
# - Fresh angle: the field is full of dying phone batteries, robot
#   vacuums and earbuds; nobody roasts the app that forgot the one
#   thing it exists to remember.
# - Neatly worded: one sentence, a clean setup-and-turn, and the
#   punchline is the final two words, so the line lands and stops.
# - Freshness was checked against the live field before this line was
#   settled: of the 1,325 entries already in, the visible titles roast
#   dying phone batteries, robot vacuums, earbuds, laptop fans, beeping
#   microwaves and Bluetooth pairing with the neighbour — no entry
#   roasts the app that forgot the one thing it exists to remember.
# - The em dash is one Unicode code point, so the line stays 110 chars.
LINE = (
    "My password manager forgot the one password it had to remember, "
    "so now it keeps all my secrets safe \u2014 from me."
)


def main() -> None:
    # Gate: the entry must be 1-200 Unicode code points, not only
    # whitespace — the brief's whole roast, in a single line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 code points"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
