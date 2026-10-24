def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day. Courses in each day are sorted."""
    result: dict[str, list[str]] = {}
    for course, day in entries:
        result.setdefault(day, []).append(course)
    for courses in result.values():
        courses.sort()
    return result