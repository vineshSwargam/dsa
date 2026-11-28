# Course Schedule
# Medium
# Topics
# Company Tags
# Hints

# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# The pair [0, 1], indicates that must take course 1 before taking course 0.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.




# Example 1:

# Input: numCourses = 2, prerequisites = [[0,1]]

# Output: true

# Explanation: First take course 1 (no prerequisites) and then take course 0.




# Example 2:

# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

# Output: false

# Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.




# Constraints:

# 1 <= numCourses <= 1000
# 0 <= prerequisites.length <= 1000
# prerequisites[i].length == 2
# 0 <= a[i], b[i] < numCourses
# All prerequisite pairs are unique.



# Topics

# Depth-First Search Breadth-First Search Graph Theory Topological Sort


# Recommended Time & Space Complexity

# You should aim for a solution with O(V + E) time and O(V + E) space, where V is the number of courses (nodes) and E is the number of prerequisites (edges).



# Hint 1

# Consider the problem as a graph where courses represent the nodes, and prerequisite[i] = [a, b] represents a directed edge from a to b. We need to determine whether the graph contains a cycle. Why? Because if there is a cycle, it is impossible to complete the courses involved in the cycle. Can you think of an algorithm to detect cycle in a graph?



# Hint 2

# We can use the Depth First Search (DFS) algorithm to detect a cycle in a graph. We iterate over each course, run a DFS from that course, and first try to finish its prerequisite courses by recursively traversing through them. To detect a cycle, we initialize a hash set called path, which contains the nodes visited in the current DFS call. If we encounter a course that is already in the path, we can conclude that a cycle is detected. How would you implement it?



# Hint 3

# We run a DFS starting from each course by initializing a hash set, path, to track the nodes in the current DFS call. At each step of the DFS, we return false if the current node is already in the path, indicating a cycle. We recursively traverse the neighbors of the current node, and if any of the neighbor DFS calls detect a cycle, we immediately return false. Additionally, we clear the neighbors list of a node when no cycle is found from that node to avoid revisiting those paths again.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 58.5%


from typing import List
import traceback


class Solution:
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


sol = Solution()

# run from the repo root: python3 -m graph.course_schedule
# (numCourses, prerequisites, expected). [a, b] means take b before a.

# 1000 courses in one line: 0 needs 1, 1 needs 2, ... 998 needs 999
chain_1000 = [[i, i + 1] for i in range(999)]
# the same line, but the last course needs the first: one big loop
loop_1000 = chain_1000 + [[999, 0]]

# 251 layers of 2 courses; each course needs both courses in the next layer (1000 pairs).
# No loop, but there are 2^250 different routes from the top to the bottom, so
# without remembering finished courses this never ends.
def ladder(with_loop):
    pairs = []
    for layer in range(250):
        for a in (2 * layer, 2 * layer + 1):
            for b in (2 * layer + 2, 2 * layer + 3):
                pairs.append([a, b])
    if with_loop:
        pairs[-1] = [501, 0]       # swap one pair for a loop from the bottom back to the top
    return pairs

tests = [
    (2, [[0,1]], True),                                    # example 1
    (2, [[0,1],[1,0]], False),                             # example 2: two courses need each other
    (1, [], True),                                         # one course, nothing needed
    (5, [], True),                                         # no prerequisites at all
    (1, [[0,0]], False),                                   # a course that needs itself
    (4, [[1,0],[2,1],[3,2]], True),                        # a straight line
    (3, [[0,1],[1,2],[2,0]], False),                       # three courses in a loop
    (4, [[1,0],[2,0],[3,1],[3,2]], True),                  # diamond: course 0 is reached twice, but there's no loop
    (4, [[1,0],[2,3],[3,2]], False),                       # the loop is in a separate group, away from course 0
    (4, [[0,1],[1,2],[2,3],[3,1]], False),                 # 0 is fine on its own, but leads into a loop
    (6, [[1,0],[2,1],[4,3],[5,4]], True),                  # two separate lines
    (5, [[1,0],[2,0],[3,0],[4,0]], True),                  # everyone needs course 0
    (5, [[0,1],[0,2],[0,3],[0,4]], True),                  # course 0 needs everyone
    (5, [[0,1],[1,2],[2,3],[3,4],[4,2]], False),           # loop at the end of a line
    (3, [[1,0],[2,1],[0,2]], False),                       # same loop as above, listed in another order
    (6, [[0,1],[1,2],[3,4],[4,5],[5,3],[2,0]], False),     # two loops
    (1000, [], True),                                      # max courses, nothing needed
    (1000, chain_1000, True),                              # max size, 1000 courses in one line: deep recursion
    (1000, loop_1000, False),                              # max size, one 1000-course loop
    (502, ladder(False), True),                            # 2^250 routes and no loop: too slow without remembering finished courses
    (502, ladder(True), False),                            # same, with a loop from the bottom back to the top
]

def show(pairs):
    return str(pairs) if len(pairs) <= 6 else f"[{len(pairs)} pairs]"

passed = 0
for n, pairs, expected in tests:
    try:
        got = sol.can_finish(n, [p[:] for p in pairs])
        ok = got == expected
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  n={n}, {show(pairs)} -> {got}" + ("" if ok else f"  expected {expected}"))

print(f"{passed}/{len(tests)} passed")
