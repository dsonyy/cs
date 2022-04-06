
def insertion_sort(T):
    for i in range(1, len(T)):
        v = T[i]
        j = i
        while j > 0 and T[j - 1] > v:
            T[j] = T[j - 1]
            j -= 1
        T[j] = v
