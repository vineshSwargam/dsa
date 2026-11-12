# Maximum Depth of Binary Tree
# Easy
# Topics
# Company Tags
# Hints

# Given the root of a binary tree, return its depth.

# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:

# Input: root = [1,2,3,null,null,4]

# Output: 3

# Example 2:

# Input: root = []

# Output: 0

# Constraints:

# 0 <= The number of nodes in the tree <= 100.
# -100 <= Node.val <= 100



# Topics

# Tree Depth-First Search Breadth-First Search Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the tree.



# Hint 1

# From the definition of binary tree's maximum depth, Can you think of a way to achieve this recursively? Maybe you should consider the max depth of the subtrees first before computing the maxdepth at the root.



# Hint 2

# We use the Depth First Search (DFS) algorithm to find the maximum depth of a binary tree, starting from the root. For the subtrees rooted at the left and right children of the root node, we calculate their maximum depths recursively going through left and right subtrees. We return 1 + max(leftDepth, rightDepth). Why?



# Hint 3

# The +1 accounts for the current node, as it contributes to the current depth in the recursion call. We pass the maximum depth from the current node's left and right subtrees to its parent because the current maximum depth determines the longest path from the parent to a leaf node through this subtree.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 84.4%


from typing import Optional
from utils.tree import TreeNode, build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def using_tuples(self, root: Optional[TreeNode]) -> int:
        st = [(root, 1)] if root else [] # stack for dfs
        visited = set()
        max_d = 0

        while st:
            node, dep = st.pop()

            if node in visited:
                continue
            
            visited.add(node)

            if node.left:
                st.append((node.left, dep+1))

            if node.right:
                st.append((node.right, dep+1))
            
            if not node.right and not node.left:
                max_d = max(dep, max_d)


        return max_d


    # top down recursion
    def using_recursion(self, root: Optional[TreeNode]) -> int:
        def depth(node, dep):
            if not node.left and not node.right:
                return dep
            
            max_l = depth(node.left, dep+1) if node.left else dep
            max_r = depth(node.right, dep+1) if node.right else dep
            return max(max_l, max_r)
        
        if not root:
            return 0
        return depth(root, 1)

    # bottom up recursion
    def using_bottom_up_recursion(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        
        return depth(root)



    def max_depth(self, root: Optional[TreeNode]) -> int:
        # return self.using_tuples(root)
        # return self.using_recursion(root)
        return self.using_bottom_up_recursion(root)
        


sol = Solution()

# run from the repo root: python3 -m Trees.maximum_depth_of_binary_tree
# (input, expected) - input is in LeetCode level-order form, None means "no node here"
left_chain_100 = [0] + [x for v in range(1, 100) for x in (v, None)]   # 0 -> 1 -> 2 ... all left children
right_chain_100 = [0] + [x for v in range(1, 100) for x in (None, v)]  # same chain, all right children

tests = [
    ([1,2,3,4,5], 3),                               # example 1
    ([1,2,3,None,None,4], 3),                       # example 1
    ([], 0),                                        # example 2, empty tree
    ([1], 1),                                       # single node
    ([1,2], 2),                                     # only a left child
    ([1,None,2], 2),                                # only a right child
    ([3,9,20,None,None,15,7], 3),                   # shallow left leaf, deeper right side
    ([1,2,3,4,5,6,7], 3),                           # perfect tree, every leaf at the same depth
    ([1,2,3,4,None,None,None,5], 4),                # deepest path is on the left
    ([1,2,3,None,None,4,None,5], 4),                # deepest path is on the right, after a shallow left leaf
    ([1,2,3,4,5,None,None,None,None,6,None,7], 5),  # a shallow leaf (4) comes before a deeper sibling (5 -> 6 -> 7)
    ([1,2,None,None,3,None,4], 4),                  # zigzag: left, right, right
    ([1,2,3,4,None,None,5,6,None,None,7], 4),       # two deep paths on opposite sides, same depth
    ([5,5,5,5,5], 3),                               # all values equal
    ([-100,-100,None,100], 3),                      # negatives and value limits
    (list(range(63)), 6),                           # perfect tree, 63 nodes
    (list(range(100)), 7),                          # complete tree, 100 nodes (max size)
    (left_chain_100, 100),                          # 100 nodes, all left, max depth
    (right_chain_100, 100),                         # 100 nodes, all right, max depth
]

passed = 0
for vals, expected in tests:
    got = sol.max_depth(build_tree(vals))
    status = "PASS" if got == expected else "FAIL"
    passed += got == expected
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    print(f"{status}  {shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
