# Surrounded Regions
# Medium
# Topics
# Company Tags
# Hints

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.

# Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares or rectangles.

# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.

# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

# Example 1:

# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","X","O","X"],
#   ["X","O","X","X"]
# ]

# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","O","X","X"]
# ]

# Explanation: The bottom 'O' region is not captured because it touches the edge of the board, so it cannot be surrounded.




# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

# Constraints:

# 1 <= board.length, board[i].length <= 200
# board[i][j] is 'X' or 'O'.



# Topics

# Array Depth-First Search Breadth-First Search Union Find Matrix


# Recommended Time & Space Complexity

# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the matrix.



# Hint 1

# We observe that we need to capture the regions that are not connected to the O's on the border of the matrix. This means there should be no path connecting the O's on the border to any O's in the region. Can you think of a way to check the region connected to these border O's?



# Hint 2

# We can use the Depth First Search (DFS) algorithm. Instead of checking the region connected to the border O's, we can reverse the approach and mark the regions that are reachable from the border O's. How would you implement this?



# Hint 3

# We run the DFS from every 'O' on the border of the matrix, visiting the neighboring cells that are equal to 'O' recursively and marking them as '#' to avoid revisiting. After completing all the DFS calls, we traverse the matrix again and capture the cells where matrix[i][j] == 'O', and unmark the cells back to 'O' where matrix[i][j] == '#'.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 54.6%


class Solution:
    def solve(self, board: List[List[str]]) -> None:


sol = Solution()
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
] # Output [
# board = [["X"]] # Output [["X"]]



print(sol.solve(board))
