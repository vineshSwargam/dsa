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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


sol = Solution()
root, subRoot = [1,2,3,4,5], [2,4,5] # Output true
# root, subRoot = [1,2,3,4,5,null,null,6], [2,4,5] # Output false



print(sol.is_subtree(root, subRoot))
