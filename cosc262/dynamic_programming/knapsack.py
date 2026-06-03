class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"

def knapsack_top_down(items, capacity):
    """
    Takes a set of items and a capacity and returns a list of items that give the maximum capacity without splitting items
    Uses a top-down approach to solve the problem.
    :param items: a set of items
    :param capacity: the capacity of the knapsack
    :return: a set of items which fit in the knapsack and have the maximum total value
    """

    table = [[0 if i == 0 or j == 0 else None for j in range(capacity + 1)] for i in range(len(items)+1)]

    def knapsack(i, capacity):
        if not table[i+1][capacity] is None:
            return table[i+1][capacity]

        if items[i].weight > capacity:
            table[i+1][capacity] = knapsack(i-1, capacity)
        else:
            table[i+1][capacity] = max(knapsack(i - 1, capacity), items[i].value + knapsack(i - 1, capacity - items[i].weight))

        return table[i+1][capacity]

    max_value = knapsack(len(items) - 1, capacity)
    return max_value, traceback_for_solution(table, items)




def knapsack_bottom_up(items, capacity):
    """
    Takes a set of items and a capacity and returns a list of items that give the maximum capacity without splitting items
    Uses a bottom-up approach to solve the problem.
    :param items: a set of items
    :param capacity: the capacity of the knapsack
    :return: a set of items which fit in the knapsack and have the maximum total value
    """

    table = [[0 if i == 0 else -1 for j in range(capacity + 1)] for i in range(len(items)+1)]

    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            if items[i-1].weight > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max([
                    table[i - 1][j], items[i-1].value + table[i - 1][j - items[i-1].weight]
                ])
    return table[-1][-1], traceback_for_solution(table, items)


def traceback_for_solution(table, items):

    i = len(table) - 1
    j = len(table[0]) - 1

    current_items = []

    while i > 0 and j > 0:
        if table[i][j] == table[i-1][j]:
            i -= 1
        else:
            j -= items[i-1].weight
            current_items.append(items[i-1])
            i -= 1

    return current_items
