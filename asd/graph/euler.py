
def has_euler_path(G):
    pass


def has_euler_cycle(G):
    pass


def _euler_path(G, history):
    s = 0

    odds = 0
    for v in range(len(G)):
        if len(G[v]) % 2 == 1:
            s = v
            odds += 1

    if odds != 0 and odds != 2:
        return False


def _euler_cycle(G, history):
    if _count_odd_degrees(G) != 0:
        return False
