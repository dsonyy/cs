from typing import List

DP: List[List[int]] = []
Weights: List[int] = []
Prices: List[int] = []


def _knapsack(i: int, cap: int) -> int:
    if i == 0:
        if Weights[0] <= cap:
            DP[i][cap] = Prices[i]
        else:
            DP[i][cap] = 0
        return DP[i][cap]
    if DP[i][cap] is not None:
        return DP[i][cap]

    if cap - Weights[i] >= 0:
        DP[i][cap] = max(_knapsack(i - 1, cap),
                         _knapsack(i - 1, cap - Weights[i]) + Prices[i])
    else:
        DP[i][cap] = _knapsack(i - 1, cap)

    return DP[i][cap]


def get_items(n: int, cap: int) -> List[int]:
    items = []
    res = _knapsack(n - 1, cap)
    for i in range(n - 1, 0, -1):
        if res == DP[i - 1][cap] or res <= 0:
            items.append(0)
        else:
            items.append(1)
            res -= Prices[i]
            cap -= Weights[i]
    if res >= DP[0][cap] and res > 0:
        items.append(1)
    else:
        items.append(0)

    return items[::-1]


def knapsack(weights: List[int], prices: List[int], max_cap: int) -> int:
    global DP
    global Weights
    global Prices

    N = len(weights)
    Weights = weights
    Prices = prices
    DP = [[None for _ in range(max_cap + 1)] for _ in range(N)]

    return _knapsack(N - 1, max_cap)


def knapsack_items(weights: List[int], prices: List[int], max_cap: int) -> List[int]:
    val = knapsack(weights, prices, max_cap)
    N = len(weights)
    items = get_items(N, max_cap)
    return val, items


def print_dp() -> None:
    for i in range(len(DP[0])):
        for j in range(len(DP)):
            if DP[j][i] is None:
                print("xxxx ", end="")
            else:
                print("{:>4}".format(DP[j][i]), end=" ")
        print()


if __name__ == "__main__":
    print(knapsack_items(
        [4, 5, 6],
        [1, 2, 3], 15
    ),)
