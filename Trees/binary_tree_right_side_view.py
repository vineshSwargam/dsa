# Binary Tree Right Side View
# Medium
# Topics
# Company Tags
# Hints

# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

# Example 1:

# Input: root = [1,2,3,null,4,null,5]

# Output: [1,3,5]

# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]

# Example 3:

# Input: root = [1,null,2]

# Output: [1,2]

# Example 4:

# Input: root = []

# Output: []



# Constraints:

# 0 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100



# Topics

# Tree Depth-First Search Breadth-First Search Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.



# Hint 1

# In the right-side view of a tree, can you identify the nodes that are visible? Maybe you could traverse the tree level by level and determine which nodes are visible from the right side.



# Hint 2

# The nodes visible in the right-side view are the last nodes at each level of the tree. Can you think of an algorithm to identify these nodes? Maybe an algorithm that can traverse the tree level by level.



# Hint 3

# We can use the Breadth First Search (BFS) algorithm to traverse the tree level by level. Once we completely visit a level, we take the last node of that level and add it to the result array. After processing all levels, we return the result.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 61.1%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional
from utils.tree import TreeNode, build_tree

class Solution:
    def using_iter_bfs(self, root):
        def bfs(r):
            q = deque([r]) if r else []
            res = []

            while q:
                level = []
                for _ in range(len(q)):
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if level:
                    res.append(level[-1])

            return res
                    
        return bfs(root)

    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        return self.using_iter_bfs(root)


sol = Solution()

# run from the repo root: python3 -m Trees.binary_tree_right_side_view
# (root, expected) - root in LeetCode level-order form
complete_100 = list(range(1, 101))                                    # 100 nodes, levels end at 1, 3, 7, 15, 31, 63, 100
left_chain_100 = [1] + [x for v in range(2, 101) for x in (v, None)]  # 1 -> 2 -> ... -> 100, all left children
right_chain_100 = [1] + [x for v in range(2, 101) for x in (None, v)] # 1 -> 2 -> ... -> 100, all right children

tests = [
    ([1,2,3,None,4,None,5], [1,3,5]),                   # example 1
    ([1,2,3,4,None,None,None,5], [1,3,4,5]),            # example 2, left side is longer, so it shows below
    ([1,None,2], [1,2]),                                # example 3
    ([], []),                                           # example 4, empty tree
    ([1], [1]),                                         # single node
    ([1,2], [1,2]),                                     # only a left child, still visible
    ([1,2,3,4], [1,3,4]),                               # deepest node is on the far left
    ([1,2,3,4,5,6,7], [1,3,7]),                         # full tree, right edge only
    ([1,2,3,None,5,None,4], [1,3,4]),                   # left node hidden behind the right one
    ([1,2,None,None,3], [1,2,3]),                       # zigzag: left, then right
    ([1,2,3,4,5,None,None,8], [1,3,5,8]),               # left branch goes two levels deeper than the right
    ([1,2,3,4,5,6,None,None,None,None,None,None,7], [1,3,6,7]),   # rightmost node comes from the right child's left
    ([5,5,5], [5,5]),                                   # duplicate values
    ([0,-100,100], [0,100]),                            # value limits
    ([-1,-2,-3,-4], [-1,-3,-4]),                        # all negatives
    (complete_100, [1,3,7,15,31,63,100]),               # max size, last level not full
    (left_chain_100, list(range(1, 101))),              # 100-deep left chain, every node visible
    (right_chain_100, list(range(1, 101))),             # 100-deep right chain, every node visible
]

passed = 0
for vals, expected in tests:
    got = sol.right_side_view(build_tree(vals))
    ok = got == expected
    passed += ok
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    got_shown = got if len(got) <= 20 else f"[{len(got)} values]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} -> {got_shown}")

print(f"{passed}/{len(tests)} passed")
