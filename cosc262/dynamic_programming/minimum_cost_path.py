def grid_cost_top_down(grid):
    """
    Returns the cheapest cost from row 1 to row n (1-origin) in the given grid of integer weights.
    :param grid: the grid
    :return: the cheapest cost from row 1 to row n (1-origin) in the given grid of integer weights.
    """
    m = len(grid)
    n = len(grid[0])

    table = [[grid[i][j] if i == 0 else None for j in range(n)] for i in range(m)]

    def cell_cost(row, col):
        if not table[row][col] is None:
            return table[row][col]

        possible_costs = [cell_cost(row - 1, col)]
        if col - 1 >= 0:
            possible_costs += [cell_cost(row - 1, col-1)]
        if col + 1 < n:
            possible_costs += [cell_cost(row - 1, col+1)]

        table[row][col] = grid[row][col] + min(possible_costs)

        return table[row][col]

    return min(cell_cost(m - 1, i) for i in range(n)), traceback_for_solution(table)


def grid_cost_bottom_up(grid):
    """
    Returns the cheapest cost from row 1 to row n (1-origin) in the given grid of integer weights.
    :param grid: the grid
    :return: the cheapest cost from row 1 to row n (1-origin) in the given grid of integer weights.
    """
    m = len(grid)
    n = len(grid[0])

    table = [[grid[i][j] if i == 0 else None for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(n):
            possible_costs = [table[i - 1][j]]

            if j - 1 >= 0:
                possible_costs += [table[i - 1][j - 1]]
            if j + 1 < n:
                possible_costs += [table[i - 1][j + 1]]

            table[i][j] = grid[i][j] + min(possible_costs)

    return min(table[m-1]), traceback_for_solution(table)


def traceback_for_solution(table):
    m = len(table)
    n = len(table[0])

    path = [-1 for _ in range(m)]
    path[-1] = table[-1].index(min(table[-1]))
    for i in range(m - 2, -1, -1):
        prev_node = path[i + 1]

        min_cost = table[i][prev_node]
        min_index = prev_node

        if prev_node - 1 >= 0:
            if table[i][prev_node - 1] < min_cost:
                min_cost = table[i][prev_node - 1]
                min_index = prev_node - 1

        if prev_node + 1 < n:
            if table[i][prev_node + 1] < min_cost:
                min_cost = table[i][prev_node + 1]
                min_index = prev_node + 1

        path[i] = min_index
    return path