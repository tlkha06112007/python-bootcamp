import subprocess
import sys
from pathlib import Path

# File lives at <repo>/members/<folder>/w3/tests_for_<owner>_cli.py
REPO_ROOT = Path(__file__).resolve().parents[3]
CLI_OWNER = "NQThuan25127515"  # folder that contains the cli.py under test
CLI_MODULE = f"members.{CLI_OWNER}.w3.cli"
HEADER = "title,importance,effort_h,deadline\n"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the CLI as a subprocess from the repo root."""
    return subprocess.run(
        [sys.executable, "-m", CLI_MODULE, *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def write_csv(tmp_path: Path, rows: str, name: str = "tasks.csv") -> str:
    """Write a CSV file with the project's header and return its path."""
    csv_file = tmp_path / name
    csv_file.write_text(HEADER + rows, encoding="utf-8")
    return str(csv_file)


def test_sample_file_succeeds(tmp_path):
    csv_file = write_csv(tmp_path, "Assignment 1,4,2.0,2026-10-28\nLab 2,3,1.5,2026-10-27\n")
    result = run_cli(csv_file, "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 0
    assert "Assignment" in result.stdout


def test_missing_file_exits_1_without_traceback():
    result = run_cli("missing.csv", "--hours", "2")
    assert result.returncode == 1
    assert "Error: file not found" in result.stderr
    assert "Traceback" not in result.stderr


def test_bad_csv_exits_1(tmp_path):
    csv_file = tmp_path / "bad.csv"
    csv_file.write_text("invalid,csv,data,here\n1,2,3,4\n", encoding="utf-8")
    result = run_cli(str(csv_file), "--hours", "2")
    assert result.returncode == 1
    assert "Error: invalid CSV" in result.stderr


def test_header_only_csv_prints_empty_plan(tmp_path):
    csv_file = write_csv(tmp_path, "")
    result = run_cli(csv_file, "--hours", "3")
    assert result.returncode == 0
    assert "Tonight (0.0 h):" in result.stdout


def test_hours_zero_prints_empty_plan(tmp_path):
    csv_file = write_csv(tmp_path, "Assignment 1,4,2.0,2026-10-28\n")
    result = run_cli(csv_file, "--hours", "0", "--today", "2026-10-26")
    assert result.returncode == 0
    assert "Tonight (0.0 h):" in result.stdout


def test_today_option_changes_order(tmp_path):
    csv_file = write_csv(tmp_path, "Task A,5,1.0,2026-11-10\nTask B,3,1.0,2026-10-28\n")
    early = run_cli(csv_file, "--hours", "10", "--today", "2026-10-26")
    late = run_cli(csv_file, "--hours", "10", "--today", "2026-11-09")
    assert early.stdout.index("Task B") < early.stdout.index("Task A")
    assert late.stdout.index("Task A") < late.stdout.index("Task B")


def test_missing_hours_is_an_argument_error(tmp_path):
    csv_file = write_csv(tmp_path, "Assignment 1,4,2.0,2026-10-28\n")
    result = run_cli(csv_file)
    assert result.returncode == 2