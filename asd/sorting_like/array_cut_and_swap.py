from typing import List


def array_cut_and_swap(T: List[int], cut: int) -> None:
    """
    Cuts the array in two parts and swaps the elements in the first part with
    the elements in the second part.

    Space complexity: O(n)
    """
    if len(T) <= 1:
        return

    # cut the array in two parts
    l: List[int] = T[:cut]
    r: List[int] = T[cut:]

    # swap the elements in the first part with the elements in the second part
    i: int = 0
    for j in range(len(r)):
        T[i] = r[j]
        i += 1
    for j in range(len(l)):
        T[i] = l[j]
        i += 1


def array_reverse(T: List[int], l: int, r: int) -> None:
    """
    Reverses the elements in the range [l, r].
    """
    n = r - l + 1
    for i in range(n // 2):
        T[l + i], T[r - i] = T[r - i], T[l + i]


def array_cut_and_swap(T: List[int], cut: int) -> None:
    """
    Cuts the array in two parts and swaps the elements in the first part with
    the elements in the second part.

    Space complexity: O(1)
    """
    if len(T) <= 1:
        return

    # let's assume it repesents our input array
    #           RR
    #         RRRR
    #       RRRRRR
    #     LLRRRRRR
    #   LLLLRRRRRR
    # LLLLLLRRRRRR
    #
    # so this would be the output array
    #     RR
    #   RRRR
    # RRRRRR
    # RRRRRR    LL
    # RRRRRR  LLLL
    # RRRRRRLLLLLL

    # 1. flip the left part
    #           RR
    #         RRRR
    #       RRRRRR
    # LL    RRRRRR
    # LLLL  RRRRRR
    # LLLLLLRRRRRR
    array_reverse(T, 0, cut)

    # 2. flip the right part
    #       RR
    #       RRRR
    #       RRRRRR
    # LL    RRRRRR
    # LLLL  RRRRRR
    # LLLLLLRRRRRR
    array_reverse(T, cut + 1, len(T) - 1)

    # 3. flip the whole array
    #     RR
    #   RRRR
    # RRRRRR
    # RRRRRR    LL
    # RRRRRR  LLLL
    # RRRRRRLLLLLL
    array_reverse(T, 0, len(T) - 1)


if __name__ == "__main__":
    T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    array_cut_and_swap(T, 5)
    print(T)
