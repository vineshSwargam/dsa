# Serialize and Deserialize Binary Tree
# Hard
# Topics
# Company Tags
# Hints

# Implement an algorithm to serialize and deserialize a binary tree.

# Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

# Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

# Example 1:

# Input: root = [1,2,3,null,null,4,5]

# Output: [1,2,3,null,null,4,5]

# Example 2:

# Input: root = []

# Output: []

# Constraints:

# 0 <= The number of nodes in the tree <= 10,000.
# -1000 <= Node.val <= 1000



# Topics

# String Tree Depth-First Search Breadth-First Search Design Binary Tree


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.



# Hint 1

# A straightforward way to serialize a tree is by traversing it and adding nodes to a string separated by a delimiter (example: ","), but this does not handle null nodes effectively. During deserialization, it becomes unclear where to stop or how to handle missing children. Can you think of a way to indicate null nodes explicitly?



# Hint 2

# Including a placeholder for null nodes (example: "N") during serialization ensures that the exact structure of the tree is preserved. This placeholder allows us to identify missing children and reconstruct the tree accurately during deserialization.



# Hint 3

# We can use the Depth First Search (DFS) algorithm for both serialization and deserialization. During serialization, we traverse the tree and add node values to the result string separated by a delimiter, inserting N whenever we encounter a null node. During deserialization, we process the serialized string using an index i, create nodes for valid values, and return from the current path whenever we encounter N, reconstructing the tree accurately.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 69.2%


from typing import Optional
from utils.tree import TreeNode, build_tree, to_list

# Definition for a binary tree node (lives in utils/tree.py):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:


# run from the repo root: python3 -m Trees.serialize_and_deserialize_binary_tree
# each test is a tree in LeetCode level-order form. The check is a round trip:
#   serialize must return a string, and a FRESH Codec must turn that string back into the same tree
#   (a fresh one, so the string has to carry everything - nothing can be stashed on self)
N = 10000
complete_dupes = [v for v in range(-1000, 1001)] * 5                    # 10005 values, every value repeated
complete_dupes = complete_dupes[:N]                                     # 10k nodes, lots of duplicate values
left_chain = [0] + [x for v in range(1, N) for x in (v % 2001 - 1000, None)]    # 10k deep left chain
right_chain = [0] + [x for v in range(1, N) for x in (None, v % 2001 - 1000)]   # 10k deep right chain

tests = [
    [1,2,3,None,None,4,5],              # example 1
    [],                                 # example 2, empty tree
    [1],                                # single node
    [1,2],                              # only a left child
    [1,None,2],                         # only a right child
    [1,1],                              # duplicate as the left child...
    [1,None,1],                         # ...and as the right child: same values, different shape
    [5,5,5,5,None,None,5],              # all duplicates, uneven shape
    [0,0,0],                            # zeros (a value of 0 must not be treated as "no node")
    [-1000,1000,-1,0,None,None,-999],   # negatives and multi-digit values in the string
    [1,2,None,None,3,4],                # zigzag: left, right, left
    [1,2,3,4,5,6,7],                    # full tree
    [1,None,2,None,3,None,4],           # sparse right chain
    [1,2,3,None,4,None,5,6,None,None,7],   # gaps on both sides
    complete_dupes,                     # max size, heavy duplicates
    left_chain,                         # 10k deep, too deep for plain recursion
    right_chain,                        # 10k deep the other way
]

passed = 0
for vals in tests:
    root = build_tree(vals)
    expected = to_list(root)
    try:
        data = Codec().serialize(root)
        back = Codec().deserialize(data)
        got = to_list(back)
        ok = isinstance(data, str) and got == expected and (root is None or back is not root)
    except RecursionError:
        data, got, ok = '', 'ERROR (too deep for recursion)', False
    passed += ok
    shown = vals if len(vals) <= 20 else f"[{len(vals)} values]"
    got_shown = got if not isinstance(got, list) or len(got) <= 20 else f"[{len(got)} values]"
    data_shown = data if isinstance(data, str) and len(data) <= 50 else f"<{type(data).__name__}, length {len(data) if hasattr(data, '__len__') else '?'}>"
    print(f"{'PASS' if ok else 'FAIL'}  {shown} -> {data_shown!r} -> {got_shown}")

print(f"{passed}/{len(tests)} passed")
