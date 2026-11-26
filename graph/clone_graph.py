# Clone Graph
# Medium
# Topics
# Company Tags
# Hints

# Given a node in a connected undirected graph, return a deep copy of the graph.

# Each node in the graph contains an integer value and a list of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

# The input node will always be the first node in the graph and have 1 as the value.

# Example 1:

# Input: adjList = [[2],[1,3],[2]]

# Output: [[2],[1,3],[2]]

# Explanation: There are 3 nodes in the graph.
# Node 1: val = 1 and neighbors = [2].
# Node 2: val = 2 and neighbors = [1, 3].
# Node 3: val = 3 and neighbors = [2].

# Example 2:

# Input: adjList = [[]]

# Output: [[]]

# Explanation: The graph has one node with no neighbors.

# Example 3:

# Input: adjList = []

# Output: []

# Explanation: The graph is empty.

# Constraints:

# 0 <= The number of nodes in the graph <= 100.
# 1 <= Node.val <= 100
# There are no duplicate edges and no self-loops in the graph.



# Topics

# Hash Table Depth-First Search Breadth-First Search Graph


# Recommended Time & Space Complexity

# You should aim for a solution with O(V + E) time and O(V) space, where V is the number of vertices and E is the number of edges in the given graph.



# Hint 1

# We are given only the reference to the node in the graph. Cloning the entire graph means we need to clone all the nodes as well as their child nodes. We can't just clone the node and its neighbor and return the node. We also need to clone the entire graph. Can you think of a recursive way to do this, as we are cloning nodes in a nested manner? Also, can you think of a data structure that can store the nodes with their cloned references?



# Hint 2

# We can use the Depth First Search (DFS) algorithm. We use a hash map to map the nodes to their cloned nodes. We start from the given node. At each step of the DFS, we create a node with the current node's value. We then recursively go to the current node's neighbors and try to clone them first. After that, we add their cloned node references to the current node's neighbors list. Can you think of a base condition to stop this recursive path?



# Hint 3

# We stop this recursive path when we encounter a node that has already been cloned or visited. This DFS approach creates an exact clone of the given graph, and we return the clone of the given node.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 76.1%


from typing import Optional
from collections import deque
import traceback


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: Optional['Node']) -> Optional['Node']:
        pass


sol = Solution()

# run from the repo root: python3 -m graph.clone_graph
# (adj_list, description) - adj_list[i] lists the neighbours of node i+1, like in the examples.
# Each test builds the graph, gives your solution node 1, then checks what comes back:
#   - same shape: walking your copy gives back exactly the same adjacency list (neighbour order included)
#   - a real copy: none of the nodes you return is one of the original nodes
#   - one copy per node: every value appears on exactly one copied node, even when it is reached many ways
#   - the original graph is left unchanged
def build(adj):
    """Turn an adjacency list into real nodes, and return the list of nodes (node 1 is at index 0)."""
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[v - 1] for v in nbrs]
    return nodes

def walk(start):
    """Visit every node reachable from start. Returns {val: node}, or a string saying what went wrong."""
    seen = {}
    q = deque([start])
    while q:
        n = q.popleft()
        if not isinstance(n, Node):
            return f"found {n!r} in a neighbours list, expected a Node"
        if n.val in seen:
            if seen[n.val] is not n:
                return f"value {n.val} appears on two different copied nodes"
            continue
        seen[n.val] = n
        q.extend(n.neighbors)
    return seen

def to_adj(by_val):
    return [[nb.val for nb in by_val[v].neighbors] for v in range(1, len(by_val) + 1)]

line_100 = [[2]] + [[i - 1, i + 1] for i in range(2, 100)] + [[99]]                 # 1 - 2 - 3 - ... - 100
ring_100 = [[2, 100]] + [[i - 1, i + 1] for i in range(2, 100)] + [[99, 1]]          # same line, with 100 joined back to 1
complete_100 = [[j for j in range(1, 101) if j != i] for i in range(1, 101)]          # every node joined to every other one
star_100 = [list(range(2, 101))] + [[1] for _ in range(99)]                          # node 1 in the middle, 99 leaves
star_leaf = [[2], [1] + list(range(3, 101))] + [[2] for _ in range(98)]              # node 1 is a leaf, node 2 is the middle
grid_10 = [[(r + dr) * 10 + (c + dc) + 1                                             # 10x10 grid, nodes 1..100 row by row
            for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)) if 0 <= r + dr < 10 and 0 <= c + dc < 10]
           for r in range(10) for c in range(10)]

tests = [
    ([[2],[1,3],[2]], "example 1: a line of 3"),
    ([[]], "example 2: one node, no neighbours"),
    ([], "example 3: empty graph, you get None and should return None"),
    ([[2],[1]], "two nodes pointing at each other: a cycle right away"),
    ([[2,3],[1,3],[1,2]], "triangle: node 3 is reached from both 1 and 2"),
    ([[2,4],[1,3],[2,4],[1,3]], "square: 1-2-3-4-1"),
    ([[2,3,4],[1,3,4],[1,2,4],[1,2,3]], "4 nodes, all joined to each other"),
    ([[3,2],[1],[1]], "neighbour order is not sorted, and must stay that way"),
    ([[2],[1,3,4],[2],[2,5],[4]], "small tree, node 1 is a leaf"),
    (line_100, "100 nodes in a line: a long path"),
    (ring_100, "100 nodes in a ring: a long cycle"),
    (star_100, "node 1 in the middle of 99 leaves"),
    (star_leaf, "node 1 is a leaf, the middle is one step away"),
    (grid_10, "10x10 grid: many different paths reach the same node"),
    (complete_100, "100 nodes all joined to each other: 4950 edges"),
]

def check(adj, got, original_ids):
    if not adj:
        return (got is None), ("" if got is None else "  expected None")
    if not isinstance(got, Node):
        return False, f"  expected a Node, got {got!r}"
    by_val = walk(got)
    if isinstance(by_val, str):
        return False, "  " + by_val
    if any(id(n) in original_ids for n in by_val.values()):
        return False, "  returned an original node, not a copy"
    if sorted(by_val) != list(range(1, len(adj) + 1)):
        return False, f"  copy has values {sorted(by_val)[:10]}..., expected 1..{len(adj)}"
    got_adj = to_adj(by_val)
    if got_adj != adj:
        bad = next(i for i in range(len(adj)) if got_adj[i] != adj[i])
        return False, f"  node {bad + 1} has neighbours {got_adj[bad]}, expected {adj[bad]}"
    if got.val != 1:
        return False, f"  returned node {got.val}, expected the copy of node 1"
    return True, ""

passed = 0
for adj, desc in tests:
    nodes = build(adj)
    original_ids = {id(n) for n in nodes}
    try:
        got = sol.clone_graph(nodes[0] if nodes else None)
        ok, why = check(adj, got, original_ids)
        if ok and nodes and to_adj(walk(nodes[0])) != adj:
            ok, why = False, "  the original graph was changed"
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        ok, why = False, f'  ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})'
    passed += ok
    shown = adj if len(adj) <= 5 else f"[{len(adj)} nodes]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown}  {desc}{why}")

print(f"{passed}/{len(tests)} passed")
