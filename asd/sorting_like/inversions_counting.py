from typing import List


def inversions_counting(T: List[int]) -> int:
    """
    Counts the number of inversions in a list.
    Complexity: O(n^2)

    :param T: a list of integers
    """
    cnt: int = 0
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            if T[i] > T[j]:
                cnt += 1
    return cnt


def inversions_counting(T: List[int]) -> int:
    """
    Effectively counts the number of inversions in a list.

    :param T: a list of integers
    """
    raise NotImplementedError
