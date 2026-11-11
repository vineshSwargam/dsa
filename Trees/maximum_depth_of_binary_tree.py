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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        st = [root] if root else [] # stack for dfs
        visited = set()
        depth = 1 if root else 0
        max_d = depth

        while st:
            cur = st.pop()

            if cur in visited:
                continue
            
            visited.add(cur)

            if cur.left:
                st.append(cur.left)

            if cur.right:
                st.append(cur.right)
            
            if not cur.right and not cur.left:
                max_d = max(depth, max_d)
                depth =0
            
            depth += 1

        return max_d


sol = Solution()
root = [1,2,3,null,null,4] # Output 3
# root = [] # Output 0



print(sol.max_depth(root))
