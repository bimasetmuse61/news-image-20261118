#!/usr/bin/env python3
"""news-image-20261118: sum up the world news of Wednesday 18 November 2026.

The entry is the front-page image entry.png that sits next to this file
(it was drawn during the build session: lead story US-Iran clashes in the
Strait of Hormuz, Nvidia doubling revenue, Ukraine striking the Kerch
Bridge again, Cyclone Akvan closing in, India-Japan 2+2 talks in Tokyo,
plus Gaza, COP31, the new James Bond and a Romanian quake in the strip).

Running this program copies that image, unchanged, into the folder the
harness provides ($MAKEFUN_OUTPUT_DIR, or /output when unset). Standard
library only, no network, no randomness: every run writes identical bytes.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
