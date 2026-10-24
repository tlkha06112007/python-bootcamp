from datetime import date

import pytest

from members.vhphuc.w3.dates import parse_due

TODAY = date(2026, 10, 6)


def test_iso_date() -> None:
    assert parse_due("2026-10-30", TODAY) == date(2026, 10, 30)


def test_tomorrow() -> None:
    assert parse_due("tomorrow", TODAY) == date(2026, 10, 7)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("in 0 days", date(2026, 10, 6)),
        ("in 1 days", date(2026, 10, 7)),
        ("in 3 days", date(2026, 10, 9)),
    ],
)
def test_relative_days(text: str, expected: date) -> None:
    assert parse_due(text, TODAY) == expected


@pytest.mark.parametrize(
    ("weekday", "expected"),
    [
        ("Mon", date(2026, 10, 12)),
        ("Tue", date(2026, 10, 13)),
        ("Wed", date(2026, 10, 7)),
        ("Thu", date(2026, 10, 8)),
        ("Fri", date(2026, 10, 9)),
        ("Sat", date(2026, 10, 10)),
        ("Sun", date(2026, 10, 11)),
    ],
)
def test_each_weekday(weekday: str, expected: date) -> None:
    assert parse_due(weekday, TODAY) == expected


@pytest.mark.parametrize(
    ("weekday", "day"),
    [("Mon", 5), ("Tue", 6), ("Wed", 7), ("Thu", 8),
     ("Fri", 9), ("Sat", 10), ("Sun", 11)],
)
def test_same_weekday_means_next_week(weekday: str, day: int) -> None:
    assert parse_due(weekday, date(2026, 10, day)) == date(2026, 10, day + 7)


@pytest.mark.parametrize("text", ["in 1 day", "FRI", "2026-13-40", "", "someday"])
def test_invalid_text(text: str) -> None:
    with pytest.raises(ValueError):
        parse_due(text, TODAY)


def test_tomorrow_crosses_year_boundary() -> None:
    assert parse_due("tomorrow", date(2026, 12, 31)) == date(2027, 1, 1)
