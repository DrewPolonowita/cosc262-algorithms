from collections import deque

from cosc262.graph_traversal.adjacency_list import transpose


def bfs_tree(adjacency_list, v, trace=False):
    """
    Takes an adjacency list and a starting vertex and returns a BFS Tree
    :param adjacency_list: an adjacency_list representing a graph
    :param v: the starting vertex
    :param trace: prints the stack trace
    :return: a list representing a tree formed by BFS traversal
    """
    n = len(adjacency_list)
    parent = [None] * n

    state = ['u'] * n
    state[v] = 'd'

    q = deque()
    q.append(v)

    bfs_loop(adjacency_list, parent, state, q, trace=trace)
    return parent

def bfs_loop(adjacency_list, parent, state, q, trace=False):
    i = 0
    while len(q) > 0:
        i += 1
        if trace:
            print(f"{i}: {q, state, parent}")
        v = q.popleft()
        for u, _ in adjacency_list[v]:
            if state[u] == 'u':
                parent[u] = v
                state[u] = 'd'
                q.append(u)

        state[v] = 'p'


def shortest_path(adjacency_list, u, v):
    """
    Returns a list of the shortest path from vertex u to v
    :param adjacency_list: an adjacency_list representing a graph G
    :param u: the starting vertex in the graph G
    :param v: the finishing vertex in the graph G
    :return: the shortest path from vertex u to v, and none if no path exists
    """
    parent_array = bfs_tree(adjacency_list, u)

    def recursive_shortest_path(parent_array, u, v):
        if v is None:
            return None

        if u == v:
            return [u]
        else:
            rest_of_path = recursive_shortest_path(parent_array, u, parent_array[v])
            if rest_of_path is None:
                return None

            return recursive_shortest_path(parent_array, u, parent_array[v]) + [v]

    return recursive_shortest_path(parent_array, u, v)

def connected_components(adjacency_list):
    """
    Returns a set of the connected components
    :param adjacency_list: an adjacency_list representing a graph G
    :return: a set containing the connected components of G as sets of vertices
    """
    components = []
    n = len(adjacency_list)
    _ = [None] * n
    state = ['u'] * n

    for u in range(0, n):
        if state[u] == 'u':
            prev_state = state.copy()

            state[u] = 'd'
            q = deque()
            q.append(u)

            bfs_loop(adjacency_list, _, state, q)

            component = set()

            for v, (i,j) in enumerate(zip(state, prev_state)):
                if not i == j:
                    component.add(v)
            components.append(component)


    return components


def is_strongly_connected(adjacency_list):
    """
    Returns true if the graph is strongly connected. All vertices can reach all vertices
    :param adjacency_list: the graph G
    :return: returns true if G is strongly connected
    """
    for graph in [adjacency_list, transpose(adjacency_list)]:
        n = len(graph)
        parent = [None] * n
        state = ['u'] * n
        state[0] = 'd'

        q = deque()
        q.append(0)

        bfs_loop(graph, parent, state, q)
        if 'u' in state:
            return False

    return True