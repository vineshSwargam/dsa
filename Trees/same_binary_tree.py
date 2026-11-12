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


# Definition for a binary tree node.
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

    def recursive(self, p, q):
        def check_node(a, b):
            if a.val != b.val or a.left != b.left or a.right != b.right:
                return False
            
            return check_node(a.left, b.left) and check_node(a.right, b.right)
        
        return check_node(p, q)

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.using_recursive(p, q)


sol = Solution()
p, q = [1,2,3], [1,2,3] # Output true
# p, q = [4,7], [4,null,7] # Output false
# p, q = [1,2,3], [1,3,2] # Output false



print(sol.is_same_tree(p, q))
