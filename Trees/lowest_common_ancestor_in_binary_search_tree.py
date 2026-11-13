# Lowest Common Ancestor in Binary Search Tree
# Medium
# Topics
# Company Tags
# Hints

# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q are descendants. The ancestor is allowed to be a descendant of itself.




# Example 1:

# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

# Output: 5



# Example 2:

# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

# Output: 3

# Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.




# Constraints:

# 2 <= The number of nodes in the tree <= 100.
# -100 <= Node.val <= 100
# p != q
# p and q will both exist in the BST.



# Topics

# Tree Depth-First Search Binary Search Tree Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution as good or better than O(h) time and O(h) space, where h is the height of the given tree.



# Hint 1

# A Binary Search Tree (BST) is a tree in which the values of all nodes in the left subtree of a node are less than the node's value, and the values of all nodes in the right subtree are greater than the node's value. Additionally, every subtree of a BST must also satisfy this property, meaning the "less than" or "greater than" condition is valid for all nodes in the tree, not just the root. How can you use this idea to find the LCA of the given nodes in the tree?



# Hint 2

# We can use recursion to traverse the tree. Can you figure out the conditions we encounter when choosing a path between the left and right subtrees during traversal using the values of the two given nodes? Perhaps you can determine the LCA by traversing based on these conditions.



# Hint 3

# If nodes p and q are in different subtrees, a split occurs, making the current node the LCA. If both are in the left or right subtree, the LCA lies in that subtree and we further choose that subtree to traverse using recursion. You should also handle other multiple scenarios to get the LCA.



# Hint 4

# The LCA can also be one of the nodes, p or q, if the current node is equal to either of them. This is because if we encounter either p or q during the traversal, that node is the LCA.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 73.8%


from typing import Optional
from utils.tree import TreeNode, build_tree, find_node, bst_level_order

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


sol = Solution()

# run from the repo root: python3 -m Trees.lowest_common_ancestor_in_binary_search_tree
# (root, p, q, expected) - root in LeetCode level-order form; p, q and expected are node VALUES
# p and q are looked up as real nodes in the tree before calling, the way LeetCode passes them,
# and the answer must be the actual node from the tree (checked with "is"), not just a node with the right value
ex = [5,3,8,1,4,7,9,None,2]
#          5
#        /   \
#       3     8
#      / \   / \
#     1   4 7   9
#      \
#       2
balanced_1_to_100 = bst_level_order(list(range(1, 101)))                  # 100 nodes, height 7, root is 50
desc_left_chain = [100] + [x for v in range(99, 0, -1) for x in (v, None)] # 100 -> 99 -> ... -> 1, all left children
asc_right_chain = [1] + [x for v in range(2, 101) for x in (None, v)]      # 1 -> 2 -> ... -> 100, all right children

tests = [
    (ex, 3, 8, 5),                          # example 1, split at the root
    (ex, 3, 4, 3),                          # example 2, p is the ancestor of q
    (ex, 8, 3, 5),                          # example 1 with p and q swapped
    (ex, 4, 3, 3),                          # example 2 with p and q swapped
    (ex, 2, 4, 3),                          # split one level down, on the left
    (ex, 7, 9, 8),                          # split one level down, on the right
    (ex, 1, 2, 1),                          # q is p's direct child
    (ex, 2, 9, 5),                          # deepest left node vs a right leaf
    (ex, 5, 2, 5),                          # p is the root itself
    (ex, 2, 3, 3),                          # deep node and its grandparent
    ([2,1], 2, 1, 2),                       # two nodes, root and left child
    ([1,None,2], 1, 2, 1),                  # two nodes, root and right child
    ([0,-100,100], -100, 100, 0),           # value limits, split at the root
    ([-50,-100,0,None,None,-25,100], -25, 100, 0),   # all negatives on one side, split below the root
    (balanced_1_to_100, 1, 100, 50),        # smallest and largest, split at the root
    (balanced_1_to_100, 24, 26, 25),        # neighbours that split at 25
    (balanced_1_to_100, 99, 100, 99),       # neighbours where one is the parent
    (balanced_1_to_100, 37, 38, 37),        # neighbours deep in the tree
    (desc_left_chain, 1, 2, 2),             # 100-deep left chain, answer at the very bottom
    (desc_left_chain, 1, 100, 100),         # left chain, answer is the root
    (asc_right_chain, 99, 100, 99),         # 100-deep right chain, answer near the bottom
    (asc_right_chain, 50, 51, 50),          # right chain, answer in the middle
]

passed = 0
for vals, p_val, q_val, expected in tests:
    root = build_tree(vals)
    got = sol.lowest_common_ancestor(root, find_node(root, p_val), find_node(root, q_val))
    ok = got is find_node(root, expected)
    passed += ok
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} p={p_val} q={q_val} -> {got.val if got else None}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
