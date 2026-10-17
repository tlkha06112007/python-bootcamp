"""Data model used by the Week 2 task planner."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with an importance score, estimated effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("title must be a non-empty string")
        if isinstance(self.importance, bool) or not isinstance(self.importance, int):
            raise ValueError("importance must be an integer from 1 to 5")
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")
        valid_effort = isinstance(self.effort_h, (int, float)) and not isinstance(
            self.effort_h, bool
        )
        if not valid_effort:
            raise ValueError("effort_h must be a number")
        if self.effort_h < 0:
            raise ValueError("effort_h must be non-negative")
        if not isinstance(self.deadline, date):
            raise ValueError("deadline must be a datetime.date")

    def days_left(self, today: date) -> int:
        """Return days until the deadline, never returning a negative value."""
        if not isinstance(today, date):
            raise TypeError("today must be a datetime.date")
        return max((self.deadline - today).days, 0)
