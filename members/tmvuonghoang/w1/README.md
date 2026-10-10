# W1-3

File: `rules.py`.

`can_register_thesis(credits, gpa)` returns a boolean. Both requirements
must hold: at least 120 credits and GPA at least 2.0. Equality is allowed.

`missing(credits, gpa)` returns a new list of human-readable reasons:

- For insufficient credits, it reports the difference from 120,
  e.g. `need 2 more credits`.
- For insufficient GPA, it reports `need GPA of at least 2.0`.
- If both requirements are satisfied, it returns `[]`.

The credit reason is listed before the GPA reason when both are missing.
Inputs are assumed to be valid credit counts and GPA values as in the task;
the assignment does not specify extra input validation.

Run from the repository root:

```sh
python -m pytest -q members/tmvuonghoang/w1
python -m ruff check members/tmvuonghoang
```

These are local tests, not the instructor's missing test suite. AI assistance
is disclosed in `docs/ai-use-log.md`.
