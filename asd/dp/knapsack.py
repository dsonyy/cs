from typing import List

from numpy import piecewise

DP: List[List[int]] = []
Weights: List[int] = []
Prices: List[int] = []


def _knapsack(i: int, cap: int) -> int:
    if i == 0:
        if Weights[0] <= cap:
            return Prices[i]
        else:
            return 0
    if DP[i][cap] is not None:
        return DP[i][cap]

    if cap - Weights[i] >= 0:
        DP[i][cap] = max(_knapsack(i - 1, cap),
                         _knapsack(i - 1, cap - Weights[i]) + Prices[i])
    else:
        DP[i][cap] = _knapsack(i - 1, cap)

    return DP[i][cap]


def knapsack(weights: List[int], prices: List[int], max_cap: int) -> int:
    global DP
    global Weights
    global Prices

    N = len(weights)
    Weights = weights
    Prices = prices
    DP = [[None for _ in range(max_cap + 1)] for _ in range(N)]
    return _knapsack(N - 1, max_cap)


if __name__ == "__main__":
    print(knapsack(
        [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        [92, 57, 49, 68, 60, 43, 67, 84, 87, 72],
        165,
    ))
