# Binary Tree Level Order Traversal
# Medium
# Topics
# Company Tags
# Hints

# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Example 1:

# Input: root = [1,2,3,4,5,6,7]

# Output: [[1],[2,3],[4,5,6,7]]

# Example 2:

# Input: root = [1]

# Output: [[1]]

# Example 3:

# Input: root = []

# Output: []

# Constraints:

# 0 <= The number of nodes in the tree <= 2000.
# -1000 <= Node.val <= 1000



# Topics

# Tree Breadth-First Search Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.



# Hint 1

# The level of a tree refers to the nodes that are at equal distance from the root node. Can you think of an algorithm that traverses the tree level by level, rather than going deeper into the tree?



# Hint 2

# We can use the Breadth First Search (BFS) algorithm to traverse the tree level by level. BFS uses a queue data structure to achieve this. At each step of BFS, we only iterate over the queue up to its size at that step. Then, we take the left and right child pointers and add them to the queue. This allows us to explore all paths simultaneously.



# Hint 3

# The number of times we iterate the queue corresponds to the number of levels in the tree. At each step, we pop all nodes from the queue for the current level and add them collectively to the resultant array. This ensures that we capture all nodes at each level of the tree.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 80.4%


from typing import List, Optional
from utils.tree import TreeNode, build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def using_iterative_bfs(self, root):
        def bfs(r):
            q = deque([(r, 1)]) if r else []
            res = []

            while q:
                node, dep = q.popleft()
                if len(res) < dep:
                    res.append([node.val])
                else:
                    res[dep-1].append(node.val)
                
                if node.left:
                    q.append((node.left, dep+1))
                if node.right:
                    q.append((node.right, dep+1))
            
            return res
        
        return bfs(root)

    # without depth tuples
    def using_improved_iterative_bfs(self, root):
        def bfs(r):
            q = deque([r]) if r else []
            res = []

            while q:
                nlist = []
                for _ in range(len(q)):
                    node = q.popleft()
                    nlist.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(nlist)
            
            return res
        
        return bfs(root)


    def using_recursive_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(r, d):
            if len(res) < d:
                res.append([r.val])
            else:
                res[d-1].append(r.val)
            
            if r.left:
                dfs(r.left, d+1)
            if r.right:
                dfs(r.right, d+1)
        
        if not root:
            return []
        
        dfs(root, 1)
        return res

            

    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return self.using_recursive_bfs(root)
        # return self.using_iterative_bfs(root)
        return self.using_improved_iterative_bfs(root)


sol = Solution()

# run from the repo root: python3 -m Trees.binary_tree_level_order_traversal
# (root, expected) - root in LeetCode level-order form
complete_2000 = list(range(1, 2001))                                    # 2000 nodes, every level full except the last
complete_2000_levels = [complete_2000[2**d - 1 : 2**(d + 1) - 1] for d in range(11)]   # [1], [2,3], [4..7], ... [1024..2000]
left_chain_2000 = [1] + [x for v in range(2, 2001) for x in (v, None)]  # 1 -> 2 -> ... -> 2000, all left children
right_chain_2000 = [1] + [x for v in range(2, 2001) for x in (None, v)] # 1 -> 2 -> ... -> 2000, all right children
one_per_level_2000 = [[v] for v in range(1, 2001)]

tests = [
    ([1,2,3,4,5,6,7], [[1],[2,3],[4,5,6,7]]),          # example 1, full tree
    ([1], [[1]]),                                       # example 2, single node
    ([], []),                                           # example 3, empty tree
    ([1,2], [[1],[2]]),                                 # only a left child
    ([1,None,2], [[1],[2]]),                            # only a right child
    ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),     # left side ends early
    ([1,2,3,4,None,None,5], [[1],[2,3],[4,5]]),         # gap in the middle of a level
    ([1,2,3,None,4,5], [[1],[2,3],[4,5]]),              # children on the inner sides
    ([1,2,3,4,None,None,5,6,None,None,7], [[1],[2,3],[4,5],[6,7]]),   # two separate deep branches
    ([1,2,None,None,3,4], [[1],[2],[3],[4]]),           # zigzag: left, right, left
    ([1,2,3,4,5,6,7,8], [[1],[2,3],[4,5,6,7],[8]]),     # last level has a single node
    ([5,5,5,5,5], [[5],[5,5],[5,5]]),                   # duplicate values
    ([0,-1000,1000,-1000,-1000], [[0],[-1000,1000],[-1000,-1000]]),   # value limits and zero
    ([-1,-2,-3], [[-1],[-2,-3]]),                       # all negatives, order is left to right not by value
    ([1,3,2], [[1],[3,2]]),                             # not sorted, keep tree order
    (complete_2000, complete_2000_levels),              # max size, 11 levels
    (left_chain_2000, one_per_level_2000),              # 2000-deep left chain
    (right_chain_2000, one_per_level_2000),             # 2000-deep right chain
]

passed = 0
for vals, expected in tests:
    try:
        got = sol.level_order(build_tree(vals))
    except RecursionError:
        got = 'ERROR (too deep for recursion)'
    ok = got == expected
    passed += ok
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    got_shown = got if len(str(got)) <= 80 else f"[{len(got)} levels]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} -> {got_shown}")

print(f"{passed}/{len(tests)} passed")
