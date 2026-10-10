"""Local boundary and reason checks for W1-3, not the instructor's tests."""

import pytest

from members.tmvuonghoang.w1.rules import can_register_thesis, missing


@pytest.mark.parametrize(
    ("credits", "gpa", "eligible", "reasons"),
    [
        (120, 2.0, True, []),
        (150, 4.0, True, []),
        (119, 2.0, False, ["need 1 more credits"]),
        (118, 3.0, False, ["need 2 more credits"]),
        (120, 1.99, False, ["need GPA of at least 2.0"]),
        (150, 1.0, False, ["need GPA of at least 2.0"]),
        (
            119, 1.99, False,
            ["need 1 more credits", "need GPA of at least 2.0"],
        ),
        (
            0, 0.0, False,
            ["need 120 more credits", "need GPA of at least 2.0"],
        ),
    ],
)
def test_thesis_requirements(credits, gpa, eligible, reasons):
    assert can_register_thesis(credits, gpa) is eligible
    assert missing(credits, gpa) == reasons


def test_missing_returns_independent_lists():
    first = missing(118, 2.0)
    first.append("unrelated reason")
    assert missing(118, 2.0) == ["need 2 more credits"]
