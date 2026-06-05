def fractional_knapsack(capacity, items):
    """
    Takes a capacity and a list of tuples of (item_name, value, weight) and returns the maximum value you can fit in the
    knapsack with a list of tuples (number_of_items, item_name). Items can only be used once
    :param capacity: the maximum capacity of the knapsack
    :param items: a list of tuples of (item_name, value, weight)
    :return:the maximum value you can fit in the knapsack with a list of tuples (number_of_items, item_name)
    """

    sorted_items = sorted(items, key=lambda x: x[1] / x[2])[::-1]
    total_value = 0
    item_list = []
    capacity_remaining = capacity

    for name, value, weight in sorted_items:
        if weight <= capacity_remaining:
            capacity_remaining -= weight
            total_value += value
            item_list.append((1, name))
        else:
            total_value += capacity_remaining / weight * value
            item_list.append((capacity_remaining / weight, name))
            return total_value, item_list

    return total_value, item_list