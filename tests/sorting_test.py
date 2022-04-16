#!/usr/bin/env python3
import random


from asd.sorting.heap_sort import *
from asd.sorting.insertion_sort import *
from asd.sorting.merge_sort import *
from asd.sorting.quick_sort import *
from asd.sorting.radix_sort import *
from asd.sorting.bubble_sort import *
from asd.sorting.selection_sort import *
from utils import test

random.seed(42)

sorting_fn = (
    heap_sort,
    merge_sort,
    quick_sort,
    radix_sort,
    insertion_sort,
    bubble_sort,
    selection_sort
)

print("Sorting shuffled arrays:")
outputs = [[v for v in range(1000)] for _ in range(10)]
inputs = [[random.sample(t, len(t))] for t in outputs]
for fn in sorting_fn:
    test(fn, inputs, outputs, fn.__name__)

print("Sorting sorted arrays:")
inputs = [[t.copy()] for t in outputs]
for fn in sorting_fn:
    test(fn, inputs, outputs, fn.__name__)

print("Sorting reversed arrays:")
inputs = [[t.copy()[::-1]] for t in outputs]
for fn in sorting_fn:
    test(fn, inputs, outputs, fn.__name__)
