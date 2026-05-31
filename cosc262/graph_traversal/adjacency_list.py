def adjacency_list(graph_string):
    """
    Takes a graph string defined using COSC262 conventions and returns an adjacency list for the graph
    :param graph_string: a graph string defining the graph
    :return: a graph in the form of an adjacency list
    """
    header, *edges = [s.split() for s in graph_string.strip().splitlines()]
    directed = header[0] == 'D'
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list

def transpose(adjacency_list):
    """
    Takes an adjacency_list and returns the transpose with all edges reversed
    :param adjacency_list: an adjacency list of the graph
    :return: the transposed adjacency_list
    """
    n = len(adjacency_list)
    transposed_graph = [[] for _ in range(n)]

    for u, edges in enumerate(adjacency_list):
        for v, w in edges:
            transposed_graph[v].append((u, w))

    return transposed_graph