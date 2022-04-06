
def selection_sort(T):
    for i in range(len(T)):
        min_j = i
        for j in range(i, len(T)):
            if T[min_j] > T[j]:
                min_j = j
        T[i], T[min_j] = T[min_j], T[i]
    return T
