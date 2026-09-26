"""Print a small, reproducible prompt for a brighter workday."""

from __future__ import annotations

import argparse
import datetime as dt
import random


PROMPTS = (
    "まず一番小さい次の一歩を決めよう。",
    "5分だけ、気になっていることを片付けよう。",
    "完璧より前進。今日できる範囲で始めよう。",
    "深呼吸して、今の作業をひとつだけ進めよう。",
    "未来の自分が助かるメモを一行残そう。",
)


def prompt_for_date(day: dt.date) -> str:
    """Return the same prompt every time for a given calendar date."""
    return random.Random(day.toordinal()).choice(PROMPTS)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--date",
        type=dt.date.fromisoformat,
        help="date in YYYY-MM-DD format (defaults to today)",
    )
    args = parser.parse_args()
    day = args.date or dt.date.today()
    print(f"{day.isoformat()} — {prompt_for_date(day)}")


if __name__ == "__main__":
    main()
