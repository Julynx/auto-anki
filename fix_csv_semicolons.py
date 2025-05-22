"""
Script to recursively fix semicolon usage in CSV files.
"""

import os
import sys

def fix_line(line):
    """Replace all semicolons after the first one in a line with commas."""
    first, *rest = line.rstrip('\n').split(';')
    if not rest:
        return line
    # Only the first semicolon is kept, others become commas
    return first + ';' + ','.join(rest) + '\n'

def fix_csv_file(filepath):
    """Process a CSV file, fixing semicolons as specified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    fixed_lines = [fix_line(line) for line in lines]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)

def fix_csvs_recursively(root_folder):
    """Recursively find and fix all .csv files in the given folder and subfolders."""
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith('.csv'):
                filepath = os.path.join(dirpath, filename)
                print(f"Fixing: {filepath}")
                fix_csv_file(filepath)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python fix_csv_semicolons.py [target_folder]")
        sys.exit(1)
    target_folder = sys.argv[1] if len(sys.argv) == 2 else os.getcwd()
    if not os.path.isdir(target_folder):
        print(f"Error: {target_folder} is not a valid directory.")
        sys.exit(1)
    fix_csvs_recursively(target_folder)
    print("All CSV files processed.")
