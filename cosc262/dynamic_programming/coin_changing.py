def coins_reqd_top_down(value, coinage):
    """
    Returns the minimum number of coins required to make up a value, from some coinage and
    the amount of each coin required to make up a value. Using a recursive top down approach
    :param value: the amount of coin to make up
    :param coinage: the denominations of coins
    :return: the minimum number of coins required to make up a value, from some coinage
    """
    coinage = sorted(coinage)
    table = [None] * (value + 1)
    table[0] = 0
    for c in coinage:
        if c <= value:
            table[c] = 1

    def coins_reqd(value, coinage):
        if not table[value] is None:
            return table[value]

        possible_values = [
            coins_reqd(value - c, coinage) for c in coinage
            if c <= value
        ]

        table[value] = 1 + min(possible_values)

        return table[value]

    coins = coins_reqd(value, coinage)
    return coins, traceback_for_coinage(table, coinage)


def coins_reqd_bottom_up(value, coinage):
    """
        Returns the minimum number of coins required to make up a value, from some coinage and
        the amount of each coin required to make up a value. Using a bottom up approach
        :param value: the amount of coin to make up
        :param coinage: the denominations of coins
        :return: the minimum number of coins required to make up a value, from some coinage
        """
    coinage = sorted(coinage)
    table = [None] * (value + 1)
    table[0] = 0
    for c in coinage:
        if c <= value:
            table[c] = 1

    for i in range(1, value + 1):
        possible_values = [
            table[i - c] for c in coinage
            if c <= i
        ]

        table[i] = 1 + min(possible_values)

    return table[-1], traceback_for_coinage(table, coinage)


def traceback_for_coinage(table, coinage):
    coins = []
    current_value = len(table) - 1
    while len(coins) < table[-1]:
        possible_values = [
            c for c in coinage
            if c <= current_value and table[current_value-c]+1==table[current_value]
        ]
        c = possible_values[0]
        coins.append(c)
        current_value -= c
    sum_coins = []
    for c in coinage[::-1]:
        count = coins.count(c)
        if count > 0:
            sum_coins.append((c, count))


    return sum_coins