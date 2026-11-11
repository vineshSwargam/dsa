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


from typing import Optional
from utils.tree import TreeNode, build_tree, to_list

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root] if root else []
        visited = set()

        while q:
            cur = q.pop(0)

            if cur in visited:
                continue

            visited.add(cur)

            temp = cur.left
            cur.left = cur.right
            cur.right = temp
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        return root



sol = Solution()

# run from the repo root: python3 -m Trees.invert_binary_tree
# (input, expected) - both in LeetCode level-order form, None means "no node here"
perfect_63 = list(range(63))                                                   # 6 full levels
perfect_63_inverted = [v for d in range(6) for v in reversed(range(2**d - 1, 2**(d+1) - 1))]  # every level reversed
left_chain_100 = [0] + [x for v in range(1, 100) for x in (v, None)]          # 0 -> 1 -> 2 ... all left children
right_chain_100 = [0] + [x for v in range(1, 100) for x in (None, v)]         # same chain, all right children

tests = [
    ([1,2,3,4,5,6,7], [1,3,2,7,6,5,4]),                    # example 1
    ([3,2,1], [3,1,2]),                                    # example 2
    ([], []),                                              # example 3, empty tree
    ([1], [1]),                                            # single node
    ([1,2], [1,None,2]),                                   # only a left child, it moves to the right
    ([1,None,2], [1,2]),                                   # only a right child, it moves to the left
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),                    # classic example, full tree
    ([1,2,3,None,4,5], [1,3,2,None,5,4]),                  # gaps in the middle of a level
    ([1,2,None,None,3], [1,None,2,3]),                     # zigzag: left, then right
    ([1,2,None,3,None,4], [1,None,2,None,3,None,4]),       # left chain becomes a right chain
    ([1,None,2,None,3,None,4], [1,2,None,3,None,4]),       # right chain becomes a left chain
    ([2,2,2,3,None,None,3], [2,2,2,3,None,None,3]),        # mirror-symmetric tree, output looks the same
    ([5,5,5,5,5], [5,5,5,None,None,5,5]),                  # all values equal, only the shape shows the swap
    ([-100,100,0], [-100,0,100]),                          # negatives and value limits
    (perfect_63, perfect_63_inverted),                     # 63 nodes, every level reversed
    (left_chain_100, right_chain_100),                     # 100 nodes, max depth
]

passed = 0
for vals, expected in tests:
    got = to_list(sol.invert_tree(build_tree(vals)))
    status = "PASS" if got == expected else "FAIL"
    passed += got == expected
    if len(vals) <= 20:
        print(f"{status}  {vals} -> {got}  expected {expected}")
    else:
        print(f"{status}  [{len(vals)} values] -> {'matches' if got == expected else 'got ' + str(got)[:60] + '...'}")

print(f"{passed}/{len(tests)} passed")
