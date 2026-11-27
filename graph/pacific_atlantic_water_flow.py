# Pacific Atlantic Water Flow
# Medium
# Topics
# Company Tags
# Hints

# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

# Example 1:

# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]

# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

# Example 2:

# Input: heights = [[1],[1]]

# Output: [[0,0],[1,0]]

# Constraints:

# 1 <= heights.length, heights[r].length <= 100
# 0 <= heights[r][c] <= 1000



# Topics

# Array Depth-First Search Breadth-First Search Matrix


# Recommended Time & Space Complexity

# You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.



# Hint 1

# A brute force solution would be to traverse each cell in the grid and run a BFS from each cell to check if it can reach both oceans. This would result in an O((m * n)^2) solution. Can you think of a better way? Maybe you should consider a reverse way of traversing.



# Hint 2

# We can use the Depth First Search (DFS) algorithm starting from the border cells of the grid. However, we reverse the condition such that the next visiting cell should have a height greater than or equal to the current cell. For the top and left borders connected to the Pacific Ocean, we use a hash set called pacific and run a DFS from each of these cells, visiting nodes recursively. Similarly, for the bottom and right borders connected to the Atlantic Ocean, we use a hash set called atlantic and run a DFS. The required coordinates are the cells that exist in both the pacific and atlantic sets. How do you implement this?



# Hint 3

# We perform DFS from the border cells, using their respective hash sets. During the DFS, we recursively visit the neighbouring cells that are unvisited and have height greater than or equal to the current cell's height and add the current cell's coordinates to the corresponding hash set. Once the DFS completes, we traverse the grid and check if a cell exists in both the hash sets. If so, we add that cell to the result list.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 67.0%


from typing import List
import traceback


class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass


sol = Solution()

# run from the repo root: python3 -m graph.pacific_atlantic_water_flow
# (heights, expected) - the cells can come back in any order
# Pacific = top and left edges, Atlantic = bottom and right edges.
# Water moves to a neighbour that is equal or LOWER.
flat_100 = [[7] * 100 for _ in range(100)]                                     # 100x100, all the same height
slope_100 = [[r + c for c in range(100)] for r in range(100)]                  # 100x100, rises toward the bottom-right
slope_100_answer = [[99, c] for c in range(100)] + [[r, 99] for r in range(99)]   # only the bottom row and right column
row_100 = [[(c * 37) % 1001 for c in range(100)]]                              # one row: every cell touches both oceans
col_100 = [[(r * 53) % 1001] for r in range(100)]                              # one column: same

tests = [
    ([[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]],
     [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]),                       # example 1
    ([[1],[1]], [[0,0],[1,0]]),                                               # example 2
    ([[5]], [[0,0]]),                                                         # one cell touches all four sides
    ([[0]], [[0,0]]),                                                         # height 0 still flows into both oceans
    ([[1,2,3]], [[0,0],[0,1],[0,2]]),                                         # one row: top is Pacific, bottom is Atlantic
    ([[3],[1],[2]], [[0,0],[1,0],[2,0]]),                                     # one column: left is Pacific, right is Atlantic
    ([[1,1],[1,1]], [[0,0],[0,1],[1,0],[1,1]]),                               # flat: water moves across equal heights
    ([[3,3,3],[3,1,3],[3,3,3]],
     [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]),                      # pit in the middle: the pit can't flow uphill
    ([[1,1,1],[1,5,1],[1,1,1]],
     [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]),                # peak in the middle: it flows everywhere
    ([[1,2],[2,3]], [[0,1],[1,0],[1,1]]),                                     # top-left is lowest: it only reaches the Pacific
    ([[3,2],[2,1]], [[0,0],[0,1],[1,0]]),                                     # bottom-right is lowest: it only reaches the Atlantic
    ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
     [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),                            # classic 5x5
    ([[0,1000],[1000,0]], [[0,1],[1,0]]),                                     # height limits
    ([[10,10,10],[10,1,10],[10,10,10],[1,1,1]],
     [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2]]),    # low bottom row: touches both oceans itself
    (flat_100, [[r, c] for r in range(100) for c in range(100)]),             # max size, flat: every cell
    (slope_100, slope_100_answer),                                            # max size, slope: water can't climb to the Atlantic
    (row_100, [[0, c] for c in range(100)]),                                  # max length row
    (col_100, [[r, 0] for r in range(100)]),                                  # max length column
]

def normal(cells):
    return sorted(list(c) for c in cells)

def show(grid):
    if len(grid) * len(grid[0]) > 30:
        return f"[{len(grid)}x{len(grid[0])} grid]"
    return str(grid)

passed = 0
for heights, expected in tests:
    try:
        got = sol.pacific_atlantic([row[:] for row in heights])
        ok = isinstance(got, list) and normal(got) == normal(expected)
        why = ""
        if isinstance(got, list) and not ok:
            g, e = set(map(tuple, got)), set(map(tuple, expected))
            extra, missing = sorted(g - e), sorted(e - g)
            why = (f"  extra {extra[:5]}" if extra else "") + (f"  missing {missing[:5]}" if missing else "")
            if not extra and not missing:
                why = "  some cells appear more than once"
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} cells" if isinstance(got, list) and len(got) > 12 else got
    want = f"{len(expected)} cells" if len(expected) > 12 else expected
    print(f"{'PASS' if ok else 'FAIL'}  {show(heights)} -> {shown}" + ("" if ok else f"  expected {want}{why}"))

print(f"{passed}/{len(tests)} passed")
