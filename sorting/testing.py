from random import shuffle
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort, quick_sort2

FN = (
    insertion_sort,
    heap_sort,
    merge_sort,
    quick_sort,
    quick_sort2
)

for fn in FN:
    print(fn.__name__ + ": ", end="")
    for _ in range(100):
        T = [i for i in range(100)]
        shuffle(T)
        A = sorted(T)
        B = insertion_sort(T)
        if A != B:
            print("ERR!")
            print("in: ", T)
            print("out:", B)
            break
    else:
        print("OK")
