#!/usr/bin/env python3
import os

def tree(dir_path, prefix=""):
    """Recursively prints a directory-only tree starting at dir_path."""
    # list and sort entries, then keep only directories (skip hidden)
    entries = sorted(e for e in os.listdir(dir_path)
                     if not e.startswith('.') and
                     os.path.isdir(os.path.join(dir_path, e)))
    pointers = ['├── '] * (len(entries) - 1) + ['└── ']

    for pointer, entry in zip(pointers, entries):
        path = os.path.join(dir_path, entry)
        print(prefix + pointer + entry + os.sep)
        # recurse into subdirectory
        extension = '│   ' if pointer == '├── ' else '    '
        tree(path, prefix=prefix + extension)

def main():
    path = input("Enter the path to scan: ").strip()
    if not path:
        print("No path provided. Exiting.")
        return

    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return

    root = os.path.abspath(path)
    basename = os.path.basename(root)
    print(basename + os.sep)
    tree(root)

if __name__ == "__main__":
    main()
