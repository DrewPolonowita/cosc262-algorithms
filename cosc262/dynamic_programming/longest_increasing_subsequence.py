


def longest_increasing_subsequence_top_down(s):
    """
    Returns the longest increasing subsequence of s using a top-down approach
    :param s: a sequence of integers
    :return: the longest increasing subsequence of s using a top-down approach
    """

    L = [1 if i == 0 else None for i in range(len(s))]
    K = [-1 for _ in range(len(s))]

    def lis(s, i):
        if not L[i] is None:
            return L[i]

        max_value = 0
        index = -1

        for j in range(0, i):
            if s[j] < s[i]:
                value = lis(s, j)
                if value > max_value:
                    max_value = value
                    index = j

        L[i] = 1 + max_value
        K[i] = index

        return L[i]

    max_length = max([lis(s, i) for i in range(len(s))])
    
    return max_length, traceback_to_get_solution(s, K, L.index(max_length))


def longest_increasing_subsequence_bottom_up(s):
    """
    Returns the longest increasing subsequence of s using a bottom-up approach
    :param s: a sequence of integers
    :return: the longest increasing subsequence of s using a bottom-up approach
    """
    L = [1 if i == 0 else None for i in range(len(s))]
    K = [-1 for _ in range(len(s))]

    for i in range(1, len(s)):
        max_value = 0
        index = -1

        for j in range(0, i):
            if s[j] < s[i]:
                value = L[j]
                if value > max_value:
                    max_value = value
                    index = j

        L[i] = 1 + max_value
        K[i] = index

    max_value = max(L)

    return max_value, traceback_to_get_solution(s, K, L.index(max_value))

def traceback_to_get_solution(s, K, start):
    i = start
    path = []

    while i > 0:
        path.append(i)
        i = K[i]

    return [s[i] for i in path[::-1]]