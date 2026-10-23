import argparse
from collections.abc import Sequence
from datetime import date

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
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


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)

    tasks = parse_csv(args.csv_path)
    prioritised_tasks = prioritise(tasks, args.today)
    blocks = allocate(prioritised_tasks, args.hours)
    output = render(blocks)

    print(output)


if __name__ == "__main__":
    main()
