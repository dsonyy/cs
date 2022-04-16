from typing import List, Union


def series_leader(T: List[int]) -> Union[int, None]:
    """
    Finds the series leader in a list of integers.
    Leader is an integer which occurs more than half of the time in the list.

    :param T: List of integers.
    :return: The series leader or None if there is no series leader.
    """
    if len(T) == 0:
        return None

    # look for a leader candidate
    candidate: int = T[0]
    cnt: int = 1
    for v in T[1:]:
        if v == candidate:
            cnt += 1
        elif cnt == 1:
            candidate = v
        else:
            cnt -= 1

    # check if the candidate is a leader
    cnt = 0
    for v in T:
        if v == candidate:
            cnt += 1

    if cnt > (len(T) // 2):
        return candidate
    else:
        return None


if __name__ == "__main__":
    print(series_leader([5, 5, 1, 5, 2, 3, 4, 5, 5, 5, 7]))
