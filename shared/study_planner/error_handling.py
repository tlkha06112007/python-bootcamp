"""Command-line interface for shared.study_planner with error handling."""

import argparse
import sys
from datetime import date, datetime

# Reuse InfeasiblePlan và check_feasible từ members/vhphuc/w2/errors.py
from members.vhphuc.w2.errors import InfeasiblePlan, check_feasible
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def build_parser() -> argparse.ArgumentParser:
    """Build argument parser for the study planner CLI."""
    parser = argparse.ArgumentParser(
        description="Plan tonight's study session from a tasks CSV file."
    )
    parser.add_argument("csv_file", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Hours available tonight"
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="Date as YYYY-MM-DD (default: today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the study planner pipeline and handle all error edge cases."""
    args = build_parser().parse_args(argv)
    today = args.today or datetime.now().astimezone().date()

    # -----------------------------------------------------------------------
    # 1. Xử lý lỗi File thiếu (FileNotFoundError) & File rỗng / sai định dạng CSV
    # -----------------------------------------------------------------------
    try:
        tasks = parse_csv(args.csv_file)
        if not tasks:  # Trường hợp file rỗng (chỉ có header hoặc hoàn toàn trống)
            print(
                f"Error: empty tasks file '{args.csv_file}'", file=sys.stderr
            )
            return 1
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_file}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: invalid CSV format: {e}", file=sys.stderr)
        return 1

    # -----------------------------------------------------------------------
    # 2. Xử lý lỗi Kế hoạch không khả thi (InfeasiblePlan via check_feasible)
    # -----------------------------------------------------------------------
    try:
        check_feasible(tasks, args.hours)
    except InfeasiblePlan as e:
        print(f"Error: infeasible plan - {e}", file=sys.stderr)
        return 1

    # -----------------------------------------------------------------------
    # 3. Luồng xử lý chính khi không có lỗi
    # -----------------------------------------------------------------------
    ranked = prioritise(tasks, today)
    plan = allocate(ranked, args.hours)
    print(render(plan))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())