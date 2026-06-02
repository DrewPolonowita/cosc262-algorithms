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

    return min(cell_cost(m - 1, i) for i in range(n))


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

    return min(table[m-1])