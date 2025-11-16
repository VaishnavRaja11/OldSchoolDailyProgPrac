#!/usr/bin/env python3
"""
Create a new practice day folder:

  days/dayNN/
    cpp/main.cpp
    python/main.py
    README.md
    NOTES.md

Usage:
  python scripts/new_day.py          # auto next day (day01, day02, ...)
  python scripts/new_day.py --day 5  # explicitly create day05
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Repo root = parent of this script's directory
ROOT = Path(__file__).resolve().parents[1]
DAYS_ROOT = ROOT / "days"


CPP_TEMPLATE = r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: implement today's solution
    // Use stdin/stdout so you can paste sample inputs like on LeetCode.

    return 0;
}
"""

PY_TEMPLATE = r"""def solve() -> None:
    # TODO: implement today's solution
    # Use input() / print() so you can paste sample inputs like on LeetCode.
    pass


if __name__ == "__main__":
    solve()
"""

README_TEMPLATE = """# Day {day_num:02d}

**Patterns**: <fill before coding>  
**Why this pattern fits (1 line)**: <reason>

## Problems
- [ ] <Problem 1 title> – <link>
- [ ] <Problem 2 title> – <link>

## Checklist
- [ ] Read problem
- [ ] Plan edge cases
- [ ] Implement
- [ ] Test & refactor
- [ ] Write NOTES.md
- [ ] Commit & push
"""

NOTES_TEMPLATE = """# Notes for Day {day_num:02d}

- What worked:
- What failed:
- What I want to remember for next time:
"""


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def next_day_number() -> int:
    """
    Scan days/ for existing dayNN folders and return the next number.
    """
    if not DAYS_ROOT.exists():
        return 1

    nums = []
    for child in DAYS_ROOT.iterdir():
        if child.is_dir():
            m = re.fullmatch(r"day(\d{2})", child.name)
            if m:
                nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def create_day(day_num: int) -> Path:
    day_name = f"day{day_num:02d}"
    day_dir = DAYS_ROOT / day_name

    if day_dir.exists():
        print(f"[ERROR] {day_dir} already exists", file=sys.stderr)
        sys.exit(1)

    cpp_dir = day_dir / "cpp"
    py_dir = day_dir / "python"

    ensure_dir(cpp_dir)
    ensure_dir(py_dir)

    # Write minimal cpp main
    (cpp_dir / "main.cpp").write_text(CPP_TEMPLATE, encoding="utf-8")

    # Write minimal python main
    (py_dir / "main.py").write_text(PY_TEMPLATE, encoding="utf-8")

    # README + NOTES
    (day_dir / "README.md").write_text(
        README_TEMPLATE.format(day_num=day_num),
        encoding="utf-8",
    )
    (day_dir / "NOTES.md").write_text(
        NOTES_TEMPLATE.format(day_num=day_num),
        encoding="utf-8",
    )

    print(f"[OK] Created {day_dir}")
    return day_dir


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a new dayNN folder with C++/Python stubs and notes."
    )
    parser.add_argument(
        "--day",
        type=int,
        help="day number to create (1..n). If omitted, the next available day is used.",
    )
    args = parser.parse_args()

    ensure_dir(DAYS_ROOT)

    if args.day is not None:
        day_num = args.day
    else:
        day_num = next_day_number()

    if day_num < 1:
        print("[ERROR] day must be >= 1", file=sys.stderr)
        sys.exit(1)

    create_day(day_num)


if __name__ == "__main__":
    main()
