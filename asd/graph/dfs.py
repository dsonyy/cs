def dfs(G, s, fn=None):
    stack = [s]
    visited = [False for _ in range(len(G))]
    visited[s] = True

    while stack:
        v = stack.pop()

        for u in G[v]:
            if not visited[u]:
                stack.append(u)
                visited[u] = True

        print(v, ":", stack)
        if fn is not None:
            fn(v)


if __name__ == "__main__":
    G = [[2, 1, 8], [0], [0, 3, 4], [2, 5],
         [2, 6, 7], [3], [4, 7], [6, 4], [0]]
    dfs(G, 0)
