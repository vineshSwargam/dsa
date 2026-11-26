# Rotting Fruit
# Medium
# Topics
# Company Tags
# Hints

# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit

# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Example 1:

# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

# Output: 4

# Example 2:

# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

# Output: -1

# Constraints:

# 1 <= grid.length, grid[i].length <= 10



# Topics

# Array Breadth-First Search Matrix


# Recommended Time & Space Complexity

# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the given grid.



# Hint 1

# The DFS algorithm is not suitable for this problem because it explores nodes deeply rather than level by level. In this scenario, we need to determine which oranges rot at each second, which naturally fits a level-by-level traversal. Can you think of an algorithm designed for such a traversal?



# Hint 2

# We can use the Breadth First Search (BFS) algorithm. At each second, we rot the oranges that are adjacent to the rotten ones. So, we store the rotten oranges in a queue and process them in one go. The time at which a fresh orange gets rotten is the level at which it is visited. How would you implement it?



# Hint 3

# We traverse the grid and store the rotten oranges in a queue. We then run a BFS, processing the current level of rotten oranges and visiting the adjacent cells of each rotten orange. We only insert the adjacent cell into the queue if it contains a fresh orange. This process continues until the queue is empty. The level at which the BFS stops is the answer. However, we also need to check whether all oranges have rotted by traversing the grid. If any fresh orange is found, we return -1; otherwise, we return the level.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 51.3%


from typing import List
from collections import deque
import copy
import traceback
from collections import deque


class Solution:
    def iter_bfs(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        min_mins = 0
        all_rotten = True
        q = deque([])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        while q:
            i, j, d = q.popleft() # d is distance

            if i-1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                q.append((i-1, j, d+1))
                min_mins = max(d+1, min_mins)

            if i+1 < rows and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                q.append((i+1, j, d+1))
                min_mins = max(d+1, min_mins)

            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                q.append((i, j-1, d+1))
                min_mins = max(d+1, min_mins)
            
            if j+1 < cols and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                q.append((i, j+1, d+1))
                min_mins = max(d+1, min_mins)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    all_rotten = False
        
        if not all_rotten:
            return -1
        
        return min_mins

    def oranges_rotting(self, grid: List[List[int]]) -> int:
        return self.iter_bfs(grid)


sol = Solution()

# run from the repo root: python3 -m graph.rotting_fruit
# (grid, expected minutes) - each test gets its own copy of the grid, so changing it inside your solution is fine
# 0 = empty, 1 = fresh, 2 = rotten
def g(*rows):
    """Write a grid as strings: g("120", "011") is [[1,2,0],[0,1,1]]."""
    return [[int(ch) for ch in r] for r in rows]

def full(n, value):
    return [[value] * n for _ in range(n)]

corner = full(10, 1); corner[0][0] = 2                      # 10x10 fresh, rotten in one corner
middle = full(10, 1); middle[4][4] = 2                      # 10x10 fresh, rotten near the middle
two_corners = full(10, 1); two_corners[0][0] = 2; two_corners[9][9] = 2
almost = full(10, 1); almost[0][0] = 2; almost[9][9] = 0      # same, but the far corner is empty
cut_off = full(10, 1); cut_off[0][0] = 2; cut_off[8][9] = 0; cut_off[9][8] = 0   # fresh corner walled off by empties
# winding path of fresh fruit: rows joined at alternating ends, empties everywhere else, rotten at the start
snake = [[1] * 10 if r % 2 == 0 else ([0] * 9 + [1] if r % 4 == 1 else [1] + [0] * 9) for r in range(10)]
snake[0][0] = 2

tests = [
    ([[1,1,0],[0,1,1],[0,1,2]], 4),         # example 1
    ([[1,0,1],[0,2,0],[1,0,1]], -1),        # example 2: rot can't move diagonally
    (g("0"), 0),                            # nothing at all: no fresh fruit, so 0 minutes
    (g("2"), 0),                            # only rotten fruit: already done
    (g("1"), -1),                           # fresh fruit and nothing to rot it
    (g("02"), 0),                           # no fresh fruit at the start: 0, not -1
    (g("21"), 1),                           # one minute
    (g("2111"), 3),                         # rot spreads one cell per minute
    (g("21112"), 2),                        # rot from both ends meets in the middle
    (g("201"), -1),                         # an empty cell blocks the spread
    (g("20", "01"), -1),                    # diagonal does not count
    (g("11", "11"), -1),                    # fresh fruit but no rotten fruit at all
    (g("22", "22"), 0),                     # all rotten
    (g("2", "1", "1", "0", "2", "1"), 2),   # one column, two separate groups, each with its own rotten fruit
    (g("211", "000", "112"), 2),            # two rows rot at the same time, the answer is the slower one
    (g("2110", "0001", "0002"), 2),         # two groups, each rotted by its own rotten fruit
    (g("21", "00", "11"), -1),              # one group rots fully, another group has no rotten fruit
    (full(10, 0), 0),                       # max size, all empty
    (corner, 18),                           # max size, rot travels corner to corner
    (middle, 10),                           # max size, rot starts near the middle
    (two_corners, 9),                       # max size, two sources: the farthest cell is 9 from both
    (almost, 17),                           # max size, the far corner is empty, so the answer drops
    (cut_off, -1),                          # max size, one fresh fruit in the corner can never be reached
    (snake, 54),                            # max size, one long winding path
]

def show(grid):
    if len(grid) * len(grid[0]) > 30:
        return f"[{len(grid)}x{len(grid[0])} grid]"
    return "[" + ",".join("".join(map(str, row)) for row in grid) + "]"

passed = 0
for grid, expected in tests:
    try:
        got = sol.oranges_rotting(copy.deepcopy(grid))
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})'
    ok = got == expected
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {show(grid)} -> {got}" + ("" if ok else f"  expected {expected}"))

print(f"{passed}/{len(tests)} passed")
