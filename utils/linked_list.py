class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head) -> None:
    seen = set()
    vals = []
    node = head
    while node and node not in seen:
        seen.add(node)
        vals.append(str(node.val))
        node = node.next

    # node is only non-None here if the list loops back on itself
    vals.append(f'CYCLE back to {node.val}' if node else 'None')
    print(' -> '.join(vals))
    
def build_list(vals):
    """[1, 2, 3] -> 1 -> 2 -> 3 -> None. Returns the head (None for an empty list)."""
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    """1 -> 2 -> 3 -> None -> [1, 2, 3]. Stops if the list has a cycle."""
    vals, seen = [], set()
    while head and head not in seen:
        seen.add(head)
        vals.append(head.val)
        head = head.next
    return vals



class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def build_random_list(pairs):
    """[[3, None], [7, 0]] -> 3 -> 7 -> None, where each pair is [val, random_index]. Returns the head."""
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, random_index) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0] if nodes else None


def _node_indexes(head):
    """Maps each node to its position. Stops if the list has a cycle."""
    indexes = {}
    while head and head not in indexes:
        indexes[head] = len(indexes)
        head = head.next
    return indexes


def to_random_list(head):
    """3 -> 7 -> None -> [[3, None], [7, 0]]. A random pointing to a node outside this list shows as 'OUTSIDE'."""
    indexes = _node_indexes(head)
    return [[n.val, None if n.random is None else indexes.get(n.random, 'OUTSIDE')] for n in indexes]


def shares_nodes(head1, head2):
    """True if the two lists have any node object in common."""
    return bool(_node_indexes(head1).keys() & _node_indexes(head2).keys())
