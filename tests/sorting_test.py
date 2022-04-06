from asd.sorting import *
import random
from utils import test

sorting_fn = (
    heap_sort,
    insertion_sort,
    merge_sort,
    # quick_sort,
    radix_sort,
)

outputs = [[v for v in range(1000000)] for _ in range(10)]
inputs = [[random.sample(t, len(t))] for t in outputs]

for fn in sorting_fn:
    test(fn, inputs, outputs, fn.__name__)
