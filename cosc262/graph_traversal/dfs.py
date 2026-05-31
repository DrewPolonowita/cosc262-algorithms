def dfs_tree(adjacency_list, v, trace=False):
    """
    Takes an adjacency list and a starting vertex and returns a DFS Tree
    :param adjacency_list: an adjacency_list representing a graph
    :param v: the starting vertex
    :param trace: prints the stack trace
    :return: a list representing a tree formed by DFS traversal (MST)
    """
    n = len(adjacency_list)
    parent = [None] * n
    state = ['u'] * n
    state[v] = 'd'

    dfs_loop(adjacency_list, parent, state, v, trace=trace)

    return parent

def dfs_loop(adjacency_list, parent, state, v, trace=False, call_stack=None, finish_order=None):
    if call_stack is None:
        call_stack = []
    if finish_order is None:
        finish_order = []



    call_stack.append(v)
    if trace:
        print(f"{call_stack, state, parent}")

    for u, _ in adjacency_list[v]:
        if state[u] == 'u':
            state[u] = 'd'
            parent[u] = v
            call_stack.append(u)
            dfs_loop(adjacency_list, parent, state, u, trace=trace, call_stack=call_stack, finish_order=finish_order)

    finish_order.append(v)
    state[v] = 'p'

    if trace:
        print(f"{call_stack, state, parent}")

    call_stack.pop()


def topological_ordering(adjacency_list):
    """
    Returns a topological ordering for the given adjacency list
    :param adjacency_list: the adjacency list for a directed acyclic graph
    :return: a topological ordering for a directed acyclic graph
    """
    n = len(adjacency_list)
    parent = [None] * n
    state = ['u'] * n
    finish_order = []

    for v in range(0, n):
        if state[v] == 'u':
            state[v] = 'd'
            dfs_loop(adjacency_list, parent, state, v, finish_order=finish_order)

    return finish_order[::-1]

def is_acyclic(adjacency_list):
    """
    Returns true if the given graph contains a cycle
    :param adjacency_list: the graph to check if it contains a cycle as an adjacency list
    :return: true if the graph contains a cycle
    """
    n = len(adjacency_list)
    state = ['u'] * n

    def contains_cycle(adjacency_list, state, v):
        for u, _ in adjacency_list[v]:
            if state[u] == 'u':
                state[u] = 'd'
                if contains_cycle(adjacency_list, state, u):
                    return True
            elif state[u] == 'd':
                if not u == v:
                    return True

        state[v] = 'p'
        return False

    for v in range(0, n):
        state[v] = 'd'
        if contains_cycle(adjacency_list, state, v):
            return False

    return True