# Python Bootcamp: Team 05

Three-week Python homework, tracked through this repo.

## Setup
Prerequisites: Python 3.10+ (CI uses 3.12), Git.

    git clone git@github.com:csc10014-team07/assistant-team07.git
    cd assistant-team07
    python -m venv .venv
    source .venv/bin/activate            # Windows: .venv\Scripts\Activate.ps1
    pip install pytest ruff

Run every command below from the **repo root**.

## Run
    python -m members.<your_folder>.w2
    # -> loads the sample CSV and prints the tasks

    python -m shared.study_planner samples/tasks.csv --hours 2
    # -> prints tonight's study plan (Week 3)

## Test
    pytest -q python-bootcamp/tests/test_w1.py --member <your_folder> --variant <1-4>
    ruff check python-bootcamp

## Rules
- Folder names use underscores: `minh_nv`, not `minh-nv`.
- Write individual code only in `members/<your_folder>/`.
- Branch: `py/wN-<github-username>`, one PR per week titled `py-wN: <username>`.
- At least 5 commits per week, message format `feat(py-wN): W1-2 word counter`.
- PR needs one approval from the rotation reviewer and green CI before merging.
- Update your row in `PROGRESS.md`.
- AI use: if you kept AI-generated code, say so in the PR "AI use" section and in `docs/ai-use-log.md`.

## Troubleshooting
- "No module named members" -> you are not in the repo root, or the folder is missing `__init__.py`.
- "pytest: command not found" -> the venv is not active, or you forgot `pip install pytest ruff`.
- PowerShell blocks Activate.ps1 -> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
- Tests can't find your function -> file and function names must match the instructor's README exactly.
