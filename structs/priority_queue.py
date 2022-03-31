from random import shuffle


class Element:
    def __init__(self, prio, val=None) -> None:
        self.prio = prio
        self.val = val

    def __repr__(self) -> str:
        return self.prio


class PQ:
    def __init__(self):
        self.T = []

    def push(self, v):
        self.T.append(v)

        i = len(self.T) - 1
        parent_i = (i - 1) // 2

        while parent_i >= 0 and self.T[i].prio > self.T[parent_i].prio:
            self.T[i], self.T[parent_i] = self.T[parent_i], self.T[i]
            i = parent_i
            parent_i = (i - 1) // 2

    def pop(self):
        if not self.T:
            return None
        self.T[-1], self.T[0] = self.T[0], self.T[-1]
        v = self.T.pop()
        self._heapify(0)
        return v

    def _heapify(self, idx):
        left = 2*idx + 1
        right = 2*idx + 2
        max_idx = idx
        if left < len(self.T) and self.T[left].prio > self.T[max_idx].prio:
            max_idx = left
        if right < len(self.T) and self.T[right].prio > self.T[max_idx].prio:
            max_idx = right
        if max_idx != idx:
            self.T[max_idx], self.T[idx] = self.T[idx], self.T[max_idx]
            self._heapify(max_idx)


pq = PQ()

prios = [v for v in range(10)]
shuffle(prios)
for p in prios:
    pq.push(Element(p))

for v in pq.T:
    print(v.prio, end=" ")
print()

for _ in prios:
    pq.pop()
    for v in pq.T:
        print(v.prio, end=" ")
    print()
