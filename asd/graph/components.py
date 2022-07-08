
def components(G):
    """
    Checks if the graph is connected. Returns the number of components
    and a list of components.
    """
    cps = [None] * len(G)
    stack = []

    counter = 0
    for s in range(len(G)):
        if cps[s] is None:
            stack.append(s)
            while stack:
                v = stack.pop()
                cps[v] = counter

                for u in G[v]:
                    if cps[u] is None:
                        stack.append(u)
            counter += 1
    return counter, cps


def is_connected(G):
    """
    Checks if the graph is connected.
    """
    stack = [0]
    visited = [False] * len(G)

    while stack:
        v = stack.pop()
        visited[v] = True

        for u in G[v]:
            if not visited[u]:
                stack.append(u)
    return all(visited)


if __name__ == "__main__":
    import utils
    while True:
        G = utils.gen_graph()
        print(*components(G), is_connected(G))
        utils.render_graph(G, sleep_ms=0)
