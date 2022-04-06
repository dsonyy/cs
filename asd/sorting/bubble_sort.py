
def bubble_sort(T):
    for _ in range(1, len(T)):
        for i in range(1, len(T)):
            if T[i - 1] > T[i]:
                T[i - 1], T[i] = T[i], T[i - 1]
    return T
