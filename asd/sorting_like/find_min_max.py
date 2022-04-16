def find_min_max(T):
    """
    Find min and max value in an unsorted list using only 3/2*N comparisons.
    """
    N = len(T)
    max_, min_ = T[0], T[0]
    for i in range(1, N, 2):  # floor(N / 2) iterations
        if T[i - 1] > T[i]:  # the first comparison
            local_max, local_min = T[i - 1], T[i]
        else:
            local_max, local_min = T[i], T[i - 1]

        if local_max > max_:  # the second comparison
            max_ = local_max
        if local_min < min_:  # the thrid comparison
            min_ = local_min

    if N % 2 == 1:  # additional check when N is odd
        if T[N - 1] > max_:
            max_ = T[N - 1]
        if T[N - 1] < min_:
            min_ = T[N - 1]

    return min_, max_


if __name__ == "__main__":
    import random
    for _ in range(100):
        T = [random.randint(0, 100) for _ in range(30)]
        print(find_min_max(T) == (min(T), max(T)))
