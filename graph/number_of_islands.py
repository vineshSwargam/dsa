# Number of Islands
# Medium
# Topics
# Company Tags
# Hints

# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

# Example 1:

# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1

# Example 2:

# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4

# Constraints:

# 1 <= grid.length, grid[i].length <= 100
# grid[i][j] is '0' or '1'.



# Topics

# Array Depth-First Search Breadth-First Search Union Find Matrix


# Recommended Time & Space Complexity

# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.



# Hint 1

# An island is a group of 1's in which every 1 is reachable from any other 1 in that group. Can you think of an algorithm that can find the number of groups by visiting a group only once? Maybe there is a recursive way of doing it.



# Hint 2

# We can use the Depth First Search (DFS) algorithm to traverse each group independently. We iterate through each cell of the grid. When we encounter a 1, we perform a DFS starting at that cell and recursively visit every other 1 that is reachable. During this process, we mark the visited 1's as 0 to ensure we don't revisit them, as they belong to the same group. The number of groups corresponds to the number of islands.



# Company Tags

# Amazon
# 23
#  Snap
# 16
#  Google
# 14
#  PayPal
# 9
#  Salesforce
# 9
#  Zoho
# 9
#  Capital One
# 8
#  Samsung
# 8
#  Tesla
# 8
#  Adobe
# 7
#  Anduril
# 7
#  CrowdStrike
# 7
#  Bloomberg
# 6
#  Siemenes
# 6
#  Microsoft
# 5
#  ByteDance
# 4
#  LinkedIn
# 4
#  Uber
# 4
#  Walmart Labs
# 4
#  Waymo
# 4
#  Apple
# 3
#  Goldman Sachs
# 3
#  Oracle
# 3
#  Tiktok
# 3
#  Infosys
# 2
#  Meta
# 2
#  NVIDIA
# 2
#  TCS
# 2
#  Visa
# 2
#  Yandex
# 2
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 78.1%


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:


sol = Solution()
grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ] # Output 1
# grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ] # Output 4



print(sol.num_islands(grid))
