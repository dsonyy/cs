from .insertion_sort import insertion_sort


def bucket_sort(T, a, b):
    width = (b - a + 1) / len(T)
    buckets = [[] for _ in range(len(T))]

    for v in T:
        idx = int((v - a) // width)
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
