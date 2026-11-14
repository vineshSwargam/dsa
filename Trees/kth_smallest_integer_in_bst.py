# Kth Smallest Integer in BST
# Medium
# Topics
# Company Tags
# Hints

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

# A binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.



# Example 1:

# Input: root = [2,1,3], k = 1

# Output: 1



# Example 2:

# Input: root = [4,3,5,2,null], k = 4

# Output: 5



# Constraints:

# 1 <= k <= The number of nodes in the tree <= 10,000.
# 0 <= Node.val <= 10,000



# Topics

# Tree Depth-First Search Binary Search Tree Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the number of nodes in the given tree.



# Hint 1

# A naive solution would be to store the node values in an array, sort it, and then return the k-th value from the sorted array. This would be an O(nlogn) solution due to sorting. Can you think of a better way? Maybe you should try one of the traversal technique.



# Hint 2

# We can use the Depth First Search (DFS) algorithm to traverse the tree. Since the tree is a Binary Search Tree (BST), we can leverage its structure and perform an in-order traversal, where we first visit the left subtree, then the current node, and finally the right subtree. Why? Because we need the k-th smallest integer, and by visiting the left subtree first, we ensure that we encounter smaller nodes before the current node. How can you implement this?



# Hint 3

# We keep a counter variable cnt to track the position of the current node in the ascending order of values. When cnt == k, we store the current node's value in a global variable and return. This allows us to identify and return the k-th smallest element during the in-order traversal.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 82.3%


from typing import Optional
from utils.tree import TreeNode, build_tree, bst_level_order

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:


sol = Solution()

# run from the repo root: python3 -m Trees.kth_smallest_integer_in_bst
# (root, k, expected) - root in LeetCode level-order form
N = 10000
balanced = bst_level_order(list(range(N)))                                  # values 0..9999, height 14
asc_right_chain = [0] + [x for v in range(1, N) for x in (None, v)]         # 0 -> 1 -> ... -> 9999, all right children
desc_left_chain = [N - 1] + [x for v in range(N - 2, -1, -1) for x in (v, None)]   # 9999 -> ... -> 0, all left children
ex = [5,3,8,1,4,7,9,None,2]                                                 # sorted order: 1 2 3 4 5 7 8 9
#          5
#        /   \
#       3     8
#      / \   / \
#     1   4 7   9
#      \
#       2

tests = [
    ([2,1,3], 1, 1),                        # example 1
    ([4,3,5,2,None], 4, 5),                 # example 2
    ([1], 1, 1),                            # single node
    ([2,1,3], 2, 2),                        # k lands on the root
    ([2,1,3], 3, 3),                        # k is the largest
    ([3,1,4,None,2], 1, 1),                 # smallest is not the deepest node
    ([3,1,4,None,2], 2, 2),                 # 2 is the right child of the smallest
    ([3,1,4,None,2], 4, 4),                 # largest
    ([5,3,6,2,4,None,None,1], 3, 3),        # inner node of the left subtree
    ([5,3,6,2,4,None,None,1], 6, 6),        # only node on the right
    (ex, 2, 2),                             # inner node hanging right of the smallest
    (ex, 5, 5),                             # the root, middle of the order
    (ex, 6, 7),                             # first node of the right subtree
    (ex, 8, 9),                             # last node
    ([0,None,10000], 2, 10000),             # value limits
    ([10000,0], 1, 0),                      # value limits, other way round
    (balanced, 1, 0),                       # max size, smallest
    (balanced, N, N - 1),                   # max size, largest (whole tree must be visited)
    (balanced, 5000, 4999),                 # max size, middle
    (asc_right_chain, N, N - 1),            # 10k deep right chain, answer at the bottom
    (desc_left_chain, 1, 0),                # 10k deep left chain, smallest at the bottom
    (desc_left_chain, N, N - 1),            # 10k deep left chain, answer is the root
]

passed = 0
for vals, k, expected in tests:
    try:
        got = sol.kth_smallest(build_tree(vals), k)
    except RecursionError:
        got = 'ERROR (too deep for recursion)'
    ok = got == expected
    passed += ok
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} k={k} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
