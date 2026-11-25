# Max Area of Island
# Medium
# Topics
# Company Tags
# Hints

# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

# Example 1:

# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]

# Output: 6

# Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

# Constraints:

# 1 <= grid.length, grid[i].length <= 50



# Topics

# Array Depth-First Search Breadth-First Search Union Find Matrix


# Recommended Time & Space Complexity

# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.



# Hint 1

# An island is a group of 1's in which every 1 is reachable from any other 1 in that group. Can you think of an algorithm that can find the number of groups by visiting a group only once? Maybe there is a recursive way of doing it.



# Hint 2

# We can use the Depth First Search (DFS) algorithm to traverse each group by starting at a cell with 1 and recursively visiting all the cells that are reachable from that cell and are also 1. Can you think about how to find the area of that island? How would you implement this?



# Hint 3

# We traverse the grid, and when we encounter a 1, we initialize a variable area. We then start a DFS from that cell to visit all connected 1's recursively, marking them as 0 to indicate they are visited. At each recursion step, we increment area. After completing the DFS, we update maxArea, which tracks the maximum area of an island in the grid, if maxArea < area. Finally, after traversing the grid, we return maxArea.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 68.5%


from typing import List
import copy
import traceback


class Solution:
  def using_iter(self, grid):
    res = 0
    rows = len(grid)
    cols = len(grid[0])
    explored = set()


    def iter(i, j):
      st = [(i, j)] # stack for remembering the next directions
      area = 1

      while st:
        (i, j) = st.pop()
    
        if i+1 < rows and grid[i+1][j] == 1 and (i+1, j) not in explored:
          area += 1
          explored.add((i+1, j))
          st.append((i+1, j))
        if i-1 >= 0 and grid[i-1][j] == 1 and (i-1, j) not in explored:
          area += 1
          explored.add((i-1, j))
          st.append((i-1, j))
        if j+1 < cols and grid[i][j+1] == 1 and (i, j+1) not in explored:
          area += 1
          explored.add((i, j+1))
          st.append((i, j+1))
        if j-1 >= 0 and grid[i][j-1] == 1 and (i, j-1) not in explored:
          area += 1
          explored.add((i, j-1))
          st.append((i, j-1))

      return area
    
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 1 and (r, c) not in explored:
          explored.add((r, c))
          res = max(iter(r, c), res)

    print(res)
    return res


  def max_area_of_island(self, grid: List[List[int]]) -> int:
      return self.using_iter(grid)


sol = Solution()

# run from the repo root: python3 -m graph.max_area_of_island
# (grid, expected) - each test gets its own copy of the grid, so changing it inside your solution is fine
# note: cells are the numbers 0 and 1 here, not the strings "0" and "1" like in Number of Islands
def g(*rows):
    """Write a grid as strings: g("110", "011") is [[1,1,0],[0,1,1]]."""
    return [[int(ch) for ch in r] for r in rows]

ex1 = g("01101",
        "10101",
        "01101",
        "01001")
all_land = [[1] * 50 for _ in range(50)]                                      # 50x50, one island of 2500 cells
all_water = [[0] * 50 for _ in range(50)]                                     # 50x50, no land
checker = [[1 if (r + c) % 2 == 0 else 0 for c in range(50)] for r in range(50)]   # 1s only touch diagonally
# one long winding island: full land rows joined at alternating ends
snake = [[1] * 50 if r % 2 == 0 else ([0] * 49 + [1] if r % 4 == 1 else [1] + [0] * 49) for r in range(50)]

tests = [
    (ex1, 6),                                            # example 1
    # (g("0"), 0),                                         # single water cell, no island
    # (g("1"), 1),                                         # single land cell
    # (g("000", "000"), 0),                                # no land at all
    # (g("1111", "1111", "1111"), 12),                     # all land, the whole grid is one island
    # (g("10", "01"), 1),                                  # diagonal cells are NOT connected
    # (g("11101"), 3),                                     # one row
    # (g("1", "1", "0", "1"), 2),                          # one column
    # (g("10111"), 3),                                     # the bigger island comes second
    # (g("11011"), 2),                                     # two islands of the same size
    # (g("111", "101", "111"), 8),                         # a ring, with water inside
    # (g("11111", "10001", "10101", "10001", "11111"), 16),   # ring of 16 with a 1-cell island inside the lake
    # (g("110011", "110011", "001100", "000000"), 4),      # three 2x2 blocks, only touching at corners
    # (g("1100", "1100", "0110", "0011"), 8),              # blocks joined through edge contact, one island
    # (g("10000", "00000", "00011", "00011"), 4),          # the biggest island is in the bottom-right corner
    # (g("1111", "0001", "1111", "1000", "1111"), 14),     # S-shape winding back and forth
    # (g("10101", "01010", "10101"), 1),                   # small checkerboard, every 1 alone
    # (all_water, 0),                                      # max size, no land
    # (checker, 1),                                        # max size, 1250 islands of one cell each
    # (all_land, 2500),                                    # max size, 2500 connected cells: recursive DFS can hit
    #                                                      # Python's recursion limit (1000) here
    # (snake, 1275),                                       # max size, one long winding path: same recursion trap
]

def show(grid):
    if len(grid) * len(grid[0]) > 30:
        return f"[{len(grid)}x{len(grid[0])} grid]"
    return "[" + ",".join("".join(map(str, row)) for row in grid) + "]"

passed = 0
for grid, expected in tests:
    try:
        got = sol.max_area_of_island(copy.deepcopy(grid))
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})'
    ok = got == expected
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {show(grid)} -> {got}" + ("" if ok else f"  expected {expected}"))

print(f"{passed}/{len(tests)} passed")
