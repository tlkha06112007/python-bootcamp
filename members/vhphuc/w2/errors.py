class InfeasiblePlan(Exception):
    """Exception raised when the total effort required exceeds the available time."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        super().__init__()
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        return f"need {self.needed_h} h but only {self.available_h} h available"


def check_feasible(tasks: list, available_h: float) -> None:
    """Calculate the total effort required for all tasks.

    Raises InfeasiblePlan if total effort exceeds available_h.
    """
    total_needed = sum(task.effort_h for task in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)