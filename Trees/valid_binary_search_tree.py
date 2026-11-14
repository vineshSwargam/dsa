# Valid Binary Search Tree
# Medium
# Topics
# Company Tags
# Hints

# Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

# A valid binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

# Example 1:

# Input: root = [2,1,3]

# Output: true

# Example 2:

# Input: root = [1,2,3]

# Output: false

# Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

# Constraints:

# 1 <= The number of nodes in the tree <= 10000.
# -1000000000 <= Node.val <= 1000000000



# Topics

# Tree Depth-First Search Binary Search Tree Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.



# Hint 1

# A brute force solution would involve traversing the tree and, for every node, checking its entire left subtree to ensure all nodes are less than the current node, and its entire right subtree to ensure all nodes are greater. This results in an O(n^2) solution. Can you think of a better way? Maybe tracking values during the traversal would help.



# Hint 2

# We can use the Depth First Search (DFS) algorithm to traverse the tree. At each node, we need to ensure that the tree rooted at that node is a valid Binary Search Tree (BST). One way to do this is by tracking an interval that defines the lower and upper limits for the node's value in that subtree. This interval will be updated as we move down the tree, ensuring each node adheres to the BST property.



# Hint 3

# We start with the interval [-infinity, infinity] for the root node. As we traverse the tree, when checking the left subtree, we update the maximum value limit because all values in the left subtree must be less than the current node's value. Conversely, when checking the right subtree, we update the minimum value limit because all values in the right subtree must be greater than the current node's value.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 43.6%


from typing import Optional
from utils.tree import TreeNode, build_tree, bst_level_order

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:


sol = Solution()

# run from the repo root: python3 -m Trees.valid_binary_search_tree
# (root, expected) - root in LeetCode level-order form
N = 10000
balanced_valid = bst_level_order(list(range(1, N + 1)))                     # 10k nodes, height 14, valid
swapped = list(range(1, N + 1)); swapped[5000], swapped[5001] = swapped[5001], swapped[5000]
balanced_one_swap = bst_level_order(swapped)                                # same shape, two neighbouring values swapped deep inside
asc_right_chain = [1] + [x for v in range(2, N + 1) for x in (None, v)]     # 1 -> 2 -> ... -> 10000, all right children, valid
desc_left_chain = [N] + [x for v in range(N - 1, 0, -1) for x in (v, None)] # 10000 -> ... -> 1, all left children, valid
asc_right_chain_bad_end = asc_right_chain[:-1] + [0]                        # same right chain, but the very last node is 0

tests = [
    ([2,1,3], True),                                # example 1
    ([1,2,3], False),                               # example 2, left child bigger than the root
    ([1], True),                                    # single node
    ([1,1], False),                                 # duplicate on the left, must be strictly less
    ([1,None,1], False),                            # duplicate on the right, must be strictly greater
    ([2,2,2], False),                               # all duplicates
    ([5,1,4,None,None,3,6], False),                 # right child smaller than the root
    ([5,4,6,None,None,3,7], False),                 # 3 is fine under its parent 6, but it is in 5's right subtree
    ([10,5,15,None,None,6,20], False),              # same trap: 6 < 15 but 6 < 10 too
    ([3,1,5,0,4], False),                           # mirror trap: 4 > 1 but it is in 3's left subtree
    ([32,26,47,19,None,None,56,None,27], False),    # 27 > 19 but it is in 26's left subtree
    ([3,1,5,0,2,4,6], True),                        # full valid tree
    ([5,3,8,1,4,7,9,None,2], True),                 # valid with a deep inner node (2 sits between 1 and 3)
    ([2,1,3,None,None,None,4], True),               # valid, one-sided deeper level
    ([0,-1000000000,1000000000], True),             # value limits: a fake -1e9 / 1e9 starting bound would break this
    ([1000000000,-1000000000], True),               # root at the max limit
    ([-1000000000,None,1000000000], True),          # root at the min limit
    (balanced_valid, True),                         # max size, valid
    (balanced_one_swap, False),                     # max size, one hidden swap
    (asc_right_chain, True),                        # 10k deep right chain, too deep for plain recursion
    (desc_left_chain, True),                        # 10k deep left chain
    (asc_right_chain_bad_end, False),               # 10k deep, broken only at the very bottom
]

passed = 0
for vals, expected in tests:
    try:
        got = sol.is_valid_bst(build_tree(vals))
    except RecursionError:
        got = 'ERROR (too deep for recursion)'
    ok = got == expected
    passed += ok
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
