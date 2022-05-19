import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from typing import List, Union
import random
import graphviz


def gen_graph(v: int, e: int) -> List[List[int]]:
    G = [[] for _ in range(v)]
    E = set([])

    e = min(e, v*(v - 1) // 2)

    while len(E) < e:
        a = random.randint(0, v - 1)
        b = random.randint(0, v - 1)
        if a != b and (a, b) not in E and (b, a) not in E:
            E.add((a, b))
    for ee in E:
        G[ee[0]].append(ee[1])
        G[ee[1]].append(ee[0])

    for g in G:
        g.sort()

    return G


def gen_complete_graph(v: int) -> List[List[int]]:
    return [[j for j in range(v) if i != j] for i in range(v)]


def matrix_to_list(M: List[List[bool]]) -> List[List[int]]:
    V: int = len(M)
    L: List[List[int]] = [[] for _ in range(V)]

    for v in range(V):
        for u in range(V):
            if M[v][u]:
                L[v].append(u)
    return L


def list_to_matrix(L: List[List[int]]) -> List[List[int]]:
    V: int = len(L)
    M: List[List[bool]] = [[False for _ in range(V)] for _ in range(V)]

    for v, neighbors in enumerate(L):
        for u in neighbors:
            M[v][u] = True

    return M


def print_matrix(M: List[List[bool]]) -> None:
    for row in M:
        for e in row:
            print(int(e), end="")
        print()


def render_graph(L: List[List[int]],
                 T0: Union[List[bool], None] = None,
                 T1: Union[List[bool], None] = None,
                 T2: Union[List[bool], None] = None) -> None:
    dot = graphviz.Graph()

    for v in range(len(L)):
        if T0 is not None and T0[v]:
            dot.node(str(v), color="red", penwidth="2.0")
        elif T1 is not None and T1[v]:
            dot.node(str(v), color="green", penwidth="2.0")
        elif T2 is not None and T2[v]:
            dot.node(str(v), color="blue", penwidth="2.0")
        else:
            dot.node(str(v))

    for v, neighbors in enumerate(L):
        for u in neighbors:
            if u >= v:
                dot.edge(str(v), str(u))

    img: np.array = Image.open(BytesIO(dot.pipe("jpg")))
    cv2.imshow("Graph", np.array(img)[:, :, ::-1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


G = gen_graph(5, 6)
T = [0, 1, 0, 0, 0]
T0 = [0, 0, 1, 0, 0]
T1 = [0, 0, 1, 1, 0]
render_graph(G, T, T0, T1)
