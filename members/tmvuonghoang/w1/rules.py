"""W1-3: Check whether a student can register for a thesis."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True with at least 120 credits and a GPA of at least 2.0."""
    return credits >= 120 and gpa >= 2.0
