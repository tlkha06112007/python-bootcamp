"""Command-line tool: plan tonight's study session from a tasks CSV file."""

import argparse
import sys
from datetime import date, datetime

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the command-line tool."""
    parser = argparse.ArgumentParser(
        description="Plan tonight's study session from a tasks CSV file."
    )
    parser.add_argument("csv_file", help="path to the tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="hours available tonight"
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="date as YYYY-MM-DD (default: today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the tool and return the process exit code."""
    args = build_parser().parse_args(argv)
    today = args.today or datetime.now().astimezone().date()

    try:
        tasks = parse_csv(args.csv_file)
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_file}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: invalid CSV: {e}", file=sys.stderr)
        return 1
    
    ranked = prioritise(tasks, today)
    plan = allocate(ranked, args.hours)
    print(render(plan))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())