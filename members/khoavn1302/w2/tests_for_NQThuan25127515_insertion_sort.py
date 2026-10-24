from members.NQThuan25127515.w1.translate import insertion_sort


def test_already_sorted():
    nums = [1, 2, 3, 4, 5]
    assert insertion_sort(nums) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    nums = [9, 7, 5, 3, 1]
    assert insertion_sort(nums) == [1, 3, 5, 7, 9]


def test_duplicates():
    nums = [4, 2, 4, 1, 3, 2, 1]
    assert insertion_sort(nums) == [1, 1, 2, 2, 3, 4, 4]


def test_negative_numbers():
    nums = [0, -5, 12, -2, 7, -1]
    assert insertion_sort(nums) == [-5, -2, -1, 0, 7, 12]


def test_all_elements_identical():
    nums = [8, 8, 8, 8]
    assert insertion_sort(nums) == [8, 8, 8, 8]


def test_single_element():
    nums = [42]
    assert insertion_sort(nums) == [42]


def test_sorts_in_place():
    nums = [3, 1, 2]
    res = insertion_sort(nums)
    assert res is nums
    assert nums == [1, 2, 3]