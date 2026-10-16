from dataclasses import dataclass
import pytest

from members.vhphuc.w2.errors import InfeasiblePlan, check_feasible


# Dummy Task class for isolated testing
@dataclass
class DummyTask:
    effort_h: float


def test_check_feasible_valid():
    tasks = [DummyTask(2.0), DummyTask(3.0)]
    # Total effort is 5.0h <= 10.0h -> Should not raise
    check_feasible(tasks, 10.0)


def test_check_feasible_empty():
    # Empty task list -> Total effort 0.0h <= 5.0h -> Should not raise
    check_feasible([], 5.0)


def test_check_feasible_exceeded():
    tasks = [DummyTask(4.0), DummyTask(7.0)]
    # Total effort is 11.0h > 10.0h -> Should raise InfeasiblePlan
    with pytest.raises(InfeasiblePlan) as exc_info:
        check_feasible(tasks, 10.0)

    # Verify exception attributes and string representation
    err = exc_info.value
    assert err.needed_h == 11.0
    assert err.available_h == 10.0
    assert str(err) == "need 11.0 h but only 10.0 h available"