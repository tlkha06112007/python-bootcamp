from datetime import date
from pathlib import Path

import pytest

from shared.study_planner.__main__ import main, parse_args

BOOTCAMP = Path(__file__).resolve().parents[2]


def test_parse_args_all():
    args = parse_args(["samples/tasks.csv", "--hours", "2.5", "--today", "2026-10-26"])
    assert args.csv_path == "samples/tasks.csv"
    assert args.hours == 2.5
    assert args.today == date(2026, 10, 26)


def test_parse_args_default_today():
    args = parse_args(["samples/tasks.csv", "--hours", "3"])
    assert args.csv_path == "samples/tasks.csv"
    assert args.hours == 3.0
    assert args.today == date.today()


def test_parse_args_missing_hours():
    with pytest.raises(SystemExit):
        parse_args(["samples/tasks.csv"])


def test_main_with_sample_csv(capsys):
    csv_file = str(BOOTCAMP / "samples" / "tasks.csv")
    main([csv_file, "--hours", "2", "--today", "2026-10-26"])
    captured = capsys.readouterr()
    expected = (
        "Tonight (2.0 h):\n"
        "1. Assignment ...... 1.5 h\n"
        "2. DS exam ......... 0.5 h\n"
    )
    assert captured.out == expected

