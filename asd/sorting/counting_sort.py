
def counting_sort(T, a, b):
    n = len(T)
    k = b - a + 1
    counters = [0] * k
    results = [0] * n

    for v in T:
        counters[v - a] += 1
    for i in range(1, k):
        counters[i] += counters[i - 1]
    for i in range(n - 1, -1, -1):
        results[counters[T[i] - a] - 1] = T[i]
        counters[T[i] - a] -= 1

    for i in range(n):
        T[i] = results[i]
