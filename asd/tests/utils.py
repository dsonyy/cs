from copy import deepcopy
import traceback
from termcolor import cprint
from typing import Callable, List, Any
import time


test_group = 0


def test(fn: Callable[..., bool],
         inputs: List[List[Any]],
         outputs: List[Any],
         test_name: str) -> bool:
    global test_group
    test_group += 1
    cprint(f"{test_group}. {test_name}", color="cyan")

    if len(inputs) != len(outputs):
        cprint("Length of inputs and outputs are not the same.", color="red")
        return False
    n = len(inputs)

    ok = True
    elapsed_all = 0
    for i in range(n):
        input = deepcopy(inputs[i])
        start = time.time()
        try:
            result = fn(*input)
        except Exception as e:
            cprint(f"TEST {test_group}.{i} EXCEPTION", color="red")
            traceback.print_exc()
            ok = False
            continue
        elapsed = time.time() - start
        elapsed_all += elapsed

        if result != outputs[i]:
            cprint(f"TEST {test_group}.{i} BAD RESULT", color="red")
            cprint(f"\tInput:  {inputs[i]}")
            cprint(f"\tOutput: {outputs[i]}")
            cprint(f"\tResult: {result}")
            ok = False
    if ok:
        cprint(f"   OK {elapsed_all:0.3f}s", "green")
    return ok
