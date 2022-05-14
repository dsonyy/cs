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
        if res <= 0 or res == DP[i - 1][cap]:
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
    # print(knapsack_items(
    #     [19, 7, 15, 15, 7, 3, 7, 15, 19, 7],
    #     [3, 18, 28, 18, 20, 18, 4, 21, 44, 27], 40
    # ),)
    T = [(3, 3, 4, 19), (3, 11, 17, 7), (4, 8, 15, 15), (3, 1, 7, 15), (4, 12, 17, 7),
         (3, 1, 7, 3), (4, 8, 9, 7), (3, 11, 18, 15), (4, 20, 31, 19), (3, 17, 26, 7)]
    Prices = [x[3] for x in T]
    Weights = [x[0] * (x[2] - x[1]) for x in T]

    DP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 18, 18, 18, 18, 18],
          [0, 0, 0, 18, 18, 18, 18, 18, 18, 18, 18,
              18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
          [0, 0, 0, 18, 18, 18, 18, 18, 18, 18, 22,
           22, 22, 22, 22, 22, 22, 22, 22, 22, 22],
          [0, 0, 0, 18, 18, 18, 18, 18, 18, 18, 22,
           22, 22, 22, 22, 28, 28, 28, 46, 46, 46],
          [0, 0, 0, 18, 18, 18, 18, 18, 18, 18, 36,
           36, 36, 36, 36, 36, 36, 40, 46, 46, 46],
          [0, 0, 0, 18, 18, 18, 18, 20, 20, 20, 38,
           38, 38, 38, 38, 38, 38, 42, 46, 46, 46],
          [0, 0, 0, 18, 18, 18, 18, 20, 20, 20, 38,
           38, 38, 38, 38, 38, 38, 42, 46, 46, 46],
          [0, 0, 0, 18, 18, 18, 18, 27, 27, 27, 45,
           45, 45, 45, 45, 45, 45, 49, 49, 49, 49],
          [0, 0, 0, 18, 18, 18, 18, 27, 27, 27, 45, 45, 45, 45, 45, 45, 45, 49, 49, 49, 49]]
    get_items(len(DP), len(DP[0]) - 1)
    print_dp()
