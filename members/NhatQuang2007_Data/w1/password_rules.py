def check_password(pw: str) -> list[str]:
    """Return the list of rules the password breaks (empty if none)."""
    problems = []

    if len(pw) < 8:
        problems.append("need at least 8 characters")

    if not any(char.isdigit() for char in pw):
        problems.append("need a digit")

    if not any(char.isupper() for char in pw):
        problems.append("need an uppercase letter")

    if not any(char.islower() for char in pw):
        problems.append("need a lowercase letter")

    return problems


def is_strong(pw: str) -> bool:
    """Return True if the password breaks no rule."""
    return len(check_password(pw)) == 0
