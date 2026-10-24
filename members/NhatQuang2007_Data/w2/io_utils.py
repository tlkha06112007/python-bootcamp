"""CSV loading and JSON saving helpers for Week 2."""
import csv
import json
from collections.abc import Iterable
from dataclasses import asdict
from datetime import date
from pathlib import Path

from members.vthung2536.w2.models import Task

_REQUIRED_COLUMNS = ("title", "importance", "effort_h", "deadline")


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file, reporting malformed data with its line number."""
    tasks: list[Task] = []
    with open(path, "r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError("line 1: CSV file is missing a header row")
        missing_columns = [
            column for column in _REQUIRED_COLUMNS if column not in reader.fieldnames
        ]
        if missing_columns:
            names = ", ".join(missing_columns)
            raise ValueError(f"line 1: missing required column(s): {names}")
        for line_number, row in enumerate(reader, start=2):
            is_blank_row = not row or all(
                value is None or not str(value).strip() for value in row.values()
            )
            if is_blank_row:
                continue
            try:
                if None in row:
                    raise ValueError("row contains more values than the header")
                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )
            except (AttributeError, KeyError, TypeError, ValueError) as error:
                raise ValueError(f"line {line_number}: {error}") from error
            tasks.append(task)
    return tasks


def save_json(tasks: Iterable[Task], path: str | Path) -> None:
    """Serialize tasks to a UTF-8 JSON file with ISO-formatted deadlines."""
    data = []
    for task in tasks:
        item = asdict(task)
        if isinstance(item.get("deadline"), date):
            item["deadline"] = item["deadline"].isoformat()
        data.append(item)
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
        json_file.write("\n")
