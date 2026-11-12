# Balanced Binary Tree
# Easy
# Topics
# Company Tags
# Hints

# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:

# Input: root = [1,2,3,null,null,4]

# Output: true

# Example 2:

# Input: root = [1,2,3,null,null,4,null,5]

# Output: false

# Example 3:

# Input: root = []

# Output: true

# Constraints:

# The number of nodes in the tree is in the range [0, 1000].
# -1000 <= Node.val <= 1000



# Topics

# Tree Depth-First Search Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the tree.



# Hint 1

# A brute force solution would involve traversing every node and checking whether the tree rooted at each node is balanced by computing the heights of its left and right subtrees. This approach would result in an O(n^2) solution. Can you think of a more efficient way? Perhaps you could avoid repeatedly computing the heights for every node by determining balance and height in a single traversal.



# Hint 2

# We can use the Depth First Search (DFS) algorithm to compute the heights at each node. While calculating the heights of the left and right subtrees, we also check if the tree rooted at the current node is balanced. If leftHeight - rightHeight > 1, we update a global variable, such as isBalanced = False. After traversing all the nodes, the value of isBalanced indicates whether the entire tree is balanced or not.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 66.2%


from typing import Optional
from utils.tree import TreeNode, build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def using_recursive_dfs(self, root):
        is_valid = True

        def depth(node):
            if not node:
                return 0
            nonlocal is_valid
            ld = depth(node.left) # ld = left depth
            rd = depth(node.right) # rd = right depth
            if not -1 <= ld-rd <= 1:
                is_valid = False

            return 1 + max(ld, rd)

        depth(root)
        return is_valid

#                   1
#                    \
#                     2
#                    / \
#                   3   4
#                   /
#                   5

#                 1
#                /
#               2
#              / \
#             3   4
#            /     \
#           5       6
#          /         \
#         7           8

    def using_iterative_dfs(self, root):
        st = [root] if root else [] # stack
        dmap = { None: 0 } # dmap = depth map of nodes

        while st and is_valid:
            node = st[-1]

            if node.left and node.left not in dmap:
                st.append(node.left)
            elif node.right and node.right not in dmap:
                st.append(node.right)
            else:
                node = st.pop()

                ld = dmap[node.left]
                rd = dmap[node.right]

                if not -1 <= ld-rd <= 1:
                    return False

                dmap[node] = 1+max(ld, rd)

        return True            


    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        # return self.using_recursive_dfs(root)
        return self.using_iterative_dfs(root)


sol = Solution()

# run from the repo root: python3 -m Trees.balanced_binary_tree
# (input, expected) - input is in LeetCode level-order form, None means "no node here"
left_chain_1000 = [0] + [x for v in range(1, 1000) for x in (v, None)]   # 1000 nodes, all left children

tests = [
    ([1,2,3,None,None,4], True),                    # example 1
    ([1,2,3,None,None,4,None,5], False),            # example 2
    ([], True),                                     # example 3, empty tree
    ([1], True),                                    # single node
    ([1,2], True),                                  # one child, heights 1 and 0 differ by exactly 1
    ([1,None,2], True),                             # same, right side
    ([1,2,None,3], False),                          # left chain of 3, root's sides are 2 and 0
    ([1,None,2,None,3], False),                     # right chain of 3
    ([1,2,3,4,5,6,7], True),                        # perfect tree
    ([3,9,20,None,None,15,7], True),                # right side one level deeper
    ([1,2,2,3,3,None,None,4,4], False),             # left side two levels deeper than the right
    ([1,2,3,4,None,5,6,7,None,8], False),           # root looks fine (3 vs 3) but node 2 is off by 2 underneath
    ([1,2,3,4,5,6,None,7], True),                   # off by one at several nodes, still balanced
    ([1,2,3,4,None,None,5], True),                  # V shape, each side a chain of 2
    ([1,2,3,4,None,None,5,6,None,None,7], False),   # V shape, each side a chain of 3
    ([5,5,5,5], True),                              # all values equal
    ([-1000,1000,-1000,None,0], True),              # negatives and value limits
    (list(range(1000)), True),                      # complete tree, 1000 nodes (max size)
    (left_chain_1000, False),                       # 1000 nodes in a chain, max depth
]

passed = 0
for vals, expected in tests:
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    try:
        got = sol.is_balanced(build_tree(vals))
    except RecursionError:
        print(f"ERROR {shown} -> RecursionError (too deep for Python's default limit)  expected {expected}")
        continue
    status = "PASS" if got == expected else "FAIL"
    passed += got == expected
    print(f"{status}  {shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
