from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).parent

# Ignore these markdown files
IGNORE = {
    "README.md",
}

md_files = [
    f for f in PROJECT_ROOT.glob("*.md")
    if f.name not in IGNORE
]

if not md_files:
    print("No Mermaid markdown files found.")
    sys.exit(0)

output_dir = PROJECT_ROOT / "images"
output_dir.mkdir(exist_ok=True)

print(f"Found {len(md_files)} Mermaid files\n")

for md in md_files:

    output = output_dir / f"{md.stem}.svg"

    print(f"Generating {output.name}")

    subprocess.run(
    [
        "mmdc",
        "-i",
        str(md),
        "-o",
        str(output),
        "-b",
        "transparent",
        "-c",
        "theme.json",
    ],
    check=True,
)

print("\nDone!")