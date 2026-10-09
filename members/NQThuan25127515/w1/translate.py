"""W1-4: C++ -> Python translations."""


def binary_search(a: list[int], key: int) -> int:
    """Return index of key in sorted list a, or -1 if absent.

    Difference from C++: no (int)a.size() cast is needed, and Python
    ints never overflow, so (lo + hi) // 2 would be safe anyway.
    """
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def insertion_sort(a: list[int]) -> list[int]:
    """Sort a in place and return it.

    Difference from C++: elements are swapped with one tuple
    assignment, with no temporary variable.
    """
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
    return a


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Return the transpose of a matrix (list of rows).

    Difference from C++: zip(*matrix) swaps rows and columns in one
    expression instead of two nested index loops filling a new vector.
    """
    return [list(row) for row in zip(*matrix)]


def sieve(n: int) -> list[int]:
    """Return all primes <= n.

    Difference from C++: slice assignment crosses off all multiples at
    once instead of an inner loop over vector<bool>.
    """
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i::i] = [False] * len(range(i * i, n + 1, i))
    return [i for i, p in enumerate(is_prime) if p]