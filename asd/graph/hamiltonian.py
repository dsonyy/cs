
def _check_cycle(G, stack):
    if len(stack) != len(G):
        return False

    if stack[0] in G[stack[-1]]:
        return True

    return False


def _hamiltonian_cycle(G, stack, visited):
    if _check_cycle(G, stack):
        return True

    v = stack[-1]
    for u in G[v]:
        if not visited[u]:
            stack.append(u)
            visited[u] = True

            if _hamiltonian_cycle(G, stack, visited):
                return True

            visited[u] = False
            stack.pop()

    return False


def _hamiltonian_path(G, stack, visited):
    if len(G) == len(stack):
        return True

    v = stack[-1]
    for u in G[v]:
        if not visited[u]:
            stack.append(u)
            visited[u] = True

            if _hamiltonian_path(G, stack, visited):
                return True

            visited[u] = False
            stack.pop()

    return False


def hamiltonian_cycle(G):
    stack = [0]
    visited = [i == 0 for i in range(len(G))]
    if _hamiltonian_cycle(G, stack, visited):
        return stack
    return None


def hamiltonian_path(G):
    for s in range(len(G)):
        stack = [s]
        visited = [i == s for i in range(len(G))]
        if _hamiltonian_path(G, stack, visited):
            return stack
    return None


if __name__ == "__main__":
    import utils
    while True:
        G = utils.gen_graph(5, 4)
        print(hamiltonian_cycle(G))
        print(hamiltonian_path(G))
        utils.render_graph(G, sleep_ms=0)
