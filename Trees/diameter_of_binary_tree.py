# Diameter of Binary Tree
# Easy
# Topics
# Company Tags
# Hints

# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

# The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

# Given the root of a binary tree root, return the diameter of the tree.

# Example 1:

# Input: root = [1,null,2,3,4,5]

# Output: 3

# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

# Example 2:

# Input: root = [1,2,3]

# Output: 2

# Constraints:

# 1 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100



# Topics

# Tree Depth-First Search Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the tree.



# Hint 1

# The diameter of a binary tree is the maximum among the sums of the left height and right height of the nodes in the tree. Why?



# Hint 2

# Because the diameter of a binary tree is defined as the longest path between any two nodes in the tree. The path may or may not pass through the root. For any given node, the longest path that passes through it is the sum of the height of its left subtree and the height of its right subtree.



# Hint 3

# A brute force solution would be to go through every node in the tree and compute its left height and right height, returning the maximum diameter found. This would be an O(n^2) solution. Can you think of a better way? Maybe we can compute the diameter as we calculate the height of the tree? Think about what information you need from each subtree during a single traversal.



# Hint 4

# We can use the Depth First Search (DFS) algorithm to calculate the height of the tree. At each node, the subtrees return their respective heights (leftHeight and rightHeight). Then we calculate the diameter at that node as d = leftHeight + rightHeight. We use a global variable to update the maximum diameter as needed during the traversal.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 72.6%

from typing import Optional
from utils.tree import TreeNode, build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def using_bottom_up_recursion(self, root: Optional[TreeNode]) -> int:
        best = 0
        def depth(node):
            if not node:
                return 0

            nonlocal best
            left = depth(node.left)
            right = depth(node.right)
            best = max(left+right, best)

            return 1 + max(left, right)
        

        depth(root)
        return best

    # I didn't write this. It was copied
    def using_iterative_dfs(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                mp[node] = (1 + max(leftHeight, rightHeight),
                           max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]


    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        return self.using_bottom_up_recursion(root)


sol = Solution()

# run from the repo root: python3 -m Trees.diameter_of_binary_tree
# (input, expected) - input is in LeetCode level-order form, None means "no node here"
# expected is the number of EDGES on the longest path between any two nodes
left_chain_100 = [0] + [x for v in range(1, 100) for x in (v, None)]   # 0 -> 1 -> 2 ... all left children
right_chain_100 = [0] + [x for v in range(1, 100) for x in (None, v)]  # same chain, all right children

tests = [
    ([1,None,2,3,4,5], 3),                          # example 1, longest path (5-3-2-4) skips the root
    ([1,2,3], 2),                                   # example 2, path bends at the root (2-1-3)
    ([1], 0),                                       # single node, no edges
    ([1,2], 1),                                     # two nodes
    ([1,None,2], 1),                                # two nodes, right side
    ([1,2,3,4,5], 3),                               # 4-2-1-3
    ([1,2,3,4,None,None,None,5], 4),                # deep left side plus the right child: 5-4-2-1-3
    ([1,2,3,4,5,6,7], 4),                           # perfect tree, leaf to leaf through the root
    ([1,2,None,3,4,5,None,None,6,7,None,None,8], 6),# longest path (7-5-3-2-4-6-8) is all under 2, root is off to the side
    ([1,2,None,None,3,None,4], 3),                  # zigzag chain, the path is the whole chain
    ([5,5,5,5,5], 3),                               # all values equal
    ([-100,-100,100], 2),                           # negatives and value limits
    (list(range(63)), 10),                          # perfect tree, 63 nodes, 5 edges down each side
    (list(range(100)), 12),                         # complete tree, 100 nodes (max size)
    (left_chain_100, 99),                           # 100 nodes, all left, path is the whole chain
    (right_chain_100, 99),                          # 100 nodes, all right
]

passed = 0
for vals, expected in tests:
    got = sol.diameter_of_binary_tree(build_tree(vals))
    status = "PASS" if got == expected else "FAIL"
    passed += got == expected
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    print(f"{status}  {shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
