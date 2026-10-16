def parse_csv(path) -> list[Task]:
    tasks = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                tasks.append(
                    Task(
                        title=row["title"].strip(),
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"]),
                    )
                )
            except (KeyError, ValueError, TypeError, AttributeError) as e:
                raise ValueError(f"Dòng {reader.line_num}: {e}") from e
    return tasks