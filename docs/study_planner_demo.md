# Study Planner demo

All commands are run from the repo root.

## 1. Two hours: the second task gets only part of its time

    python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26

    Tonight (2.0 h):
    1. Assignment ...... 1.5 h
    2. DS exam ......... 0.5 h

Assignment is due tomorrow, so it is planned first and gets all 1.5 h.
DS exam gets the remaining 0.5 h.

## 2. Enough hours: every task gets its full time

    python -m shared.study_planner samples/tasks.csv --hours 8 --today 2026-10-26

    Tonight (7.5 h):
    1. Assignment ...... 1.5 h
    2. DS exam ......... 6.0 h

The header shows the hours actually planned (7.5 h), not the 8 h available.

## 3. Missing file: clear error and exit code 1

    python -m shared.study_planner missing.csv --hours 2

    Error: file not found: missing.csv

The message goes to stderr and the exit code is 1.