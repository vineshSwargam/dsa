# Islands and Treasure
# Medium
# Topics
# Company Tags
# Hints

# You are given a
# 𝑚
# ×
# 𝑛
# m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]

# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is one of {-1, 0, 2147483647}



# Topics

# Array Breadth-First Search Matrix


# Recommended Time & Space Complexity

# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the given grid.



# Hint 1

# A brute force solution would be to iterate on each land cell and run a BFS from that cells to find the nearest treasure chest. This would be an O((m * n)^2) solution. Can you think of a better way? Sometimes it is not optimal to go from source to destination.



# Hint 2

# We can see that instead of going from every cell to find the nearest treasure chest, we can do it in reverse. We can just do a BFS from all the treasure chests in grid and just explore all possible paths from those chests. Why? Because in this approach, the treasure chests self mark the cells level by level and the level number will be the distance from that cell to a treasure chest. We don't revisit a cell. This approach is called Multi-Source BFS. How would you implement it?



# Hint 3

# We insert all the cells (row, col) that represent the treasure chests into the queue. Then, we process the cells level by level, handling all the current cells in the queue at once. For each cell, we mark it as visited and store the current level value as the distance at that cell. We then try to add the neighboring cells (adjacent cells) to the queue, but only if they have not been visited and are land cells.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 65.2%


from typing import List
import copy
import traceback


class Solution:
    def islands_and_treasure(self, grid: List[List[int]]) -> None:
        pass


sol = Solution()

# run from the repo root: python3 -m graph.islands_and_treasure
# (grid, expected) - your solution changes the grid in place (nothing is returned), and the test
# compares the changed grid to expected. Each test gets its own copy of the grid.
INF = 2147483647

def g(*rows):
    """Write a small grid as strings: W = water (-1), T = treasure (0), . = land (INF), or a digit for an answer."""
    m = {"W": -1, "T": 0, ".": INF}
    return [[m[ch] if ch in m else int(ch) for ch in r] for r in rows]

ex1_in = [[INF,-1,0,INF],
          [INF,INF,INF,-1],
          [INF,-1,INF,-1],
          [0,-1,INF,INF]]
ex1_out = [[3,-1,0,1],
           [2,2,1,-1],
           [1,-1,2,-1],
           [0,-1,3,4]]

# 100x100, open land, one treasure in the top-left corner: every cell is r + c away
corner_in = [[INF] * 100 for _ in range(100)]; corner_in[0][0] = 0
corner_out = [[r + c for c in range(100)] for r in range(100)]
# 100x100, open land, treasures in two opposite corners: the nearer one wins
two_in = [[INF] * 100 for _ in range(100)]; two_in[0][0] = 0; two_in[99][99] = 0
two_out = [[min(r + c, 198 - r - c) for c in range(100)] for r in range(100)]
# 100x100, all water except one treasure: nothing to fill
water_in = [[-1] * 100 for _ in range(100)]; water_in[50][50] = 0
water_out = copy.deepcopy(water_in)
# 100x100, all land and no treasure: everything stays INF
no_treasure = [[INF] * 100 for _ in range(100)]

# 100x100 winding path: land rows joined at alternating ends, water everywhere else,
# treasure at the start. Each cell's answer is how far along the path it is (up to 5049).
def snake():
    grid = [[-1] * 100 for _ in range(100)]
    out = [[-1] * 100 for _ in range(100)]
    step = 0
    for r in range(100):
        if r % 2 == 0:
            cs = range(100) if r % 4 == 0 else range(99, -1, -1)
        else:
            cs = [99] if r % 4 == 1 else [0]
        for c in cs:
            grid[r][c] = INF
            out[r][c] = step
            step += 1
    grid[0][0] = 0
    return grid, out
snake_in, snake_out = snake()

tests = [
    (ex1_in, ex1_out),                                          # example 1
    ([[0,-1],[INF,INF]], [[0,-1],[1,2]]),                       # example 2
    ([[INF]], [[INF]]),                                         # single land cell, no treasure: stays INF
    ([[0]], [[0]]),                                             # single treasure
    ([[-1]], [[-1]]),                                           # single water cell
    (g("...", "..."), g("...", "...")),                         # no treasure anywhere: nothing changes
    (g("T..."), g("0123")),                                     # one row
    (g("T", ".", ".", "T"), g("0", "1", "1", "0")),             # one column, two treasures: nearest one wins
    (g("T...T"), g("01210")),                                   # middle cell is 2 from both
    (g("TW.", "WW.", "..."), g("0W.", "WW.", "...")),           # land walled off from the treasure stays INF
    (g("T.W.", "..W.", "WWW."), g("01W.", "12W.", "WWW.")),     # one reachable area, one walled-off area
    (g("T.T", "...", "T.T"), g("010", "121", "010")),           # four treasures, the centre is 2 from all of them
    (g("TTT", "TTT"), g("TTT", "TTT")),                         # all treasure, nothing to fill
    (g("T.....", "WWWWW.", "......"),                           # the path must go around the wall, so the
     [[0,1,2,3,4,5],[-1,-1,-1,-1,-1,6],[12,11,10,9,8,7]]),      # bottom-left cell is 12 away, not 2
    (g(".T.", "...", ".T."), g("101", "212", "101")),           # two treasures in one column
    (g("..W..", "T.W.T", "..W.."), g("12W21", "01W10", "12W21")),   # a wall down the middle: each side uses its own treasure
    (corner_in, corner_out),                                    # max size, distances up to 198
    (two_in, two_out),                                          # max size, two treasures share the grid
    (water_in, water_out),                                      # max size, no land
    (no_treasure, [[INF] * 100 for _ in range(100)]),           # max size, no treasure: all stay INF
    (snake_in, snake_out),                                      # max size, one long winding path, distances up to 5049
]

def show(grid):
    if len(grid) * len(grid[0]) > 30:
        return f"[{len(grid)}x{len(grid[0])} grid]"
    cell = lambda v: "INF" if v == INF else str(v)
    return "[" + ",".join("[" + ",".join(cell(v) for v in row) + "]" for row in grid) + "]"

def first_diff(got, expected):
    for r in range(len(expected)):
        for c in range(len(expected[0])):
            if got[r][c] != expected[r][c]:
                return f"  first wrong cell ({r},{c}): got {got[r][c]}, expected {expected[r][c]}"
    return ""

passed = 0
for grid, expected in tests:
    work = copy.deepcopy(grid)
    try:
        sol.islands_and_treasure(work)
        ok = work == expected
        why = "" if ok else first_diff(work, expected)
        got = show(work)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        ok, why, got = False, "", f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})'
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {show(grid)} -> {got}" + ("" if ok else f"  expected {show(expected)}{why}"))

print(f"{passed}/{len(tests)} passed")
