"""Unit tests for the Week 2 Task model."""

from datetime import date

import pytest

from members.NhatQuang2007_Data.w2.models import Task


def test_days_left_never_returns_a_negative_value() -> None:
    task = Task("DS exam", 5, 6.0, date(2026, 10, 30))

    assert task.days_left(date(2026, 10, 26)) == 4
    assert task.days_left(date(2026, 11, 2)) == 0


@pytest.mark.parametrize("importance", [0, 6, -1])
def test_importance_out_of_range_is_rejected(importance: int) -> None:
    with pytest.raises(ValueError):
        Task("DS exam", importance, 6.0, date(2026, 10, 30))


@pytest.mark.parametrize("importance", [1, 2, 3, 4, 5])
def test_valid_importance_is_accepted(importance: int) -> None:
    task = Task("DS exam", importance, 6.0, date(2026, 10, 30))

    assert task.importance == importance
