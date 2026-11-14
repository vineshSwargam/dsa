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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:


sol = Solution()
root, k = [2,1,3], 1 # Output 1
# root, k = [4,3,5,2,null], 4 # Output 5



print(sol.kth_smallest(root, k))
