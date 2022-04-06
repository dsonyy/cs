

def partition(T, l, r):
    pivot = T[r]
    i = l
    for j in range(l, r):
        if T[j] <= pivot:
            T[j], T[i] = T[i], T[j]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def _quick_sort(T, l, r):
    """ Naive quick sort implementation. Might not handle large (nearly) sorted
    arrays: stack overflow.
    """
    if l < r:
        c = partition(T, l, r)
        _quick_sort(T, l, c - 1)
        _quick_sort(T, c + 1, r)


def _quick_sort(T, l, r):
    """ Simple quick sort implementation with O(log n) space complexity. Might 
    not handle large (nearly) sorted arrays: long execution time.
    """
    while l < r:
        c = partition(T, l, r)
        if (c - l) < (r - c):
            _quick_sort(T, l, c - 1)
            l = c + 1
        else:
            _quick_sort(T, c + 1, r)
            r = c - 1


def quick_sort(T):
    _quick_sort(T, 0, len(T) - 1)
    return T
