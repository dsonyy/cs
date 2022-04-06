import random


def bogo_sort(T):
    while not sorted(T):
        random.shuffle(T)
    return T
