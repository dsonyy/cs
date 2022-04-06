
from math import log


def counting_sort(T, key_n, key_fn):
    counters = [0] * key_n
    results = [0] * len(T)

    for v in T:
        counters[key_fn(v)] += 1
    for i in range(1, key_n):
        counters[i] += counters[i - 1]
    for i in range(len(T) - 1, -1, -1):
        results[counters[key_fn(T[i])] - 1] = T[i]
        counters[key_fn(T[i])] -= 1

    for i in range(len(T)):
        T[i] = results[i]


def radix_sort(T):
    base = 10
    digits = int(log(max(T), base) + 1)
    for i in range(digits):
        counting_sort(T, base, lambda v: v // base**i % base)
