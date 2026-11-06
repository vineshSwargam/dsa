from typing import Optional, List

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
