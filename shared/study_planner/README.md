# Study Planner

Plan tonight's study session from a CSV file of tasks.

## Setup
Python 3.10+.

    python -m venv .venv
    .venv\Scripts\Activate.ps1          # macOS/Linux: source .venv/bin/activate
    pip install pytest ruff

## Run (from the repo root)

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

## Input format

    title,importance,effort_h,deadline
    DS exam,5,6,2026-10-30
    Assignment,4,1.5,2026-10-27

`importance` is 1-5, `effort_h` is hours, `deadline` is YYYY-MM-DD.

## How it works
`parse_csv` -> `prioritise` (importance / days left) -> `allocate` (greedy) -> `render`

## Errors
(update to match the merged error handling)
A missing file, an empty file or an invalid CSV prints `Error: ...` on stderr and exits with code 1.

## Tests

    python -m pytest -q
    ruff check .