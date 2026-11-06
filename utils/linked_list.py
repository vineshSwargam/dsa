class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
