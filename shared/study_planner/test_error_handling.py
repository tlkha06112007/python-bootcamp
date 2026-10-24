import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
HEADER = "title,importance,effort_h,deadline\n"


def run_cli(path, hours):
    return subprocess.run(
        [sys.executable, "-X", "utf8", "-m", "shared.study_planner", str(path),
         "--hours", str(hours), "--today", "2026-10-26"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=10,
        check=False,
    )


@pytest.mark.parametrize("content, message", [
    (None, "file not found"),
    ("", "no tasks"),
    (HEADER, "no tasks"),
    (HEADER + "Assignment,4,3,2026-10-26\n", "infeasible plan"),
    (HEADER + "Assignment,4,3,2026-10-25\n", "infeasible plan"),
    (HEADER + "Assignment,4,abc,2026-10-27\n", "invalid CSV"),
], ids=["missing", "empty", "header_only", "due_today", "overdue", "bad_csv"])
def test_errors(tmp_path, content, message):
    path = tmp_path / "tasks.csv"
    if content is not None:
        path.write_text(content, encoding="utf-8")

    result = run_cli(path, 2)
    assert result.returncode == 1
    assert result.stdout == ""
    assert message in result.stderr
    assert "Traceback" not in result.stderr


def test_valid_plan(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(HEADER + "Assignment,4,2,2026-10-26\n", encoding="utf-8")

    result = run_cli(path, 2)
    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout == "Tonight (2.0 h):\n1. Assignment ...... 2.0 h\n"


def test_future_task_can_be_split(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(HEADER + "Assignment,4,3,2026-10-27\n", encoding="utf-8")

    result = run_cli(path, 2)
    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout == "Tonight (2.0 h):\n1. Assignment ...... 2.0 h\n"


@pytest.mark.parametrize("deadline", ["2026-10-25", "2026-10-26"])
@pytest.mark.parametrize("hours", [2, 3])
def test_due_task_before_future_task(tmp_path, deadline, hours):
    path = tmp_path / "tasks.csv"
    path.write_text(
        HEADER + f"Due,1,2,{deadline}\nFuture,5,3,2026-10-27\n",
        encoding="utf-8",
    )

    result = run_cli(path, hours)
    assert result.returncode == 0
    assert result.stderr == ""
    if hours == 2:
        assert result.stdout == "Tonight (2.0 h):\n1. Due ...... 2.0 h\n"
    else:
        assert result.stdout == (
            "Tonight (3.0 h):\n1. Due ......... 2.0 h\n2. Future ...... 1.0 h\n"
        )
