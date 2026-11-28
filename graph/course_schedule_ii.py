# Course Schedule II
# Medium
# Topics
# Company Tags
# Hints

# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 3, prerequisites = [[1,0]]

# Output: [0,1,2]

# Explanation: We must ensure that course 0 is taken before course 1.

# Example 2:

# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

# Output: []

# Explanation: It's impossible to finish all courses.

# Constraints:

# 1 <= numCourses <= 1000
# 0 <= prerequisites.length <= 1000
# All prerequisite pairs are unique.



# Topics

# Depth-First Search Breadth-First Search Graph Theory Topological Sort


# Recommended Time & Space Complexity

# You should aim for a solution with O(V + E) time and O(V + E) space, where V is the number of courses (nodes) and E is the number of prerequisites (edges).



# Hint 1

# Consider the problem as a graph where courses represent the nodes, and prerequisite[i] = [a, b] represents a directed edge from a to b. We need to determine whether the graph contains a cycle. Why? Because if there is a cycle, it is impossible to complete the courses involved in the cycle. Can you think of an algorithm to detect a cycle in a graph and also find the valid ordering if a cycle doesn't exist?



# Hint 2

# We can use DFS to detect a cycle in a graph. However, we also need to find the valid ordering of the courses, which can also be achieved using DFS. Alternatively, we can use the Topological Sort algorithm to find the valid ordering in this directed graph, where the graph must be acyclic to complete all the courses, and the prerequisite of a course acts as the parent node of that course. How would you implement this?



# Hint 3

# We compute the indegrees of all the nodes. Then, we perform a BFS starting from the nodes that have no parents (indegree[node] == 0). At each level, we traverse these nodes, decrement the indegree of their child nodes, and append those child nodes to the queue if their indegree becomes 0. We only append nodes whose indegree is 0 or becomes 0 during the BFS to our result array. If the length of the result array is not equal to the number of courses, we return an empty array.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 64.0%


from typing import List
import traceback
from collections import defaultdict, deque


class Solution:
    def using_iter_dfs(self, nc, reqs):
        cdm = { i: [] for i in range(nc) }

        for c, d in reqs:
            cdm[c].append(d)

        visited = set()
        done = set()
        order = []

        for i in range(nc):
            st = [(i, False)]
            while st:
                c, exiting = st.pop()

                if exiting:
                    visited.remove(c)
                    done.add(c)
                    order.append(c)
                    continue

                if c in done:
                    continue

                if c in visited:
                    return []
                    
                visited.add(c)
                st.append((c, True))
                # order.append(c)
                for d in cdm[c]:
                    st.append((d, False))
        
        return order



    def using_kahn(self, nc, reqs):
        # need a { [course x]: [unblocks these courses]} dict
        unblock = defaultdict(list)
        # need a count of how many courses are blocking a course i
        blocks = [0]*nc

        # populate both
        for c, d in reqs:
            unblock[d].append(c)
            blocks[c] += 1
        
        # start the queue with unblocked courses first
        q = deque(i for i, blocks_count in enumerate(blocks) if blocks_count == 0)
        completed = [] # track courses completed to return whethere nc courses are completed or not

        while q:
            c = q.popleft()
            completed.append(c)

            for d in unblock[c]: # c is completed, so let's decrement the block counts
                blocks[d] -= 1
                if blocks[d] == 0: # this is ready for completion, push in q
                    q.append(d)
        
        if len(completed) == nc:
            return completed
        
        return []
            
    def find_order(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return self.using_kahn(numCourses, prerequisites)
        return self.using_iter_dfs(numCourses, prerequisites)


sol = Solution()

# run from the repo root: python3 -m graph.course_schedule_ii
# (numCourses, prerequisites, possible). [a, b] means take b before a.
# Many orders can be right, so the test doesn't compare to one answer. It checks that:
#   - possible: the order has every course exactly once, and b comes before a for every [a, b]
#   - impossible: the answer is []

# 1000 courses in one line: 0 needs 1, 1 needs 2, ... 998 needs 999
chain_1000 = [[i, i + 1] for i in range(999)]
# the same line, but the last course needs the first: one big loop
loop_1000 = chain_1000 + [[999, 0]]

# 251 layers of 2 courses; each course needs both courses in the next layer (1000 pairs).
# No loop, but there are 2^250 different routes from the top to the bottom.
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
    (3, [[1,0]], True),                                    # example 1: course 2 has no pairs but must still be in the order
    (3, [[0,1],[1,2],[2,0]], False),                       # example 2
    (1, [], True),                                         # one course
    (4, [], True),                                         # no prerequisites: any order of all 4
    (2, [[0,1]], True),                                    # 1 then 0
    (2, [[0,1],[1,0]], False),                             # two courses need each other
    (1, [[0,0]], False),                                   # a course that needs itself
    (4, [[1,0],[2,1],[3,2]], True),                        # a straight line: only one right order
    (4, [[0,1],[1,2],[2,3]], True),                        # the same line, backwards: 3, 2, 1, 0
    (4, [[1,0],[2,0],[3,1],[3,2]], True),                  # diamond: 0 first, 3 last
    (4, [[1,0],[2,3],[3,2]], False),                       # the loop is in a separate group
    (4, [[0,1],[1,2],[2,3],[3,1]], False),                 # 0 is fine on its own, but leads into a loop
    (6, [[1,0],[2,1],[4,3],[5,4]], True),                  # two separate lines
    (5, [[1,0],[2,0],[3,0],[4,0]], True),                  # everyone needs course 0
    (5, [[0,1],[0,2],[0,3],[0,4]], True),                  # course 0 needs everyone, so it comes last
    (5, [[0,1],[1,2],[2,3],[3,4],[4,2]], False),           # loop at the end of a line
    (6, [[3,0],[3,1],[4,1],[4,2],[5,3],[5,4]], True),      # courses with two prerequisites each
    (7, [[1,0],[2,1],[3,2],[4,0],[5,4],[6,5],[6,3]], True),   # two routes from 0 that join at 6
    (1000, [], True),                                      # max courses, nothing needed
    (1000, chain_1000, True),                              # max size, 1000 courses in one line: deep recursion
    (1000, loop_1000, False),                              # max size, one 1000-course loop
    (502, ladder(False), True),                            # 2^250 routes and no loop: too slow without remembering finished courses
    (502, ladder(True), False),                            # same, with a loop from the bottom back to the top
]

def check(n, pairs, possible, got):
    """Return "" if got is a right answer, otherwise what's wrong."""
    if not isinstance(got, list):
        return f"expected a list, got {type(got).__name__}"
    if not possible:
        return "" if got == [] else "expected [] (there's a loop)"
    if len(got) != n or sorted(got) != list(range(n)):
        missing = sorted(set(range(n)) - set(got))
        extra = len(got) - len(set(got))
        return (f"should have each of the {n} courses once; got {len(got)} items"
                + (f", missing {missing[:5]}" if missing else "")
                + (f", {extra} repeated" if extra else ""))
    pos = {c: i for i, c in enumerate(got)}
    for a, b in pairs:
        if pos[b] > pos[a]:
            return f"course {a} comes before its prerequisite {b}"
    return ""

def show(x):
    return str(x) if len(x) <= 8 else f"[{len(x)} items]"

passed = 0
for n, pairs, possible in tests:
    try:
        got = sol.find_order(n, [p[:] for p in pairs])
        why = check(n, pairs, possible, got)
        ok = why == ""
        shown = show(got) if isinstance(got, list) else got
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        ok, why = False, ""
        shown = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})'
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  n={n}, {show(pairs)} -> {shown}" + ("" if ok else f"  ({why})" if why else ""))

print(f"{passed}/{len(tests)} passed")
