# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Example 2:

# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


# Topics

  

# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n^2) time and O(n^2) space, where n is the number of rows in the square grid.


# Hint 1
# Which data structure would you prefer to use for checking duplicates?


# Hint 2
# You can use a hash set for every row and column to check duplicates. But how can you efficiently check for the squares?


# Hint 3
# We can find the index of each square by the equation (row / 3) * 3 + (col / 3). Then we use hash set for O(1) lookups while inserting the number into its row, column and square it belongs to. We use separate hash maps for rows, columns, and squares.

from collections import defaultdict


class Solution:
    def is_valid_sudoku(self, board) -> bool:
        row_set = set()
        col_set = defaultdict(set)
        grid_set_one = set()
        grid_set_two = set()
        grid_set_three = set()

        for i in range(9):
            if i == 3 or i == 6:
                grid_set_one.clear()
                grid_set_two.clear()
                grid_set_three.clear()

            for j in range(9):
                row_val = board[i][j]

                if row_val == '.':
                    continue

                if row_val in row_set:
                    print(f'Found duplicate in row/col set - {i},{j} - val - {row_val}')
                    print('row_set -', row_set)
                    return False

                print(f'Adding row val {i}, {j} to row_set - {row_val}')
                row_set.add(row_val)

                if j < 3:
                    if row_val in grid_set_one:
                        print(f'Found duplicate in grid_set_one - {i},{j} - val - {row_val}')
                        return False

                    print(f'Adding grid val {i}, {j} to grid_set_one - {row_val}')
                    grid_set_one.add(row_val)

                elif j >= 3 and j < 6:
                    if row_val in grid_set_two:
                        print(f'Found duplicate in grid_set_two - {i},{j} - val - {row_val}')
                        return False

                    print(f'Adding grid val {i}, {j} to grid_set_two - {row_val}')
                    grid_set_two.add(row_val)
                
                elif j >= 6 and j < 9:
                    if row_val in grid_set_three:
                        print(f'Found duplicate in grid_set_three - {i},{j} - val - {row_val}')
                        return False

                    print(f'Adding grid val {i}, {j} to grid_set_three - {row_val}')
                    grid_set_three.add(row_val)

                # print('======== Entering Col checks =========', row_val)
                if row_val in col_set[j]:
                    print(f'Found duplicate in row/col set - {i},{j} - val - {row_val}')
                    print(f'col_set-{j} -', col_set[j])
                    return False

                print(f'Adding col val {i}, {j} to col_set - {row_val}')
                col_set[j].add(row_val)
                print(f'col_set[{j}] -', col_set[j])
            
            row_set.clear()

        return True      


sol = Solution()
# true
b1 = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]
# false
b2 = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]
# false
b3 = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]
# false
b4 = [
    [".",".",".","9",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".","9",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]
print(sol.is_valid_sudoku(b4))
        