from members.NQThuan25127515.w1.translate import primes_up_to


def test_negative_limit():
    assert primes_up_to(-5) == []


def test_zero_limit():
    assert primes_up_to(0) == []


def test_one_is_not_prime():
    assert primes_up_to(1) == []


def test_smallest_prime():
    assert primes_up_to(2) == [2]


def test_prime_upper_bound_is_included():
    assert primes_up_to(13) == [2, 3, 5, 7, 11, 13]


def test_composite_upper_bound():
    assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_prime_square_is_excluded():
    assert primes_up_to(49) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    ]


def test_primes_up_to_one_hundred():
    expected = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    ]
    assert primes_up_to(100) == expected
