import math
from .prims import next_vertex

def dijkstra(adjacency_list, v, trace=False):
    """
        Returns tree created from a dijkstra's traversal which gives a minimal distance tree on the graph
        :param adjacency_list: a graph in adjacency list form
        :param v: the starting vertex
        :param trace: an optional argument to display the trace of the algorithm
        :return: a minimal distance tree created by dijkstra's algorithm
        """
    n = len(adjacency_list)
    in_tree = [False] * n
    parent = [None] * n
    distance = [math.inf] * n

    in_tree[v] = True
    distance[v] = 0

    while not all(in_tree):
        for u, w in adjacency_list[v]:
            if not in_tree[u] and distance[v] + w < distance[u]:
                distance[u] = distance[v] + w
                parent[u] = v

        if trace:
            print(f"{v}: {in_tree, distance, parent}")

        v = next_vertex(in_tree, distance)
        in_tree[v] = True

    return parent