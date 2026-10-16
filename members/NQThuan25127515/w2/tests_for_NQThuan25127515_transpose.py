"""W2-4: tests for transpose (W1-4)."""
from members.NQThuan25127515.w1.translate import transpose


def test_square_matrix():
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_rectangular_matrix():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_one_row_becomes_one_column():
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]


def test_one_column_becomes_one_row():
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]


def test_single_element():
    assert transpose([[7]]) == [[7]]


def test_transpose_twice_returns_original():
    m = [[1, 2, 3], [4, 5, 6]]
    assert transpose(transpose(m)) == m


def test_input_is_not_modified():
    m = [[1, 2], [3, 4]]
    transpose(m)
    assert m == [[1, 2], [3, 4]]