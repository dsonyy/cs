import numpy as np
from typing import Tuple, List


class MatrixGraph:
    """Graphs represented as adjacency matrix."""

    def __init__(self, v: int = 0):
        self.v: int = v
        self.mat: np.array = np.zeros((self.v, self.v), dtype=np.bool)

    def add_vertice(self) -> int:
        self.v += 1
        self.mat.resize((self.v, self.v), refcheck=False)
        return self.v - 1

    def add_vertices(self, v: int) -> Tuple[int, int]:
        self.v += v
        self.mat.resize((self.v, self.v), refcheck=False)
        return (self.v - v, self.v - 1)

    def add_edge(self, v0: int, v1: int):
        self.mat[v0][v1] = True
        self.mat[v1][v0] = True

    def add_edges(self, e: List[Tuple[int, int]]):
        for v0, v1 in e:
            self.add_edge(v0, v1)

    def remove_edge(self, v0: int, v1: int):
        self.mat[v0][v1] = False
        self.mat[v1][v0] = True

    def remove_vertice(self, v: int):
        self.mat = np.delete(self.mat, v, 0)
        self.mat = np.delete(self.mat, v, 1)

    def get_neighbors(self, v: int) -> List[int]:
        return [u for u, edge in enumerate(self.mat[v]) if edge]

    def check_neighborhood(self, v0: int, v1: int) -> bool:
        return self.mat[v0][v1]


class ListGraph:
    """Graphs represented as an adjacency list."""

    def __init__(self, v: int = 0):
        self.v: int = v
        self.l: List[List[int]] = [[] for _ in range(v)]

    def add_vertice(self) -> int:
        self.v += 1
        self.l.append([])
        return self.v - 1

    def add_vertices(self, v: int) -> Tuple[int, int]:
        self.v += v
        for _ in range(v):
            self.l.append([])
        return (self.v - v, self.v - 1)

    def add_edge(self, v0: int, v1: int) -> bool:
        if v0 in self.l[v1]:
            return False
        self.l[v1].append(v0)
        self.l[v0].append(v1)
        return True

    def add_edges(self, e: List[Tuple[int, int]]) -> bool:
        ok = True
        for v0, v1 in e:
            ok &= self.add_edge(v0, v1)
        return ok

    def remove_vertice(self, v: int):
        del self.l[v]

    def remove_edge(self, v0: int, v1: int):
        self.l[v0].remove(v1)
        self.l[v1].remove(v0)

    def get_neighbors(self, v: int) -> List[int]:
        return self.l[v]

    def check_neighborhood(self, v0: int, v1: int) -> bool:
        return v1 in self.l(v0)
