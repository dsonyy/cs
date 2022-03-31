
def _quick_sort(T, l, r):
    if l > r:
        return
    pivot = T[r]
    i = l
    for j in range(l, r):
        if T[j] < pivot:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    _quick_sort(T, l, i - 1)
    _quick_sort(T, i + 1, r)


def quick_sort(T):
    _quick_sort(T, 0, len(T) - 1)


def quick_sort2(T):
    pivot = T[-1]
    left = [v for v in T if v <= pivot]
    right = [v for v in T if v > pivot]

    i = 0
    for v in left:
        T[i] = v
        i += 1
    T[i] = pivot
    for v in right:
        T[i] = v
        i += 1
