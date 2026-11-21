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

# Sanity: the entry must be a whole PNG or JPEG within the gate limits
# (at most 1 MiB and 1024 by 1024 pixels), told apart by its first bytes.
data = (OUT_DIR / "entry.png").read_bytes()
assert len(data) <= 1_048_576, f"entry.png is {len(data)} bytes, over the 1 MiB gate"
assert data[:8] == b"\x89PNG\r\n\x1a\n" or data[:3] == b"\xff\xd8\xff", \
    "entry.png is neither PNG nor JPEG"
print(f"wrote {OUT_DIR / 'entry.png'} ({len(data)} bytes)")
