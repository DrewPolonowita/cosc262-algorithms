import math


def floyd_warshall_top_down(graph):
    initial_table = initial_distance_table(graph)
    table = [[[initial_table[i][j] if k==0 else None for k in range(len(graph)+1)] for j in range(len(graph))] for i in range(len(graph))]

    def floyd(i, j, k):
        if not table[i][j][k+1] is None:
            return table[i][j][k+1]

        table[i][j][k+1] = min(floyd(i, j, k - 1), floyd(i, k, k - 1) + floyd(k, j, k - 1))
        return table[i][j][k+1]

    return [[floyd(i, j, len(graph) - 1) for j in range(len(graph))] for i in range(len(graph))]



def floyd_warshall_bottom_up(graph):
    table = initial_distance_table(graph)

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

    return table

def initial_distance_table(graph):
    table = [[math.inf if not i == j else 0 for j in range(len(graph))] for i in range(len(graph))]
    for v, edge in enumerate(graph):
        for u, w in edge:
            if not u == v:
                table[v][u] = w
    return table