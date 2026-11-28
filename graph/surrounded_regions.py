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


from typing import List
import copy
import traceback


class Solution:
    def using_iter_bfs(self, b):
      rows = len(b)
      cols = len(b[0])
      st = []
      safe = set()

      for i in range(rows):
        for j in range(cols):
          if b[i][j] == 'O' and (i==0 or j==0 or i==rows-1 or j==cols-1):
            st.append((i, j))
            safe.add((i, j))
      
      while st:
        i, j = st.pop()

        if i-1 >= 0 and b[i-1][j]=='O' and (i-1,j) not in safe:
          st.append((i-1, j))
          safe.add((i-1, j))
        if i+1 < rows and b[i+1][j]=='O' and (i+1,j) not in safe:
          st.append((i+1, j))
          safe.add((i+1, j))
        if j-1 >= 0 and b[i][j-1]=='O' and (i,j-1) not in safe:
          st.append((i, j-1))
          safe.add((i, j-1))
        if j+1 < cols and b[i][j+1]=='O' and (i,j+1) not in safe:
          st.append((i, j+1))
          safe.add((i, j+1))
      
      for i in range(rows):
        for j in range(cols):
          if b[i][j]=='O' and (i, j) not in safe:
            b[i][j] = 'X'

    def solve(self, board: List[List[str]]) -> None:
        return self.using_iter_bfs(board)


sol = Solution()

# run from the repo root: python3 -m graph.surrounded_regions
# (board, expected) - your solution changes the board in place (nothing is returned), and the test
# compares the changed board to expected. Each test gets its own copy of the board.

def b(*rows):
    """Write a small board as strings, e.g. b("XOX", "XXX")."""
    return [list(r) for r in rows]

N = 200
# 200x200, all O: every region touches the edge, nothing changes
all_o = [["O"] * N for _ in range(N)]
# 200x200, X border with O everywhere inside: the whole inside is captured
walled = [["O"] * N for _ in range(N)]
for i in range(N):
    walled[0][i] = walled[N-1][i] = walled[i][0] = walled[i][N-1] = "X"
all_x = [["X"] * N for _ in range(N)]

# 200x200 winding path of O inside an X border: full rows joined at alternating ends.
# One long region of about 20,000 cells.
def snake(open_to_edge):
    grid = [["X"] * N for _ in range(N)]
    for r in range(1, N - 1):
        if r % 2 == 1:
            for c in range(1, N - 1):
                grid[r][c] = "O"
        else:
            grid[r][N - 2 if r % 4 == 2 else 1] = "O"
    if open_to_edge:
        grid[1][0] = "O"      # one O on the edge, joined to the start of the path
    return grid
snake_open = snake(True)
snake_closed = snake(False)

# 200x200 checkerboard: every O is alone, so only the ones on the edge survive
checker = [["O" if (r + c) % 2 == 0 else "X" for c in range(N)] for r in range(N)]
checker_out = [["O" if (r + c) % 2 == 0 and (r in (0, N-1) or c in (0, N-1)) else "X"
                for c in range(N)] for r in range(N)]

tests = [
    (b("XXXX", "XOOX", "XXOX", "XOXX"), b("XXXX", "XXXX", "XXXX", "XOXX")),    # example 1
    (b("X"), b("X")),                                                        # example 2
    (b("O"), b("O")),                                                        # single O is on the edge
    (b("XXX", "XOX", "XXX"), b("XXX", "XXX", "XXX")),                        # one O in the middle is captured
    (b("OOO", "OOO", "OOO"), b("OOO", "OOO", "OOO")),                        # all O: the region touches the edge
    (b("OO", "OO"), b("OO", "OO")),                                          # 2x2: every cell is on the edge
    (b("XOOX"), b("XOOX")),                                                  # one row: everything is on the edge
    (b("X", "O", "O", "X"), b("X", "O", "O", "X")),                          # one column: same
    (b("XXXX", "XOOX", "XOOX", "XXXX"), b("XXXX", "XXXX", "XXXX", "XXXX")),  # 2x2 block in the middle is captured
    (b("XXXX", "XOOX", "XOOX", "XOXX"), b("XXXX", "XOOX", "XOOX", "XOXX")),  # same block, but one O reaches the bottom edge
    (b("XXXX", "XOXX", "XXOX", "XXXO"), b("XXXX", "XXXX", "XXXX", "XXXO")),  # diagonal doesn't connect: inner O's are captured
    (b("XXXXX", "XOXOX", "XXXOX", "XXXOX"),
     b("XXXXX", "XXXOX", "XXXOX", "XXXOX")),                                 # two regions: the lone O is captured, the column reaches the edge
    (b("XXXXXXX",
       "XOOOOOX",
       "XOXXXOX",
       "XOXOXOX",
       "XOXXXOX",
       "XOOOOOX",
       "XXXXXXX"), [["X"] * 7 for _ in range(7)]),                           # a ring and its centre, all enclosed: all captured
    (b("XXXXXXX",
       "XOOOOOO",
       "XOXXXOX",
       "XOXOXOX",
       "XOXXXOX",
       "XOOOOOX",
       "XXXXXXX"),
     b("XXXXXXX",
       "XOOOOOO",
       "XOXXXOX",
       "XOXXXOX",
       "XOXXXOX",
       "XOOOOOX",
       "XXXXXXX")),                                                          # ring touches the edge and stays, the centre is captured
    (b("XXXXXX",
       "XOXXXX",
       "XOOOOX",
       "XXXXOX",
       "XXXXOO"),
     b("XXXXXX",
       "XOXXXX",
       "XOOOOX",
       "XXXXOX",
       "XXXXOO")),                                                           # a long winding region escapes at the far corner
    (all_o, copy.deepcopy(all_o)),                                           # max size, all O: nothing changes
    (walled, all_x),                                                         # max size, the whole inside is captured
    (copy.deepcopy(all_x), all_x),                                           # max size, no O at all
    (checker, checker_out),                                                  # max size, every O alone: only edge O's stay
    (snake_open, copy.deepcopy(snake_open)),                                 # max size, ~20,000-cell path that reaches the edge: nothing changes
    (snake_closed, all_x),                                                   # max size, same path sealed off: all captured
]

def show(board):
    if len(board) * len(board[0]) > 30:
        return f"[{len(board)}x{len(board[0])} board]"
    return "[" + ",".join("".join(r) for r in board) + "]"

def first_diff(got, expected):
    for r in range(len(expected)):
        for c in range(len(expected[0])):
            if got[r][c] != expected[r][c]:
                return f"  first wrong cell ({r},{c}): got {got[r][c]!r}, expected {expected[r][c]!r}"
    return ""

passed = 0
for board, expected in tests:
    work = copy.deepcopy(board)
    try:
        sol.solve(work)
        ok = work == expected
        why = "" if ok else first_diff(work, expected)
        got = show(work)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        ok, why, got = False, "", f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})'
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {show(board)} -> {got}" + ("" if ok else f"  expected {show(expected)}{why}"))

print(f"{passed}/{len(tests)} passed")
