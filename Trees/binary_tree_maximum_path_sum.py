# Binary Tree Maximum Path Sum
# Hard
# Topics
# Company Tags
# Hints

# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.

# Example 1:

# Input: root = [1,2,3]

# Output: 6

# Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

# Example 2:

# Input: root = [-15,10,20,null,null,15,5,-5]

# Output: 40

# Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

# Constraints:

# 1 <= The number of nodes in the tree <= 30000.
# -1000 <= Node.val <= 1000



# Topics

# Dynamic Programming Tree Depth-First Search Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.



# Hint 1

# A brute force solution would involve checking the path sum between every pair of nodes in the tree, leading to an O(n^2) time complexity. Can you think of a more efficient approach? Consider what information you would need at each node to calculate the path sum if it passes through the current node.



# Hint 2

# At a node, there are three scenarios to compute the maximum path sum that includes the current node. One includes both the left and right subtrees, with the current node as the connecting node. Another path sum includes only one of the subtrees (either left or right), but not both. Another considers the path sum extending from the current node to the parent. However, the parent’s contribution is computed during the traversal at the parent node. Can you implement this?



# Hint 3

# We can use the Depth First Search (DFS) algorithm to traverse the tree. We maintain a global variable to track the maximum path sum. At each node, we first calculate the maximum path sum from the left and right subtrees by traversing them. After that, we compute the maximum path sum at the current node. This approach follows a post-order traversal, where we visit the subtrees before processing the current node.



# Hint 4

# We return the maximum path sum from the current node to its parent, considering only one of the subtrees (either left or right) to extend the path. While calculating the left and right subtree path sums, we also ensure that we take the maximum with 0 to avoid negative sums, indicating that we should not include the subtree path in the calculation of the maximum path at the current node.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 48.9%


from typing import Optional
from utils.tree import TreeNode, build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        pass

    # bottom up recursion
    def find_max_path_sum(self, root):
        m_sum = float('-inf')

        def path_sum(r):
            nonlocal m_sum
            if not r:
                return 0
        
            left = path_sum(r.left)
            right = path_sum(r.right)
            lsum = left if left > 0 else 0
            rsum = right if right > 0 else 0

            m_sum = max(r.val+lsum+rsum, m_sum)

            return r.val + max(lsum, rsum)
        
        # path_sum(root)
        # return m_sum

        def iter_dfs(r):
            st = [r] if r else [] # st is stack
            res = float('-inf')
            smap = { None: (0, float('-inf')) }

            while st:
                node = st[-1] # peek don't pop

                if node.left not in smap and node.left: 
                    st.append(node.left)
                elif node.right not in smap and node.right:
                    st.append(node.right)
                else:
                    pn = st.pop() # pn is popped node

                    lsum, lbendsum = smap[pn.left]
                    rsum, rbendsum = smap[pn.right]

                    lsum = lsum if lsum > 0 else 0
                    rsum = rsum if rsum > 0 else 0


                    smap[pn] = (
                            pn.val + max(lsum, rsum),
                            max(pn.val + lsum + rsum, lbendsum, rbendsum)
                        )
            
            return smap[r][1]

        return iter_dfs(root)
        

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        return self.find_max_path_sum(root)


sol = Solution()

# run from the repo root: python3 -m Trees.binary_tree_maximum_path_sum
# (root, expected) - root in LeetCode level-order form
N = 30000
left_chain_max = [1000] + [x for _ in range(N - 1) for x in (1000, None)]      # 30k deep, every node 1000: the whole chain
right_chain_min = [-1000] + [x for _ in range(N - 1) for x in (None, -1000)]   # 30k deep, every node -1000: best is one node
complete_ones = [1] * N                                                         # 30k nodes, height 14: deepest left leaf to deepest right leaf

tests = [
    ([1,2,3], 6),                                       # example 1, path bends at the root
    ([-15,10,20,None,None,15,5,-5], 40),                # example 2, best path skips the root
    ([-3], -3),                                         # single negative node, the answer can be negative
    ([0], 0),                                           # single zero
    ([-1,-2,-3], -1),                                   # all negative, best is the single largest node
    ([2,-1], 2),                                        # negative child, leave it out
    ([-2,1], 1),                                        # child alone beats anything with the root
    ([1,-2,3], 4),                                      # drop the negative side, keep root + good side
    ([-10,9,20,None,None,15,7], 42),                    # classic: 15 -> 20 -> 7, root not used
    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 48),    # long bent path: 7 -> 11 -> 4 -> 5 -> 8 -> 13
    ([10,2,10,20,1,None,-25,None,None,None,None,3,4], 42),   # 20 -> 2 -> 10 -> 10, the -25 branch is dropped
    ([-100,5,6,3,4], 12),                               # best path is entirely inside the left subtree
    ([10,-5,None,20], 25),                              # worth crossing a negative node: 20 + -5 + 10
    ([10,-50,None,20], 20),                             # not worth crossing it: 20 alone
    ([1,2,3,4,None,None,5], 15),                        # both arms are two nodes long: 4 -> 2 -> 1 -> 3 -> 5
    ([1000,1000,1000], 3000),                           # value limits, positive
    ([-1000,-1000,-1000], -1000),                       # value limits, negative
    (left_chain_max, 1000 * N),                         # 30k deep, too deep for plain recursion
    (right_chain_min, -1000),                           # 30k deep, all negative
    (complete_ones, 29),                                # 15 nodes down each side, root counted once
]

passed = 0
for vals, expected in tests:
    try:
        got = sol.max_path_sum(build_tree(vals))
    except RecursionError:
        got = 'ERROR (too deep for recursion)'
    ok = got == expected
    passed += ok
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
