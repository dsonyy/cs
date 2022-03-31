from insertion_sort import insertion_sort
from random import uniform, randrange


def bucket_sort(T, a, b):
    n = b - a + 1
    buckets = [[] for _ in range(n)]

    for v in T:
        idx = int(v) - a
        buckets[idx].append(v)

    i = 0
    for bucket in buckets:
        if len(bucket) == 1:
            T[i] = bucket[0]
            i += 1
        elif len(bucket) > 1:
            insertion_sort(bucket)
            for v in bucket:
                T[i] = v
                i += 1


if __name__ == "__main__":
    for _ in range(100):
        a = randrange(0, 100)
        b = a + randrange(1, 100)
        n = randrange(10, 200)
        T = [uniform(a, b) for _ in range(n)]
        A = sorted(T)
        B = T.copy()
        bucket_sort(B, a, b)
        if B != A:
            print("ERR!")
            print("in: ", T)
            print("out:", B)
            break
    else:
        print("OK")
