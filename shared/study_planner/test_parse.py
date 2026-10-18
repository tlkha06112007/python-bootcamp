import pytest

from shared.study_planner.parse import parse_csv


def test_good_file_returns_2_tasks():
    tasks = parse_csv("samples/tasks.csv")
    assert len(tasks) == 2


def test_bad_file_reports_line_3():
    with pytest.raises(ValueError, match="Dòng 3"):
        parse_csv("samples/tasks_bad.csv")


def test_header_only_returns_empty_list():
    assert parse_csv("samples/tasks_header_only.csv") == []