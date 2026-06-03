def longest_common_subsequence_top_down(a, b):
    """
    Returns the longest common subsequence of two strings using top-down approach
    :param a: a string a
    :param b: a string b
    :return: the longest common subsequence of two strings a and b
    """

    if a == "" or b == "":
        return ""

    table = [[0 if i == 0 or j == 0 else None for i in range(len(b) + 1)] for j in range(len(a) + 1)]

    def lcs(i, j):
        if not table[i][j] is None:
            return table[i][j]

        if a[i-1] == b[j-1]:
            table[i][j] = 1 + lcs(i-1, j-1)
        else:
            table[i][j] = max(lcs(i-1, j), lcs(i, j-1))

        return table[i][j]

    lcs(len(a), len(b))

    return traceback_to_get_solution(table, a, b)

def longest_common_subsequence_bottom_up(a, b):
    """
    Returns the longest common subsequence of two strings using bottom-up approach
    :param a: a string a
    :param b: a string b
    :return: the longest common subsequence of two strings a and b
    """

    if a == "" or b == "":
        return ""

    table = [[0 if i == 0 or j == 0 else None for i in range(len(b) + 1)] for j in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return traceback_to_get_solution(table, a, b)

def traceback_to_get_solution(table, a, b):
    lcs = ""
    i = len(a)
    j = len(b)
    while i > 0 and j > 0:
        if a[i-1] == b[j-1] and table[i][j] == table[i-1][j-1] + 1:
            lcs += a[i - 1]
            i -= 1
            j -= 1
        else:
            if table[i-1][j] >= table[i][j-1]:
                i-=1
            else:
                j-=1

    return lcs[::-1]
