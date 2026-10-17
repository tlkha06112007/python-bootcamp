from pathlib import Path

from members.NhatQuang2007_Data.w2.io_utils import load_tasks

SAMPLE = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> None:
    for task in load_tasks(SAMPLE):
        print(task)


if __name__ == "__main__":
    main()