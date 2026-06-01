def get_possible_queen_permutations_on_chess_board(num_queens, starting_queens=None):
    if starting_queens is None:
        starting_queens = []

    solutions = []

    def dfs_backtrack(candidate, input, output):
        if should_prune(candidate):
            return

        if is_solution(candidate, input):
            add_to_output(candidate, output)
        else:
            for child in children(candidate):
                dfs_backtrack(child, input, output)

    def should_prune(candidate):
        for x, y in candidate:
            for i, j in candidate:
                if not (x,y) == (i,j): # Not an identical queen

                    if x == i or y == j: # Same row/col
                        return True
                    if abs(x - i) == abs(y - j): # Same diagonal
                        return True

        return False

    def is_solution(candidate, input):
        if len(candidate) == input:
            return True
        return False

    def children(candidate):
        next_row = len(candidate) + 1

        return [
            candidate + [(next_row, col)]
            for col in range(1, 9)
        ]

    def add_to_output(candidate, output):
        output.append(candidate)

    dfs_backtrack(starting_queens, num_queens, solutions)
    return solutions