from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import prioritise

TODAY = date(2026, 10, 26)


def test_pdf_example():
    exam = Task("DS exam", 5, 6, date(2026, 10, 30))
    hw = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    assert prioritise([exam, hw], TODAY) == [hw, exam]


def test_empty():
    assert prioritise([], TODAY) == []


def test_due_today_and_overdue_do_not_crash():
    a = Task("a", 3, 1, date(2026, 10, 26))
    b = Task("b", 3, 1, date(2026, 10, 20))
    assert len(prioritise([a, b], TODAY)) == 2


def test_does_not_modify_input():
    t = [Task("x", 1, 1, date(2026, 11, 1)), Task("y", 5, 1, date(2026, 10, 27))]
    prioritise(t, TODAY)
    assert [x.title for x in t] == ["x", "y"]


def test_same_score_is_deterministic():
    a = Task("b", 2, 1, date(2026, 10, 28))
    b = Task("a", 2, 1, date(2026, 10, 28))
    assert [t.title for t in prioritise([a, b], TODAY)] == ["a", "b"]