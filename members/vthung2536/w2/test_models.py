from datetime import date

import pytest
from models import Task

TODAY = date(2026, 10, 14)
 
 
def make(importance=3, deadline=date(2026, 10, 30)):
    return Task("DS exam", importance, 6.0, deadline)
 
 
# ---- days_left ----
def test_days_left_future():
    assert make(deadline=date(2026, 10, 30)).days_left(TODAY) == 16
 
 
def test_days_left_today_is_zero():
    assert make(deadline=TODAY).days_left(TODAY) == 0
 
 
def test_days_left_past_deadline_is_zero():
    assert make(deadline=date(2026, 10, 1)).days_left(TODAY) == 0
 
 
# ---- importance validation ----
@pytest.mark.parametrize("value", [0, 6, -1])
def test_importance_out_of_range_raises(value):
    with pytest.raises(ValueError):
        make(importance=value)
 
 
@pytest.mark.parametrize("value", [1, 2, 3, 4, 5])
def test_importance_in_range_ok(value):
    assert make(importance=value).importance == value