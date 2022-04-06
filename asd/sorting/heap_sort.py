def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i - 1) // 2


def heapify(T, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r
    if i != max_ind:
        T[max_ind], T[i] = T[i], T[max_ind]
        heapify(T, n, max_ind)


def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)


def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)
    return T
