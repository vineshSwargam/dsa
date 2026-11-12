# Same Binary Tree
# Easy
# Topics
# Company Tags
# Hints

# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]

# Output: true

# Example 2:

# Input: p = [4,7], q = [4,null,7]

# Output: false

# Example 3:

# Input: p = [1,2,3], q = [1,3,2]

# Output: false

# Constraints:

# 0 <= The number of nodes in both trees <= 100.
# -100 <= Node.val <= 100



# Topics

# Tree Depth-First Search Breadth-First Search Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the tree.



# Hint 1

# Can you think of an algorithm that is used to traverse the tree? Maybe in terms of recursion.



# Hint 2

# We can use the Depth First Search (DFS) algorithm to traverse the tree. Can you think of a way to simultaneously traverse both the trees?



# Hint 3

# We traverse both trees starting from their root nodes. At each step in the recursion, we check if the current nodes in both trees are either null or have the same value. If one node is null while the other is not, or if their values differ, we return false. If the values match, we recursively check their left and right subtrees. If any recursive call returns false, the result for the current recursive call is false.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 77.0%


from typing import Optional
from utils.tree import TreeNode, build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
#                   1
#                    \
#                     2
#                    / \
#                   3   4
#                   /
#                   5

    def using_recursive(self, p, q):
        def check_node(a, b):
            if a.val != b.val or a.left != b.left or a.right != b.right:
                return False
            
            return check_node(a.left, b.left) and check_node(a.right, b.right)
        
        return check_node(p, q)

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.using_recursive(p, q)


sol = Solution()

# run from the repo root: python3 -m Trees.same_binary_tree
# (p, q, expected) - both trees in LeetCode level-order form, None means "no node here"
# p and q are always built as separate trees, so no node is ever shared between them
full_100 = list(range(100))                                             # complete tree, 100 nodes
full_100_last_changed = list(range(99)) + [-1]                          # same, except the very last node
left_chain_100 = [0] + [x for v in range(1, 100) for x in (v, None)]   # 0 -> 1 -> 2 ... all left children
right_chain_100 = [0] + [x for v in range(1, 100) for x in (None, v)]  # same values, all right children

tests = [
    ([1,2,3], [1,2,3], True),                       # example 1
    # ([4,7], [4,None,7], False),                     # example 2, same values, child on the other side
    # ([1,2,3], [1,3,2], False),                      # example 3, children swapped
    # ([], [], True),                                 # both empty
    # ([1], [], False),                               # only q is empty
    # ([], [1], False),                               # only p is empty
    # ([1], [1], True),                               # single node, same
    # ([1], [2], False),                              # single node, different value
    # ([0,0], [0], False),                            # value 0 vs missing node, catches "if node.val" bugs
    # ([1,1], [1,None,1], False),                     # all values equal, only the shape differs
    # ([2,1], [1,None,2], False),                     # same values, different root
    # ([1,2,3,4,5,6,7], [1,2,3,4,5,6,7], True),       # perfect tree, same
    # ([1,2,3,4,5,6,7], [1,2,3,4,5,6,8], False),      # differs only at the last leaf
    # ([1,2,3,4], [1,2,3,4,5], False),                # q has one extra node deep down
    # ([1,2,3,4,5], [1,2,3,4], False),                # p has one extra node deep down
    # ([5,5,5,5,5], [5,5,5,5,5], True),               # duplicates, same shape
    # ([-100,0,100], [-100,0,100], True),             # negatives and value limits, same
    # ([-100,0,100], [100,0,-100], False),            # value limits swapped
    # (full_100, full_100, True),                     # 100 nodes each, same
    # (full_100, full_100_last_changed, False),       # 100 nodes, only the last value differs
    # (left_chain_100, left_chain_100, True),         # 100-node chain, same
    # (left_chain_100, right_chain_100, False),       # same values, mirrored chain
]

passed = 0
for p_vals, q_vals, expected in tests:
    got = sol.is_same_tree(build_tree(p_vals), build_tree(q_vals))
    status = "PASS" if got == expected else "FAIL"
    passed += got == expected
    shown = f"p={p_vals} q={q_vals}" if len(p_vals) + len(q_vals) <= 24 else f"p=[{len(p_vals)} values] q=[{len(q_vals)} values]"
    print(f"{status}  {shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
