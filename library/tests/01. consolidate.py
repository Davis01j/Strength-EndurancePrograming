#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path

def consolidate_data(src_root: Path, dst_folder: Path, move_files: bool = False):
    """
    Walk src_root for .json and .csv, and copy (or move) them all into dst_folder.
    If files share a name, we append a counter to avoid overwriting.
    """
    dst_folder.mkdir(parents=True, exist_ok=True)

    seen = {}  # track how many times we’ve seen each stem
    for path in src_root.rglob("*"):
        if path.suffix.lower() not in {".json", ".csv"}:
            continue
        stem = path.stem
        ext  = path.suffix.lower()
        count = seen.get(stem, 0)
        seen[stem] = count + 1

        if count == 0:
            new_name = f"{stem}{ext}"
        else:
            new_name = f"{stem}_{count}{ext}"

        dest = dst_folder / new_name
        if move_files:
            shutil.move(str(path), str(dest))
        else:
            shutil.copy2(str(path), str(dest))
        print(f"{'Moved' if move_files else 'Copied'} {path} → {dest}")

def main():
    p = argparse.ArgumentParser(
        description="Consolidate JSON & CSV files into one folder"
    )
    p.add_argument("src_root", type=Path, help="Root directory to search")
    p.add_argument("dst_folder", type=Path, help="Folder to collect all files")
    p.add_argument(
        "--move", action="store_true",
        help="Move files instead of copying"
    )
    args = p.parse_args()

    consolidate_data(args.src_root, args.dst_folder, move_files=args.move)

if __name__ == "__main__":
    main()
