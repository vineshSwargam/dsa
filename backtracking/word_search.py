# Word Search
# Medium
# Topics
# Company Tags
# Hints

# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

# Example 1:

# Input:
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"

# Output: true

# Example 2:

# Input:
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"

# Output: false

# Constraints:

# 1 <= board.length, board[i].length <= 5
# 1 <= word.length <= 10
# board and word consists of only lowercase and uppercase English letters.



# Topics

# Array String Backtracking Depth-First Search Matrix


# Recommended Time & Space Complexity

# You should aim for a solution with O(m * (4^n)) time and O(n) space, where m is the number of cells in the given board and n is the size of the given word.



# Hint 1

# As we can start at any cell on the board, we can explore all paths from that cell. Can you think of an algorithm to do so? Also, you should consider a way to avoid visiting a cell that has already been visited in the current path.



# Hint 2

# We can use a hash set to avoid revisiting a cell in the current path by inserting the (row, col) of the visiting cell into the hash set and exploring all paths (four directions, as we can move to four neighboring cells) from that cell. Can you think of the base condition for this recursive path? Maybe you should consider the board boundaries, and also, we can extend a path if the character at the cell matches the character in the word.



# Hint 3

# We can use backtracking, starting from each cell on the board with coordinates (row, col) and index i for the given word. We return false if (row, col) is out of bounds or if board[row][col] != word[i]. When i reaches the end of the word, we return true, indicating a valid path. At each step, we add (row, col) to a hash set to avoid revisiting cells. After exploring the four possible directions, we backtrack and remove (row, col) from the hash set.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 48.0%


from typing import List
import copy
import traceback


class Solution:
  def using_recur_bt(self, board, target):
    # visd = set() # visited
    ib = len(board)
    jb = len(board[0])

    def search(wl, i, j):
      if wl == len(target):
        return True

      if not (ib-1 >= i >=0 and jb-1 >= j >=0):
        return False

      if board[i][j] != target[wl]:
        return False

      tmp = board[i][j]
      board[i][j] = '#'

      found = search(wl+1, i+1, j) or search(wl+1, i-1, j) or search(wl+1, i, j+1) or search(wl+1, i, j-1):

      board[i][j] = tmp
      return found

    for i in range(ib):
      for j in range(jb):
        if search(0, i, j):
          return True

    return False


  def exist(self, board: List[List[str]], word: str) -> bool:
      return self.using_recur_bt(board, word)


sol = Solution()

# run from the repo root: python3 -m backtracking.word_search
# (board, word, expected) - each test gets its own copy of the board, so changing it inside your solution is fine
ex = [["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]]                                        # board from the examples
lc = [["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]]                                        # another classic board
snake = [list("ABCDE"),
         list("JIHGF"),
         list("KLMNO"),
         list("TSRQP"),
         list("UVWXY")]                                         # 5x5, the alphabet winds back and forth
all_a = [["A"]*5 for _ in range(5)]                             # 5x5, every cell is A
corner_b = [["A"]*5 for _ in range(4)] + [["A"]*4 + ["B"]]      # 5x5 of A, with one B in the bottom-right corner

tests = [
    (ex, "CAT", True),                                          # example 1
    (ex, "BAT", False),                                         # example 2: B has no A next to it
    (ex, "XYZ", False),                                         # letters that are not on the board at all
    ([["A"]], "A", True),                                       # 1x1 board
    ([["A"]], "B", False),                                      # 1x1, wrong letter
    ([["A"]], "AA", False),                                     # the same cell can't be used twice
    ([["A","A"]], "AAA", False),                                # two A cells, a word needing three
    ([["A","B"],["C","D"]], "ABDC", True),                      # path turns a corner
    ([["A","B"],["C","D"]], "ABCD", False),                     # B to C would be a diagonal move
    ([["A","B"],["C","D"]], "ABDCA", False),                    # a full loop would come back to A
    (lc, "ABCCED", True),                                       # classic, path turns twice
    (lc, "SEE", True),                                          # classic, starts away from the top-left
    (lc, "ABCB", False),                                        # classic: needs B again, the only B is used
    ([["a","A"]], "aA", True),                                  # upper and lower case are different letters
    ([["a","A"]], "AA", False),                                 # ...so 'a' does not count as 'A'
    ([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB", True), # many A paths, only one ends next to B
    ([list("ABCDE")], "EDCBA", True),                           # one row, read backwards
    ([[x] for x in "ABCDE"], "BCDE", True),                     # one column, starts in the middle
    (snake, "ABCDEFGHIJ", True),                                # max word length, path snakes down the board
    (snake, "ABCDEFGHIK", False),                               # same, but the last step is not a neighbour
    (all_a, "AAAAAAAAAA", True),                                # max board and word, all the same letter
    (corner_b, "AAAAAAAAAB", True),                             # must end exactly next to the one B
    (all_a, "AAAAAAAAAB", False),                               # worst case: every path is tried, and none ends in B
]

def show(board):
    return "[" + ",".join("".join(row) for row in board) + "]"

passed = 0
for board, word, expected in tests:
    try:
        got = sol.exist(copy.deepcopy(board), word)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})'
    ok = got == expected
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {show(board)} {word!r} -> {got}" + ("" if ok else f"  expected {expected}"))

print(f"{passed}/{len(tests)} passed")
