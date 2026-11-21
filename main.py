"""News-image entry (Python 3.13, standard library only).

Writes the day's front page to /output/entry.png by copying the
entry.png that ships beside this file. Deterministic: the same
bytes every run, no network, no randomness.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")

# Sanity: the copy must be byte-identical to the shipped image.
assert (OUT_DIR / "entry.png").read_bytes() == (HERE / "entry.png").read_bytes()
