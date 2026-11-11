from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    """LeetCode level-order list -> tree. None means "no node here".
    [1, 2, 3, None, 4] is 1 with children 2 and 3, and 2 has only a right child 4.
    Returns the root (None for an empty list)."""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


def to_list(root):
    """Tree -> LeetCode level-order list, trailing Nones removed.
    If a node shows up twice (a broken tree with a loop), returns 'CYCLE' instead of running forever."""
    out = []
    seen = set()
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        if node in seen:
            return 'CYCLE'
        seen.add(node)
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out
