
def merge(T, l0, r0, l1, r1):
    n = r1 - l0 + 1
    buffer = [None for _ in range(n)]

    idx0, idx1 = l0, l1
    buffer_idx = 0

    while buffer_idx < n:
        if idx1 > r1 or (idx0 <= r0 and T[idx0] < T[idx1]):
            buffer[buffer_idx] = T[idx0]
            idx0 += 1
        else:
            buffer[buffer_idx] = T[idx1]
            idx1 += 1
        buffer_idx += 1

    for i in range(n):
        T[i + l0] = buffer[i]


def _merge_sort(T, l, r):
    n = r - l + 1
    if n == 2:
        if T[l] > T[r]:
            T[l], T[r] = T[r], T[l]
    elif n > 2:
        center = (l + r) // 2
        _merge_sort(T, l, center)
        _merge_sort(T, center + 1, r)
        merge(T, l, center, center + 1, r)


def merge_sort(T):
    _merge_sort(T, 0, len(T) - 1)
    return T
