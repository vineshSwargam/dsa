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


from typing import List
import copy
import traceback


class Solution:
  def using_recur_bt(self, grid):
    res = 0
    explored = set()
    rows = len(grid)
    cols = len(grid[0])

    def explore(i, j):
      if min(i, j) < 0 or j >= cols or i >= rows or grid[i][j] == '0':
        return

      explored.add((i, j))

      if (i+1, j) not in explored:
        explore(i+1, j)
      if (i-1, j) not in explored:
        explore(i-1, j)
      if (i, j+1) not in explored:
        explore(i, j+1)
      if (i, j-1) not in explored:
        explore(i, j-1)
      
      return
    
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == '1' and (r, c) not in explored:
          res += 1
          explore(r, c)

    return res
  
   
  def num_islands(self, grid: List[List[str]]) -> int:
      return self.using_iter_bt(grid)
      # return self.using_recur_bt(grid)


sol = Solution()

# run from the repo root: python3 -m graph.number_of_islands
# (grid, expected) - each test gets its own copy of the grid, so changing it inside your solution is fine
def g(*rows):
    """Write a grid as strings: g("110", "011") is [["1","1","0"],["0","1","1"]]."""
    return [list(r) for r in rows]

ex1 = g("01110",
        "01010",
        "11000",
        "00000")
ex2 = g("11001",
        "11001",
        "00100",
        "00011")
all_land = [["1"] * 100 for _ in range(100)]                                  # 100x100, one huge island
all_water = [["0"] * 100 for _ in range(100)]                                 # 100x100, no land
checker = [["1" if (r + c) % 2 == 0 else "0" for c in range(100)] for r in range(100)]   # 1s only touch diagonally
stripes = [["1" if r % 2 == 0 else "0"] * 100 for r in range(100)]           # every other row is land
# one long winding island: full land rows joined at alternating ends, about 5000 cells in a single path
snake = [["1"] * 100 if r % 2 == 0 else (["0"] * 99 + ["1"] if r % 4 == 1 else ["1"] + ["0"] * 99) for r in range(100)]

tests = [
    (ex1, 1),                                    # example 1: one island with a bend in it
    (ex2, 4),                                    # example 2
    (g("1"), 1),                                 # single land cell
    (g("0"), 0),                                 # single water cell
    (g("000", "000"), 0),                        # no land at all
    (g("111", "111"), 1),                        # all land
    (g("101"), 2),                               # one row, split by water
    (g("1", "0", "1", "1"), 2),                  # one column
    (g("10", "01"), 2),                          # diagonal cells are NOT connected
    (g("010", "101", "010"), 4),                 # four cells around a water centre, none touching
    (g("111", "101", "111"), 1),                 # a ring is one island, even with water inside
    (g("11111", "10001", "10101", "10001", "11111"), 2),   # ring with a separate island inside the lake
    (g("1101", "1001", "0011"), 2),              # connection goes around a corner
    (g("1111", "0001", "1111", "1000", "1111"), 1),        # S-shape winding back and forth
    (g("10101", "01010", "10101"), 8),           # small checkerboard, every 1 alone
    (all_water, 0),                              # max size, nothing to count
    (stripes, 50),                               # max size, 50 separate rows of land
    (checker, 5000),                             # max size, 5000 single-cell islands
    (all_land, 1),                               # max size, 10,000 connected cells: recursive DFS can hit
                                                 # Python's recursion limit (1000) here
    (snake, 1),                                  # max size, one long winding path: same recursion trap
]

def show(grid):
    if len(grid) * len(grid[0]) > 30:
        return f"[{len(grid)}x{len(grid[0])} grid]"
    return "[" + ",".join("".join(row) for row in grid) + "]"

passed = 0
for grid, expected in tests:
    try:
        got = sol.num_islands(copy.deepcopy(grid))
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})'
    ok = got == expected
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {show(grid)} -> {got}" + ("" if ok else f"  expected {expected}"))

print(f"{passed}/{len(tests)} passed")
