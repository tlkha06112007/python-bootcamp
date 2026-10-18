from datetime import date

import pytest

from shared.contract import Task
from shared.study_planner.allocate import allocate


def make(title: str, effort_h: float) -> Task:
    return Task(title, 3, effort_h, date(2026, 10, 30))


def test_enough_hours_gives_every_task_its_full_time():
    a, b = make("a", 2.0), make("b", 3.0)
    blocks = allocate([a, b], 10.0)
    assert [(bl.task, bl.hours) for bl in blocks] == [(a, 2.0), (b, 3.0)]


def test_last_task_gets_only_the_remaining_hours():
    a, b, c = make("a", 2.0), make("b", 3.0), make("c", 5.0)
    blocks = allocate([a, b, c], 4.0)
    assert [(bl.task, bl.hours) for bl in blocks] == [(a, 2.0), (b, 2.0)]


def test_pdf_example_two_hours():
    hw, exam = make("Assignment", 1.5), make("DS exam", 6.0)
    blocks = allocate([hw, exam], 2.0)
    assert [bl.hours for bl in blocks] == pytest.approx([1.5, 0.5])


def test_zero_or_negative_hours_gives_no_blocks():
    assert allocate([make("a", 2.0)], 0.0) == []
    assert allocate([make("a", 2.0)], -5.0) == []


def test_empty_tasks():
    assert allocate([], 10.0) == []