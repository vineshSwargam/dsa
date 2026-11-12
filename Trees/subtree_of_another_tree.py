# Subtree of Another Tree
# Easy
# Topics
# Company Tags
# Hints

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.




# Example 1:

# Input: root = [1,2,3,4,5], subRoot = [2,4,5]

# Output: true



# Example 2:

# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

# Output: false



# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4



# Topics

# Tree Depth-First Search String Matching Binary Tree Hash Function


# Recommended Time & Space Complexity

# You should aim for a solution as good or better than O(m * n) time and O(m + n) space, where n and m are the number of nodes in root and subRoot, respectively.



# Hint 1

# A subtree of a tree is a tree rooted at a specific node. We need to check whether the given subRoot is identical to any of the subtrees of root. Can you think of a recursive way to check this? Maybe you can leverage the idea of solving a problem where two trees are given, and you need to check whether they are identical in structure and values.



# Hint 2

# When two trees are identical, it means that every node in both trees has the same value and structure. We can use the Depth First Search (DFS) algorithm to solve the problem. How do you implement this?



# Hint 3

# We traverse the given root, and at each node, we check if the subtree rooted at that node is identical to the given subRoot. We use a helper function, sameTree(root1, root2), to determine whether the two trees passed to it are identical in both structure and values.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 54.6%


from typing import Optional
from utils.tree import TreeNode, build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


sol = Solution()

# run from the repo root: python3 -m Trees.subtree_of_another_tree
# (root, subRoot, expected) - both trees in LeetCode level-order form, None means "no node here"
def left_chain(vals):
    """[a, b, c] -> a with left child b with left child c, in level-order form"""
    return vals[:1] + [x for v in vals[1:] for x in (v, None)]

chain_0_to_1999 = left_chain(list(range(2000)))                 # 2000 nodes (max root size), values 0..1999
chain_1000_to_1999 = left_chain(list(range(1000, 2000)))        # its bottom 1000 nodes
ones_2000 = left_chain([1] * 2000)                              # 2000 nodes, all 1
ones_1000 = left_chain([1] * 1000)                              # 1000 nodes, all 1
ones_999_then_2 = left_chain([1] * 999 + [2])                   # 1000 nodes, all 1 except the last

tests = [
    ([1,2,3,4,5], [2,4,5], True),                               # example 1
    ([1,2,3,4,5,None,None,6], [2,4,5], False),                  # example 2, 4 has an extra child 6 in root
    ([1], [1], True),                                           # single node, same
    ([1], [2], False),                                          # single node, different
    ([1,2,3], [1,2,3], True),                                   # the whole tree counts as its own subtree
    ([1,2], [2], True),                                         # subRoot is a leaf of root
    ([1,2], [1], False),                                        # root's 1 has a child, subRoot's 1 doesn't
    ([1], [1,2], False),                                        # subRoot bigger than root
    ([3,4,5,1,2], [4,1,2], True),                               # match on the left side
    ([3,4,5,1,2,None,None,None,None,0], [4,1,2], False),        # same, but 2 has an extra child 0
    ([1,2,3,4,5], [2,4], False),                                # subRoot matches the top of 2 but not all of it
    ([1,2,3,4], [2,None,4], False),                             # same values, 4 on the wrong side
    ([1,2,3,5,None,2,None,None,None,4], [2,4], True),           # first 2 doesn't match, the second one does
    ([1,1,1,1,1,1,1], [1,1,1], True),                           # all values equal, shape decides
    ([1,1,1,1,1,1,1], [1,1], False),                            # all equal, but no node has only a left child
    ([1,1], [1], True),                                         # duplicates, the leaf matches
    ([12], [2], False),                                         # catches string-matching bugs ("12" contains "2")
    ([-10000,10000], [10000], True),                            # value limits
    (chain_0_to_1999, chain_1000_to_1999, True),                # 2000-node root, match is the bottom 1000
    (ones_2000, ones_1000, True),                               # all 1s, only the node at depth 1000 matches
    (ones_2000, ones_999_then_2, False),                        # all 1s, every node almost matches (slowest case)
]

passed = 0
for root_vals, sub_vals, expected in tests:
    shown = f"root={root_vals} subRoot={sub_vals}" if len(root_vals) + len(sub_vals) <= 24 else f"root=[{len(root_vals)} values] subRoot=[{len(sub_vals)} values]"
    try:
        got = sol.is_subtree(build_tree(root_vals), build_tree(sub_vals))
    except RecursionError:
        print(f"ERROR {shown} -> RecursionError (too deep for Python's default limit)  expected {expected}")
        continue
    status = "PASS" if got == expected else "FAIL"
    passed += got == expected
    print(f"{status}  {shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
