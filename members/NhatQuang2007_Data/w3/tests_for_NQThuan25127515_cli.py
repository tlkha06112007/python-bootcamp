from pathlib import Path
import subprocess
import sys
import pytest

# ===========================================================================
# CẤU HÌNH ĐƯỜNG DẪN DỰ ÁN & CLI MODULE
# ===========================================================================
# File nằm tại: repo_root/members/<folder>/w3/tests_for_<owner>_cli.py
FILE_PATH = Path(__file__).resolve()
REPO_ROOT = FILE_PATH.parents[3]  # Đường dẫn tới thư mục gốc Repo
MEMBER_FOLDER = "NQThuan25127515" 
CLI_MODULE = f"members.{MEMBER_FOLDER}.w3.cli"


def run_cli(*args):
    """Hàm bổ trợ chạy CLI qua subprocess.run theo đúng yêu cầu đề bài."""
    cmd = [sys.executable, "-m", CLI_MODULE] + list(args)
    return subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


# ===========================================================================
# 1. TEST CỦA THẦY (MAIN TEST CASES)
# ===========================================================================
def test_w3_3_cli_sample_file_success(tmp_path):
    """Test của thầy 1: File CSV mẫu hợp lệ -> exit 0 và stdout chứa 'Assignment'."""
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,due,hours,priority\n"
        "Assignment 1,2026-10-28,2.0,1\n"
        "Lab 2,2026-10-27,1.5,2\n",
        encoding="utf-8",
    )

    result = run_cli(str(csv_file), "--hours", "2", "--today", "2026-10-26")

    assert result.returncode == 0
    assert "Assignment" in result.stdout


def test_w3_3_cli_missing_file_error():
    """Test của thầy 2: Truyền missing.csv -> exit 1 và có thông báo lỗi ở stderr."""
    result = run_cli("missing.csv", "--hours", "2")

    assert result.returncode == 1
    assert result.stderr != ""
    assert "Error: file not found" in result.stderr


# ===========================================================================
# 2. EDGE CASES (CÁC TRƯỜNG HỢP BIÊN THEO GỢI Ý ĐỀ BÀI)
# ===========================================================================
def test_w3_3_cli_bad_csv_value_error(tmp_path):
    """Edge Case 1: tasks_bad.csv (file CSV sai định dạng/thiếu cột) -> exit 1 & in stderr."""
    csv_file = tmp_path / "tasks_bad.csv"
    csv_file.write_text("invalid,csv,data,here\n1,2,3,4\n", encoding="utf-8")

    result = run_cli(str(csv_file), "--hours", "2")

    assert result.returncode == 1
    assert result.stderr != ""
    assert "Error: invalid CSV" in result.stderr


def test_w3_3_cli_header_only_csv(tmp_path):
    """Edge Case 2: File CSV chỉ có dòng header (không có dữ liệu task) -> exit 0."""
    csv_file = tmp_path / "empty_tasks.csv"
    csv_file.write_text("title,due,hours,priority\n", encoding="utf-8")

    result = run_cli(str(csv_file), "--hours", "3")

    assert result.returncode == 0


def test_w3_3_cli_hours_zero(tmp_path):
    """Edge Case 3: Truyền --hours 0 -> exit 0 và không báo lỗi crash."""
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,due,hours,priority\n" "Assignment 1,2026-10-28,2.0,1\n",
        encoding="utf-8",
    )

    result = run_cli(str(csv_file), "--hours", "0", "--today", "2026-10-26")

    assert result.returncode == 0


def test_w3_3_cli_today_option_changes_order(tmp_path):
    """Edge Case 4: Truyền tham số --today tùy chọn hợp lệ -> exit 0 và thực thi thành công."""
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,due,hours,priority\n"
        "Task A,tomorrow,2.0,1\n"
        "Task B,in 3 days,1.0,2\n",
        encoding="utf-8",
    )

    result = run_cli(str(csv_file), "--hours", "2", "--today", "2026-10-26")

    assert result.returncode == 0