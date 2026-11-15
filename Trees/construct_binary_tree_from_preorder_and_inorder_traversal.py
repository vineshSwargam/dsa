# Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# Topics
# Company Tags
# Hints

# You are given two integer arrays preorder and inorder.

# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.

# Rebuild the binary tree from the preorder and inorder traversals and return its root.

# Example 1:

# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

# Output: [1,2,3,null,null,null,4]

# Example 2:

# Input: preorder = [1], inorder = [1]

# Output: [1]

# Constraints:

# 1 <= inorder.length <= 2001.
# inorder.length == preorder.length
# -1000 <= preorder[i], inorder[i] <= 1000



# Topics

# Array Hash Table Divide and Conquer Tree Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes.



# Hint 1

# You can observe that the in-order traversal helps divide the array into two halves based on the root node: the left part corresponds to the left subtree, and the right part corresponds to the right subtree. Can you think of how we can get the index of the root node in the in-order array? Maybe you should look into the pre-order traversal array.



# Hint 2

# From the pre-order traversal, we know that the first node is the root node. Using this information, can you now construct the binary tree?



# Hint 3

# After getting the root node from pre-order traversal, we then look for the index of that node in the in-order array. We can linearly search for the index but this would be an O(n^2) solution. Can you think of a better way? Maybe we can use a data structure to get the index of a node in O(1)?



# Hint 4

# We can use a hash map to get the index of any node in the in-order array in O(1) time. How can we implement this?



# Hint 5

# We use Depth First Search (DFS) to construct the tree. A global variable tracks the current index in the pre-order array. Indices l and r represent the segment in the in-order array for the current subtree. For each node in the pre-order array, we create a node, find its index in the in-order array using the hash map, and recursively build the left and right subtrees by splitting the range [l, r] into two parts for the left and right subtrees.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 71.0%


from typing import List, Optional
from utils.tree import TreeNode, to_list, preorder_vals, inorder_vals
from utils.tree import build_tree as make_tree   # renamed so it doesn't get mixed up with Solution.build_tree

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def using_recur_dfs(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_ind = 0
        in_len = len(inorder)
        pre_in_map = {}
        for i, val in enumerate(inorder):
            pre_in_map[val] = i


        def dfs(il, iu):
            # il is inorder's lower bound
            # iu is inorder's upper bound
            nonlocal pre_ind

            if il>iu:
                return None 

            root_val = preorder[pre_ind]
            root_ind = pre_in_map[root_val]

            root = TreeNode(root_val)
            pre_ind += 1


            root.left = dfs(il, root_ind-1)
            root.right = dfs(root_ind+1, iu)
            return root
                
        
        return dfs(0, in_len-1)
    
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.using_recur_dfs(preorder, inorder)


sol = Solution()

# run from the repo root: python3 -m Trees.construct_binary_tree_from_preorder_and_inorder_traversal
# (preorder, inorder, expected) - expected is the tree in LeetCode level-order form
# the big cases build a tree first and read its preorder / inorder off it
def big_case(vals):
    t = make_tree(vals)
    return (preorder_vals(t), inorder_vals(t), to_list(t))

complete_2001 = list(range(-1000, 1001))                                    # 2001 nodes, every value allowed, used once
left_chain_2001 = [0] + [x for v in range(1, 2001) for x in (v, None)]      # 2001-deep left chain
right_chain_2001 = [0] + [x for v in range(1, 2001) for x in (None, v)]     # 2001-deep right chain

tests = [
    ([1,2,3,4], [2,1,3,4], [1,2,3,None,None,None,4]),          # example 1
    # ([1], [1], [1]),                                            # example 2, single node
    # ([3,9,20,15,7], [9,3,15,20,7], [3,9,20,None,None,15,7]),    # left child is a leaf, right side goes deeper
    # ([1,2], [2,1], [1,2]),                                      # only a left child
    # ([1,2], [1,2], [1,None,2]),                                 # only a right child (same preorder as above!)
    # ([1,2,3], [3,2,1], [1,2,None,3]),                           # left chain
    # ([1,2,3], [1,2,3], [1,None,2,None,3]),                      # right chain
    # ([1,2,3], [2,3,1], [1,2,None,None,3]),                      # zigzag: left, then right
    # ([1,2,4,5,3,6,7], [4,2,5,1,6,3,7], [1,2,3,4,5,6,7]),        # full tree
    # ([1,2,4,3,5], [4,2,1,5,3], [1,2,3,4,None,5]),               # each child has only a left child
    # ([1,2,3,4,5], [2,4,3,5,1], [1,2,None,None,3,4,5]),          # empty left part at node 2
    # ([5,9,1], [9,5,1], [5,9,1]),                                # values are not sorted, it's not a BST
    # ([0,-1000,1000], [-1000,0,1000], [0,-1000,1000]),           # value limits
    big_case(complete_2001),                                    # max size
    big_case(left_chain_2001),                                  # 2001 deep, too deep for plain recursion
    big_case(right_chain_2001),                                 # 2001 deep the other way
]

passed = 0
for pre, ino, expected in tests:
    try:
        got = to_list(sol.build_tree(pre, ino))
    except RecursionError:
        got = 'ERROR (too deep for recursion)'
    ok = got == expected
    passed += ok
    shown = f"pre={pre} in={ino}" if len(pre) <= 10 else f"[{len(pre)} nodes]"
    got_shown = got if not isinstance(got, list) or len(got) <= 20 else f"[{len(got)} values]"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} -> {got_shown}")

print(f"{passed}/{len(tests)} passed")
