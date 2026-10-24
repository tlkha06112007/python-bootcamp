import subprocess
import sys
from pathlib import Path

CSV_PATH = "samples/tasks.csv"
EXPECTED_PATH = "samples/expected_plan.txt"
HOURS = "2"
TODAY = "2026-10-26"  # co dinh, khong dung ngay that de test khong bi troi


def find_repo_root() -> Path:
    """Di nguoc len tu file test cho toi thu muc chua shared/study_planner."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "shared" / "study_planner").is_dir():
            return parent
    raise RuntimeError("Khong tim thay goc repo (thu muc chua shared/study_planner)")


REPO_ROOT = find_repo_root()


def run_planner(*extra_args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            sys.executable, "-m", "shared.study_planner",
            CSV_PATH, "--hours", HOURS, "--today", TODAY,
            *extra_args,
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )


def normalise(text: str) -> str:
    """Bo khac biet vo hai: CRLF/LF va khoang trang cuoi dong."""
    lines = text.replace("\r\n", "\n").split("\n")
    return "\n".join(line.rstrip() for line in lines).strip()


def test_end_to_end_exit_code_zero():
    result = run_planner()
    assert result.returncode == 0, f"stderr:\n{result.stderr}"


def test_end_to_end_matches_expected_plan():
    result = run_planner()
    expected = (REPO_ROOT / EXPECTED_PATH).read_text(encoding="utf-8")

    assert result.returncode == 0, f"stderr:\n{result.stderr}"
    assert normalise(result.stdout) == normalise(expected)


def test_end_to_end_output_is_repeatable():
    first = run_planner()
    second = run_planner()

    assert first.returncode == second.returncode == 0
    assert first.stdout == second.stdout