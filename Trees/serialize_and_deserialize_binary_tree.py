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

from collections import deque

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root]) if root else []
        s = []
        nulls = []

        while q:
            node = q.popleft()
            if node:
                s.extend(nulls) # flush collected nulls | can remove for round trip, only valid for serialise tests, it is meant to 
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
                nulls = [] # can remove for round trip, only valid for serialise tests, it is meant to 
            else:
                nulls.append('null') # collect nulls. | can remove for round trip, only valid for serialise 
        return ','.join(s)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        data = data.split(',')
        root = TreeNode(int(data[0]))

        q = deque([root]) if root else []
        dlen = len(data)
        pointer = 1

        while q and pointer < dlen:
            node = q.popleft()

            for side in ['left', 'right']:
                if pointer < dlen and data[pointer] != 'null':
                    child = TreeNode(int(data[pointer]))
                    setattr(node, side, child)
                    q.append(child)
                pointer += 1

        return root



        


# run from the repo root: python3 -m Trees.serialize_and_deserialize_binary_tree
#
# Format the tests expect: level order, values separated by SEP, a missing child written as NULL.
#   [-15, 10, 20, None, None, 15, 5, -5]  <->  "-15,10,20,null,null,15,5,-5"
# Trailing NULLs are optional: "1,2,null,null,null" and "1,2" are treated as the same string.
# Change SEP / NULL here if you pick a different separator or marker.
SEP, NULL = ',', 'null'

def to_string(vals):
    return SEP.join(NULL if v is None else str(v) for v in vals)

def tokens(s):
    """Split a serialized string into tokens and drop trailing NULLs, so both styles compare equal."""
    if not isinstance(s, str):
        return f'NOT A STRING ({type(s).__name__})'
    t = [x.strip() for x in s.split(SEP)] if s.strip() else []
    while t and t[-1] == NULL:
        t.pop()
    return t

def short(x, n=60):
    s = repr(x)
    return s if len(s) <= n else s[:n] + f'... ({len(s)} chars)'

N = 10000
complete_dupes = ([v for v in range(-1000, 1001)] * 5)[:N]                      # 10k nodes, lots of duplicate values
left_chain = to_list(build_tree([0] + [x for v in range(1, N) for x in (v % 2001 - 1000, None)]))   # 10k deep left chain
right_chain = to_list(build_tree([0] + [x for v in range(1, N) for x in (None, v % 2001 - 1000)]))  # 10k deep right chain

# trees in level-order form (no trailing Nones), each with what it covers
trees = [
    ([1,2,3,None,None,4,5],              "example 1"),
    ([],                                 "example 2, empty tree"),
    ([-15,10,20,None,None,15,5,-5],      "the tree you drew: 10 ends early, 15 has only a left child"),
    ([1],                                "single node"),
    ([1,2],                              "only a left child"),
    ([1,None,2],                         "only a right child"),
    ([1,1],                              "duplicate as the left child..."),
    ([1,None,1],                         "...and as the right child: same values, different shape"),
    ([5,5,5,5,None,None,5],              "all duplicates, uneven shape"),
    ([0,0,0],                            "zeros (0 must not be treated as 'no node')"),
    ([-1000,1000,-1,0,None,None,-999],   "negatives and multi-digit values"),
    ([1,2,None,None,3,4],                "zigzag: left, right, left"),
    ([1,2,3,4,5,6,7],                    "full tree"),
    ([1,None,2,None,3,None,4],           "right chain"),
    ([1,2,3,None,4,None,5,6,None,None,7], "gaps on both sides"),
    (complete_dupes,                     "max size, heavy duplicates"),
    (left_chain,                         "10k deep left chain"),
    (right_chain,                        "10k deep right chain"),
]

# extra strings for deserialize only: the same trees written WITH their trailing nulls
with_trailing = [
    ("1,2,3,null,null,4,5,null,null,null,null", [1,2,3,None,None,4,5], "example 1 with all trailing nulls"),
    ("1,null,null",                             [1],                   "single node with its two nulls"),
    ("-15,10,20,null,null,15,5,-5,null,null,null,null,null", [-15,10,20,None,None,15,5,-5], "your tree with trailing nulls"),
]


def run(name, cases, check):
    print(f"\n== {name} ==")
    passed = 0
    for case in cases:
        try:
            ok, line = check(*case)
        except Exception as e:
            ok, line = False, f"ERROR {type(e).__name__}: {e}"
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {line}")
    print(f"{name}: {passed}/{len(cases)} passed")
    return passed, len(cases)


# 1) serialize alone: tree in, compare the string token by token
def check_serialize(vals, note):
    got = Codec().serialize(build_tree(vals))
    expected = to_string(vals)
    ok = tokens(got) == tokens(expected)
    return ok, f"{note}: got {short(got)}" + ("" if ok else f"  expected {short(expected)}")

# 2) deserialize alone: string in, compare the tree that comes back
def check_deserialize(data, expected_vals, note):
    got = to_list(Codec().deserialize(data))
    ok = got == expected_vals
    return ok, f"{note}: {short(data, 40)} -> {short(got)}" + ("" if ok else f"  expected {short(expected_vals)}")

# 3) round trip: serialize, then a FRESH Codec deserializes (nothing can be stashed on self)
def check_round_trip(vals, note):
    root = build_tree(vals)
    data = Codec().serialize(root)
    back = Codec().deserialize(data)
    got = to_list(back)
    ok = isinstance(data, str) and got == vals and (root is None or back is not root)
    return ok, f"{note}: -> {short(got)}"


results = [
    # run("serialize", trees, check_serialize),
    # run("deserialize", [(to_string(v), v, note) for v, note in trees] + with_trailing, check_deserialize),
    run("round trip", trees, check_round_trip),
]
print(f"\nTOTAL {sum(p for p, _ in results)}/{sum(t for _, t in results)} passed")
