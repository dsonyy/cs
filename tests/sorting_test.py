from asd.sorting import *
import random
from utils import test

sorting_fns = (
    # bucket_sort,
    # counting_sort,
    heap_sort,
    # insertion_sort,
    # merge_sort,
    # quick_sort,
    # radix_sort,
)

outputs = [[v for v in range(100)] for _ in range(25)]
inputs = [[random.sample(t, len(t))] for t in outputs]

for fn in sorting_fns:
    test(heap_sort, inputs, outputs, fn.__name__)
