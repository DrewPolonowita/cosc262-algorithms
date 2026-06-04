def edit_distance_top_down(s1, s2):
    """
    Returns the minimum edit distance between enumerable objects of strings s1 and s2
    Uses a top-down approach
    :param s1: an enumerable object of strings
    :param s2: an enumerable object of strings
    :return: the minimum edit distance between s1 and s2 and the required steps
    """
    table = [
        [
            i if j == 0 else j if i== 0 else None
            for j in range(len(s2) + 1)
        ]
        for i in range(len(s1) + 1)
    ]

    def edit_distance(i, j):
        if not table[i][j] is None:
            return table[i][j]

        if s1[i-1] == s2[j-1]:
            table[i][j] = edit_distance(i-1, j-1)
            return table[i][j]
        else:
            table[i][j] = 1 + min([
                edit_distance(i-1, j), edit_distance(i, j-1), edit_distance(i-1, j-1)
            ])

            return table[i][j]

    s = edit_distance(len(s1), len(s2))

    return s, traceback_for_solution(table, s1, s2)



def edit_distance_bottom_up(s1, s2):
    """
    Returns the minimum edit distance between enumerable objects of strings s1 and s2
    Uses a bottom-up approach
    :param s1: an enumerable object of strings
    :param s2: an enumerable object of strings
    :return: the minimum edit distance between s1 and s2 and the required steps
    """
    table = [
        [
            i if j == 0 else j if i == 0 else None
            for j in range(len(s2) + 1)
        ]
        for i in range(len(s1) + 1)
    ]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min([
                    table[i-1][j], table[i][j-1], table[i-1][j-1]
                ])

    return table[-1][-1], traceback_for_solution(table, s1, s2)


def traceback_for_solution(table, s1, s2):
    i = len(s1)
    j = len(s2)

    order = []

    while i > 0 and j > 0:
        if table[i][j] == table[i-1][j-1] and s1[i-1] == s2[j-1]:
            order.append(('C', s1[i-1], s2[j-1]))
            i -= 1
            j -= 1
        elif table[i][j] == 1 + table[i-1][j-1]:
            order.append(('S', s1[i-1], s2[j-1]))
            i -= 1
            j -= 1
        elif table[i][j] == 1 + table[i-1][j]:
            order.append(('D', s1[i-1], ''))
            i -= 1
        else:
            order.append(('I', '', s2[j-1]))
            j -= 1

    return order[::-1]