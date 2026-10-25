import argparse
import sys
from collections.abc import Sequence
from datetime import date

from members.vhphuc.w2.errors import InfeasiblePlan, check_feasible
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Study Planner - Lập kế hoạch học tập buổi tối từ file CSV"
    )
    parser.add_argument(
        "csv_path",
        help="Đường dẫn đến file CSV chứa danh sách tasks (ví dụ: samples/tasks.csv)",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Tổng số giờ học khả dụng tối nay",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Ngày tham chiếu theo định dạng YYYY-MM-DD (mặc định: hôm nay)",
    )
    return parser.parse_args(args)


def main(argv: Sequence[str] | None = None) -> int:
    """Run the planner and return the process exit code."""
    args = parse_args(argv)

    try:
        tasks = parse_csv(args.csv_path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: invalid CSV: {e}", file=sys.stderr)
        return 1

    if not tasks:
        print(f"Error: no tasks in {args.csv_path}", file=sys.stderr)
        return 1

    due_now = [t for t in tasks if t.deadline <= args.today]
    try:
        check_feasible(due_now, args.hours)
    except InfeasiblePlan as e:
        print(f"Error: infeasible plan: {e}", file=sys.stderr)
        return 1

    future = [t for t in tasks if t.deadline > args.today]
    ordered = prioritise(due_now, args.today) + prioritise(future, args.today)
    print(render(allocate(ordered, args.hours)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
