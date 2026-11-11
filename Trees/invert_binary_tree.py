# Invert Binary Tree
# Easy
# Topics
# Company Tags
# Hints

# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:

# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,2,7,6,5,4]

# Example 2:

# Input: root = [3,2,1]

# Output: [3,1,2]

# Example 3:

# Input: root = []

# Output: []

# Constraints:

# 0 <= The number of nodes in the tree <= 100.
# -100 <= Node.val <= 100



# Topics

# Tree Depth-First Search Breadth-First Search Binary Tree


# Recommended Time & Space Complexity


# Hint 1


# Hint 2


# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 83.3%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


sol = Solution()
root = [1,2,3,4,5,6,7] # Output [1,3,2,7,6,5,4]
# root = [3,2,1] # Output [3,1,2]
# root = [] # Output []



print(sol.invert_tree(root))
