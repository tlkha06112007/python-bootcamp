"""Unit tests for the Week 2 CSV and JSON helpers."""

import json
from datetime import date
from pathlib import Path

import pytest

from members.NhatQuang2007_Data.w2.io_utils import load_tasks, save_json
from members.NhatQuang2007_Data.w2.models import Task

SAMPLES = Path(__file__).resolve().parents[3] / "samples"


def test_load_sample_tasks() -> None:
    tasks = load_tasks(SAMPLES / "tasks.csv")

    assert [task.title for task in tasks] == ["DS exam", "Assignment"]
    assert tasks[0] == Task("DS exam", 5, 6.0, date(2026, 10, 30))


def test_bad_sample_reports_csv_line_number() -> None:
    with pytest.raises(ValueError, match=r"line 3"):
        load_tasks(SAMPLES / "tasks_bad.csv")


def test_invalid_importance_is_rejected(tmp_path: Path) -> None:
    source = tmp_path / "invalid_importance.csv"
    source.write_text(
        "title,importance,effort_h,deadline\nBad,7,1,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match=r"line 2"):
        load_tasks(source)


def test_invalid_date_is_rejected(tmp_path: Path) -> None:
    source = tmp_path / "invalid_date.csv"
    source.write_text(
        "title,importance,effort_h,deadline\nBad,3,1,30-10-2026\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match=r"line 2"):
        load_tasks(source)


def test_missing_column_is_rejected(tmp_path: Path) -> None:
    source = tmp_path / "missing_column.csv"
    source.write_text(
        "title,importance,deadline\nBad,3,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match=r"line 1.*effort_h"):
        load_tasks(source)


def test_save_json_uses_iso_deadline(tmp_path: Path) -> None:
    destination = tmp_path / "tasks.json"
    tasks = [Task("DS exam", 5, 6.0, date(2026, 10, 30))]

    save_json(tasks, destination)
    saved = json.loads(destination.read_text(encoding="utf-8"))

    assert saved[0]["deadline"] == "2026-10-30"
    assert saved[0]["title"] == "DS exam"
