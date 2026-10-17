from datetime import date

from shared.contract import Task


def days_left(task: Task, today: date) -> int:
    return max((task.deadline - today).days, 0)


def score(task: Task, today: date) -> float:
    # max(..., 1) tránh chia cho 0 khi task đến hạn hôm nay hoặc đã quá hạn
    return task.importance / max(days_left(task, today), 1)


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    """Return tasks sorted from most to least urgent (importance / days left)."""
    return sorted(tasks, key=lambda t: (-score(t, today), t.deadline, t.title))