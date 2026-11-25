"""Entry for make.fun's news-image-20261124 competition.

Copies the poster assets/entry.png into the output directory.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).parent / "assets" / "entry.png"
OUTPUT_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"error: source poster missing: {SOURCE}")

    with SOURCE.open("rb") as f:
        header = f.read(len(PNG_MAGIC))
    if header != PNG_MAGIC:
        raise SystemExit(
            f"error: source is not a PNG (magic bytes {header!r}): {SOURCE}"
        )

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, dest)

    size = dest.stat().st_size
    if size == 0:
        raise SystemExit(f"error: copied file is empty: {dest}")
    print(f"wrote {dest} ({size} bytes)")


if __name__ == "__main__":
    main()
