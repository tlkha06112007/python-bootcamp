# Study Planner

Plan tonight's study session from a CSV file of tasks.

## Setup

Python 3.10 or newer.

    python -m venv .venv
    .venv\Scripts\Activate.ps1          # macOS/Linux: source .venv/bin/activate
    pip install pytest ruff

## Run

From the repo root:

    python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26

Output:

    Tonight (2.0 h):
    1. Assignment ...... 1.5 h
    2. DS exam ......... 0.5 h

| Option | Meaning |
|---|---|
| `csv_path` | the tasks CSV file |
| `--hours` | hours available tonight (required) |
| `--today` | reference date, YYYY-MM-DD (default: today) |

A demo with more examples is in `docs/study_planner_demo.md`.

## Input format

    title,importance,effort_h,deadline
    DS exam,5,6,2026-10-30
    Assignment,4,1.5,2026-10-27

`importance` is 1-5, `effort_h` is the hours needed, `deadline` is YYYY-MM-DD.

## How it works

`parse_csv` -> `prioritise` (importance / days left) -> `allocate` (greedy) -> `render`

## Errors

The program prints a message starting with `Error:` on stderr and exits with code 1 when:

- the CSV file does not exist
- the file has no tasks (empty, or header only)
- the CSV is invalid (for example a bad number or date)

Examples:

    python -m shared.study_planner missing.csv --hours 2
    Error: file not found: missing.csv

    python -m shared.study_planner samples/tasks_header_only.csv --hours 2
    Error: no tasks in samples/tasks_header_only.csv

    python -m shared.study_planner samples/tasks_bad.csv --hours 2
    Error: invalid CSV: Dòng 3: invalid literal for int() with base 10: 'high'

## Tests

    python -m pytest -q shared/study_planner
    ruff check .

`test_end_to_end.py` runs the real command and compares its output with `samples/expected_plan.txt`.