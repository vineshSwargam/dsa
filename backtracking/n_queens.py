# N-Queens
# Hard
# Topics
# Company Tags
# Hints

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

# A queen in a chessboard can attack horizontally, vertically, and diagonally.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

# You may return the answer in any order.

# Example 1:

# Input: n = 4

# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

# Explanation: There are two different solutions to the 4-queens puzzle.

# Example 2:

# Input: n = 1

# Output: [["Q"]]

# Constraints:

# 1 <= n <= 8



# Topics

# Array Backtracking


# Recommended Time & Space Complexity

# You should aim for a solution with O(n!) time and O(n^2) space, where n is the size of the given square board.



# Hint 1

# A queen can move in 8 directions, and no two queens can be in the same row or column. This means we can place one queen per row or column. We iterate column-wise and try to place a queen in each column while ensuring no other queen exists in the same row, left diagonal, or left bottom diagonal. Can you think of a recursive algorithm to find all possible combinations?



# Hint 2

# We can use backtracking to traverse through the columns with index c while maintaining a board that represents the current state in the recursive path. We reach the base condition when c == n and we add a copy of the board to the result. How would you implement this?



# Hint 3

# We initialize an empty board and recursively go through each column. For each column, we check each cell to see if we can place a queen there. We use a function to check if the cell is suitable by iterating along the left directions and verifying if the same row, left diagonal, or left bottom diagonal are free. If it is possible, we place the queen on the board, move along the recursive path, and then backtrack by removing the queen to continue to the next cell in the column.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 79.9%


from typing import List
import traceback


class Solution:
    def using_iter_bt(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]
        cols = [-1]*n

        def is_safe(row, col):
            for r in range(row):
                for c in range(n):
                    if board[r][c] == 'Q':
                        if col == c:
                            return False
                        if abs(row-r) == abs(col-c):
                            return False
            return True

        row = 0
        while row >= 0:
            if row == n:
                res.append([''.join(row) for row in board])
                row -= 1
                continue

            cur_ind = cols[row]
            if cur_ind > -1:
                board[row][cur_ind] = '.'

            cur_ind += 1
            while cur_ind < n and not is_safe(row, cur_ind):
                cur_ind += 1
            
            # couldn't find valid index
            if cur_ind == n:
                cols[row] = -1
                row -= 1
                continue

            # found safe index
            board[row][cur_ind] = 'Q'
            cols[row] = cur_ind
            row += 1
        
        return res

    def solve_n_queens(self, n: int) -> List[List[str]]:
        return self.using_iter_bt(n)


sol = Solution()

# run from the repo root: python3 -m backtracking.n_queens
# (n, expected) - the boards can come in any order
# expected is either the full answer, or (for the bigger boards) just how many solutions there should be.
# For a count, every board you return is also checked: n rows of n characters, only 'Q' and '.',
# one queen in every row and every column, no two queens on a diagonal, and no board appears twice.
tests = [
    (1, [["Q"]]),                                                       # example 2, one square
    (2, []),                                                            # no solution: the 2 queens always attack
    (3, []),                                                            # no solution either
    (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]), # example 1
    (5, 10),
    (6, 4),                                                             # fewer solutions than n = 5
    (7, 40),
    (8, 92),                                                            # max n, the classic 8 queens
]

def problem(n, board):
    """Why this board is not a valid answer, or None if it is fine."""
    if not isinstance(board, list) or len(board) != n:
        return f"{board} does not have {n} rows"
    cols, diag, anti = set(), set(), set()
    for r, row in enumerate(board):
        if not isinstance(row, str) or len(row) != n or set(row) - {"Q", "."}:
            return f"row {row!r} must be a string of {n} characters, only 'Q' and '.'"
        if row.count("Q") != 1:
            return f"row {row!r} must have exactly one queen"
        c = row.index("Q")
        if c in cols or r - c in diag or r + c in anti:
            return f"{board}: the queen in row {r} is attacked"
        cols.add(c); diag.add(r - c); anti.add(r + c)
    return None

def check(n, got, expected):
    if not isinstance(got, list):
        return False, ""
    if isinstance(expected, list):
        return sorted(map(list, got)) == sorted(expected), ""
    for board in got:
        why = problem(n, board)
        if why:
            return False, "  " + why
    if len(set(map(tuple, got))) != len(got):
        return False, "  the same board appears more than once"
    return len(got) == expected, ""

passed = 0
for n, expected in tests:
    try:
        got = sol.solve_n_queens(n)
        ok, why = check(n, got, expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} boards" if isinstance(got, list) and len(got) > 2 else got
    print(f"{'PASS' if ok else 'FAIL'}  n={n} -> {shown}" + ("" if ok else f"  expected {expected}{why}"))

print(f"{passed}/{len(tests)} passed")
