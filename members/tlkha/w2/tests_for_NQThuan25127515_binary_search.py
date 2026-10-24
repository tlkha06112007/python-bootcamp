import pytest

from members.NQThuan25127515.w1.translate import binary_search


def test_duplicates_returns_a_valid_index():
    a = [1, 2, 2, 2, 3]
    i = binary_search(a, 2)
    assert i in (1, 2, 3)  # any index holding 2 is correct
    assert a[i] == 2


def test_all_elements_equal():
    a = [5, 5, 5, 5]
    i = binary_search(a, 5)
    assert 0 <= i < len(a)
    assert a[i] == 5


def test_first_element():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_last_element():
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_smaller_than_all_elements():
    assert binary_search([10, 20, 30], 5) == -1


def test_larger_than_all_elements():
    assert binary_search([10, 20, 30], 40) == -1


def test_missing_value_between_elements():
    assert binary_search([10, 20, 30], 25) == -1


def test_single_element_found():
    assert binary_search([7], 7) == 0


def test_single_element_not_found():
    assert binary_search([7], 3) == -1
    assert binary_search([7], 9) == -1


def test_empty_list():
    assert binary_search([], 1) == -1


@pytest.mark.parametrize("n", [1, 2, 3, 10, 11])
def test_finds_every_element(n):
    a = list(range(0, n * 2, 2))
    for idx, value in enumerate(a):
        assert binary_search(a, value) == idx