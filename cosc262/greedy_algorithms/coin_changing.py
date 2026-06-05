def coin_changing_greedy(amount, coinage):
    """
    A greedy solution to the coin changing problem. Returns the optimal coinage for a given value if the coinage
    is a canonical coinage system
    :param amount: the amount of money to get the coinage of
    :param coinage: the coin denominations
    :return: the optimal coinage if the coin system is canonical, none if no solution is found
    """

    sorted_coinage = sorted(coinage)[::-1]
    total_amount_remaining = amount
    coins = []

    for coin in sorted_coinage:
        if not total_amount_remaining // coin == 0:
            coins.append((total_amount_remaining // coin, coin))
        total_amount_remaining = total_amount_remaining % coin

    if not total_amount_remaining == 0:
        return None

    return coins