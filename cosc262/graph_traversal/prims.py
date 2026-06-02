import math

def prim(adjacency_list, v, trace=False):
    """
    Returns tree created from a prims traversal which gives a minimal spanning tree on the graph
    :param adjacency_list: a graph in adjacency list form
    :param v: the starting vertex
    :param trace: an optional argument to display the trace of the algorithm
    :return: a minimal spanning tree created by prims algorithm
    """
    n = len(adjacency_list)
    in_tree = [False] * n
    parent = [None] * n
    distance = [math.inf] * n

    in_tree[v] = True
    distance[v] = 0

    while not all(in_tree):
        for u, w in adjacency_list[v]:
            if not in_tree[u] and w < distance[u]:
                distance[u] = w
                parent[u] = v

        if trace:
            print(f"{v}: {in_tree, distance, parent}")

        v = next_vertex(in_tree, distance)
        in_tree[v] = True

    return parent

def next_vertex(in_tree, distance):
    lowest_v = in_tree.index(False)
    lowest_distance = distance[lowest_v]

    for v, (tree, curr_distance) in enumerate(zip(in_tree, distance)):
        if not tree:
            if curr_distance < lowest_distance:
                lowest_v = v
                lowest_distance = curr_distance

    return lowest_v