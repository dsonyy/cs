from typing import Callable
from xmlrpc.client import Boolean
from termcolor import colored, cprint
from typing import Callable, List, Any
import time

test_group = 0


def test(fn: Callable[..., Boolean], inputs: List[List[Any]], outputs: List[Any]) -> bool:
    global test_group
    test_group += 1
    cprint(f"TEST GROUP {test_group}", color="cyan")

    if len(inputs) != len(outputs):
        cprint("Length of inputs and outputs are not the same.", color="red")
        return False
    n = len(inputs)

    for i in range(n):
        cprint(f"TEST {test_group}.{i}", end="")
        start = time.time()
        result = fn(*inputs[i])
        elapsed = time.time() - start

        if result == outputs[i]:
            cprint(" OK", color="green")
            cprint(f"\tTime: {elapsed:0.3f}s")
        else:
            cprint(" BAD RESULT", color="red")
            cprint(f"\tInput:  {inputs[i]}")
            cprint(f"\tOutput: {outputs[i]}")
            cprint(f"\tResult: {result}")
            return False
    return True
