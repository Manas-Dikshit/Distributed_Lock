#!/usr/bin/env python3

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


IGNORE_FILES = {"README.md"}


def find_mmdc():
    """
    Locate Mermaid CLI executable.
    """

    candidates = [
        "mmdc",
        "mmdc.cmd",
        "mmdc.exe",
    ]

    for cmd in candidates:
        path = shutil.which(cmd)
        if path:
            return path

    return None


def find_mermaid_files(root: Path, only_mermaid=True):
    """
    Find markdown files containing Mermaid diagrams.
    """

    files = []

    for md in root.glob("*.md"):

        if md.name in IGNORE_FILES:
            continue

        if only_mermaid:
            text = md.read_text(encoding="utf-8")

            if "```mermaid" not in text:
                continue

        files.append(md)

    return files


def generate_diagram(mmdc, md_file, output_file, theme):

    cmd = [
        mmdc,
        "-i",
        str(md_file),
        "-o",
        str(output_file),
        "-b",
        "transparent",
    ]

    if theme.exists():
        cmd.extend(["-c", str(theme)])

    subprocess.run(cmd, check=True)


def main():

    parser = argparse.ArgumentParser(
        description="Generate SVG images from Mermaid markdown files."
    )

    parser.add_argument(
        "--output",
        default="images",
        help="Output folder (default: images)",
    )

    parser.add_argument(
        "--theme",
        default="theme.json",
        help="Theme JSON file (default: theme.json)",
    )

    parser.add_argument(
        "--png",
        action="store_true",
        help="Generate PNG instead of SVG",
    )

    args = parser.parse_args()

    project_root = Path(__file__).parent

    output_dir = project_root / args.output
    output_dir.mkdir(exist_ok=True)

    theme = project_root / args.theme

    mmdc = find_mmdc()

    if mmdc is None:

        print("\nERROR: Mermaid CLI (mmdc) was not found.\n")

        print("Install Node.js:")
        print("https://nodejs.org\n")

        print("Then install Mermaid CLI:\n")

        print("npm install -g @mermaid-js/mermaid-cli\n")

        sys.exit(1)

    print(f"Using Mermaid CLI: {mmdc}\n")

    markdown_files = find_mermaid_files(project_root)

    if not markdown_files:
        print("No Mermaid markdown files found.")
        return

    print(f"Found {len(markdown_files)} Mermaid files.\n")

    extension = "png" if args.png else "svg"

    success = 0
    failed = 0

    for md in markdown_files:

        output = output_dir / f"{md.stem}.{extension}"

        print(f"Generating {output.name}")

        try:

            generate_diagram(
                mmdc,
                md,
                output,
                theme,
            )

            print("   ✓ Success\n")
            success += 1

        except subprocess.CalledProcessError as e:

            print(f"   ✗ Failed ({e})\n")
            failed += 1

    print("=" * 50)
    print(f"Generated : {success}")
    print(f"Failed    : {failed}")
    print(f"Output    : {output_dir}")
    print("=" * 50)


if __name__ == "__main__":
    main()