import utils
from collections import deque


def bfs(G, s, fn=None):
    queue = deque([s])
    visited = [False for _ in range(len(G))]
    visited[s] = True

    while queue:
        v = queue.popleft()

        for u in G[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True

        print(v, ":", queue)
        if fn is not None:
            fn(v)


if __name__ == "__main__":
    G = utils.gen_graph(7, 30)
    T = [False] * len(G)

    def fn(v):
        global G
        T[v] = True
        utils.render_graph(G, T)
    bfs(G, 1, fn)
