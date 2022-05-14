from collections import deque


def bfs(G, s):
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


if __name__ == "__main__":
    G = [[2, 1, 8], [0], [0, 3, 4], [2, 5],
         [2, 6, 7], [3], [4, 7], [6, 4], [0]]
    bfs(G, 1)
