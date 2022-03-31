from random import randrange


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


if __name__ == "__main__":
    for _ in range(100):
        a = randrange(0, 100)
        b = a + randrange(1, 100)
        n = randrange(10, 200)
        T = [randrange(a, b) for _ in range(n)]
        A = sorted(T)
        B = T.copy()
        counting_sort(B, a, b)
        if B != A:
            print("ERR!")
            print("in: ", T)
            print("out:", B)
            break
    else:
        print("OK")
