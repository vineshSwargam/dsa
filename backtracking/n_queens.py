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


class Solution:
    def solve_n_queens(self, n: int) -> List[List[str]]:


sol = Solution()
n = 4 # Output [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# n = 1 # Output [["Q"]]



print(sol.solve_n_queens(n))
