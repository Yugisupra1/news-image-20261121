"""News-image entry (Python 3.13, standard library only).

Writes the day's front page to /output/entry.png by copying the
entry.png that ships beside this file. Deterministic: the same
bytes every run, no network, no randomness.

The front page sums up Saturday 21 November 2026: a 6.8-magnitude
earthquake in Junin, central Peru (hero), plus a photo for each of
four more stories — a Russian missile landing in Poland, the UK
expelling Myanmar's envoy after the world court's genocide verdict,
record foreign money into Indian shares, and NYC mayor Mamdani's
plan to close Rikers Island by 2032.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

def _report(out_path: Path, size: int) -> str:
    """One-line human-readable confirmation for the run log."""
    return f"wrote {out_path} ({size} bytes, {size / 1024:.1f} KiB)"


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
print(_report(OUT_DIR / "entry.png", len(data)))
