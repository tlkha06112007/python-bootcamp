import pytest

from members.khoavn1302.w3.log_stats import analyse


def test_empty():
    assert analyse([]) == {"counts": {}, "p95": {}, "slowest": None}


def test_one_request():
    assert analyse([("fee", 12.5)]) == {
        "counts": {"fee": 1}, "p95": {"fee": 12.5}, "slowest": "fee"
    }


def test_multiple_routes():
    pairs = [("fee", 100), ("rag", 900), ("fee", 300), ("rag", 1100), ("fee", 200)]
    result = analyse(pairs)
    assert result["counts"] == {"fee": 3, "rag": 2}
    assert result["p95"] == {"fee": 300, "rag": 1100}
    assert result["slowest"] == "rag"


@pytest.mark.parametrize("n, expected", [(19, 19), (20, 19), (21, 20)])
def test_p95(n, expected):
    pairs = [("fee", ms) for ms in range(n, 0, -1)]
    assert analyse(pairs)["p95"]["fee"] == expected


def test_repeated_latency():
    result = analyse([("fee", 0), ("fee", 2.5), ("fee", 2.5)])
    assert result["counts"] == {"fee": 3}
    assert result["p95"] == {"fee": 2.5}


def test_slowest_uses_p95():
    pairs = [("fee", 1000)] + [("fee", 10)] * 19 + [("rag", 50)]
    result = analyse(pairs)
    assert result["p95"] == {"fee": 10, "rag": 50}
    assert result["slowest"] == "rag"


def test_input_unchanged():
    pairs = [("rag", 300), ("fee", 100), ("rag", 200)]
    original = pairs.copy()
    analyse(pairs)
    assert pairs == original
