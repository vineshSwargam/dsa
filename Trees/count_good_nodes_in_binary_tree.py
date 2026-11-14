# Count Good Nodes in Binary Tree
# Medium
# Topics
# Company Tags
# Hints

# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

# Given the root of a binary tree root, return the number of good nodes within the tree.

# Example 1:

# Input: root = [2,1,1,3,null,1,5]

# Output: 3

# Example 2:

# Input: root = [1,2,-1,3,4]

# Output: 4

# Constraints:

# 1 <= number of nodes in the tree <= 100,000
# -100 <= Node.val <= 100



# Topics

# Tree Depth-First Search Breadth-First Search Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time andO(n) space, where n is the number of nodes in the given tree.



# Hint 1

# A brute force solution would involve considering every node and checking if the path from the root to that node is valid, resulting in an O(n^2) time complexity. Can you think of a better approach?



# Hint 2

# We can use the Depth First Search (DFS) algorithm to traverse the tree. But can you think of a way to determine if the current node is a good node in a single traversal? Maybe we need to track a value while traversing the tree.



# Hint 3

# While traversing the tree, we should track the maximum value along the current path. This allows us to determine whether the nodes we encounter are good. We can use a global variable to count the number of good nodes.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 73.9%


from utils.tree import TreeNode, build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def using_recursive_dfs(self, root):
        res = 0
        if not root:
            return res

        def dfs(r, lkmv):
            nonlocal res
            if r.val >= lkmv:
                lkmv = r.val
                res += 1
            if r.left:
                dfs(r.left, lkmv)
            if r.right:
                dfs(r.right, lkmv)

        dfs(root, root.val)
        return res

    def using_improved_recursive_dfs(self, root):
        def dfs(r, lkmv):
            res = 0
            if not r:
                return res
            
            if r.val >= lkmv:
                lkmv = r.val
                res += 1

            res += dfs(r.left, lkmv)
            res += dfs(r.right, lkmv)
            return res

        return dfs(root, root.val)


    def using_iterative_dfs(self, root):
        def dfs(r):
            st = [(r, r.val)] if r else []
            res = 0

            while st:
                node, lkmv = st.pop() # lkmv is last known max value
                
                if node.val >= lkmv:
                    lkmv = node.val
                    res += 1

                if node.left:
                    st.append((node.left, lkmv))
                if node.right:
                    st.append((node.right, lkmv))

            return res

        
        return dfs(root)

    def good_nodes(self, root: TreeNode) -> int:
        # return self.using_iterative_dfs(root)
        # return self.using_recursive_dfs(root)
        return self.using_improved_recursive_dfs(root)


sol = Solution()

# run from the repo root: python3 -m Trees.count_good_nodes_in_binary_tree
# (root, expected) - root in LeetCode level-order form
N = 100000
depth = lambda i: (i + 1).bit_length() - 1                              # depth of the node at level-order index i
complete_rising = [depth(i) for i in range(N)]                          # 100k nodes, each level bigger than the last, all good
complete_falling = [-depth(i) for i in range(N)]                        # 100k nodes, each level smaller, only the root is good
left_chain_zeros = [0] + [x for _ in range(N - 1) for x in (0, None)]   # 100k-deep left chain of equal values, all good
right_chain_zigzag = [100] + [x for i in range(1, N) for x in (None, -100 if i % 2 else 100)]   # 100, -100, 100, ... only the 100s are good

tests = [
    ([2,1,1,3,None,1,5], 3),                # example 1
    ([1,2,-1,3,4], 4),                      # example 2
    ([1], 1),                               # single node, root is always good
    ([5,5,5], 3),                           # equal to the max still counts as good
    ([3,1,4], 2),                           # smaller child is bad, bigger child is good
    ([3,3,None,4,2], 3),                    # equal, then bigger, then smaller
    ([5,1,10,None,None,7,12], 3),           # 7 beats its grandparent 5 but not its parent 10, so it's bad
    ([2,None,1,None,3], 2),                 # path dips then recovers: 2 good, 1 bad, 3 good
    ([5,4,8,9,1,7,10], 4),                  # 9 is good on the left even though 8 is bigger on the right branch
    ([1,2,3,4,5,6,7], 7),                   # every level bigger, all good
    ([7,6,5,4,3,2,1], 1),                   # every level smaller, only the root
    ([-100,-100,-100], 3),                  # all at the lower limit
    ([100,-100,-100,100], 2),               # root at the upper limit, nothing beats it except an equal
    ([0,-1,1], 2),                          # zero and negatives
    (complete_rising, N),                   # max size, all good
    (complete_falling, 1),                  # max size, only the root
    (left_chain_zeros, N),                  # 100k deep, too deep for plain recursion
    (right_chain_zigzag, N // 2),           # 100k deep, half the nodes good
]

passed = 0
for vals, expected in tests:
    try:
        got = sol.good_nodes(build_tree(vals))
    except RecursionError:
        got = 'ERROR (too deep for recursion)'
    ok = got == expected
    passed += ok
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
