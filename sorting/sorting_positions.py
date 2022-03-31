
from random import shuffle


def element_position(T, l, r, idx):
    """T is an unsorted array. What would be the idx-th element of T
       if T were sorted?
       Time complexity: Θ(n)
    """
    if l == r:
        return T[l]
    elif l > r:
        return None
    elif l < r:
        pivot = T[r]
        i = l
        for j in range(l, r):
            if T[j] < pivot:
                T[i], T[j] = T[j], T[i]
                i += 1
        T[i], T[r] = T[r], T[i]

        if i == idx:
            return T[i]
        elif i < idx:
            return element_position(T, i + 1, r, idx)
        elif i > idx:
            return element_position(T, l, i - 1, idx)


if __name__ == "__main__":
    for _ in range(50):
        T = [i for i in range(100)]
        shuffle(T)
        A = sorted(T)
        for i in range(len(T)):
            if element_position(T, 0, len(T) - 1, i) != A[i]:
                print("ERR!")
                print("in: ", T)
                break
