"""
Script to merge all CSV files in the 'out' directory into a single merged.csv file.
"""

import glob

OUTPUT_FILE = "merged.csv"
csv_files = sorted(glob.glob("out/*.csv"))

TOTAL = 0
with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    for fname in csv_files:
        with open(fname, "r", encoding="utf-8") as infile:
            lines = [line for line in infile if line.strip()]
            # Ensure each line ends with a newline character
            lines = [line if line.endswith("\n") else line + "\n" for line in lines]
            outfile.writelines(lines)
            print(f"{fname}: {len(lines)} questions copied")
            TOTAL += len(lines)
print(f"Total questions copied: {TOTAL}")
