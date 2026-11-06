# Reorder Linked List
# Medium
# Topics
# Company Tags
# Hints
# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# In the general case, label the nodes by their original zero-based positions from 0 to n - 1. After reordering, those original positions appear in this order:

# [0, n-1, 1, n-2, 2, n-3, ...]

# These numbers represent node positions, not the values stored in the nodes.

# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.


# Example 1:

# Input: head = [2,4,6,8]

# Output: [2,8,4,6]

# Example 2:

# Input: head = [2,4,6,8,10]

# Output: [2,10,4,8,6]

# Constraints:

# 1 <= Length of the list <= 1000.
# 1 <= Node.val <= 1000


# Topics

   

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.


# Hint 1
# A brute force solution would be to store the node values of the list in an array, reorder the values, and create a new list. Can you think of a better way? Perhaps you can try reordering the nodes directly in place, avoiding the use of extra space.


# Hint 2
# For example, consider the list [1, 2, 3, 4, 5]. To reorder the list, we connect the first and last nodes, then continue with the second and second-to-last nodes, and so on. Essentially, the list is split into two halves: the first half remains as is, and the second half is reversed and merged with the first half. For instance, [1, 2] will merge with the reversed [5, 4, 3]. Can you figure out a way to implement this reordering process? Maybe dividing the list into two halves could help.


# Hint 3
# We can divide the list into two halves using the fast and slow pointer approach, which helps identify the midpoint of the list. This allows us to split the list into two halves, with the heads labeled as l1 and l2. Next, we reverse the second half (l2). After these steps, we proceed to reorder the two lists by iterating through them node by node, updating the next pointers accordingly.

from typing import Optional, List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head: Optional[ListNode]) -> None:
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
    # have to reorder as 0, n-1, 1, n-2
    sn = fn = head

class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:

        fn = sn = head
        # print_list(head)
        while fn != None and fn.next != None:
            sn = sn.next
            fn = fn.next.next

        

        # now sn points to the middle of the ll

        cur_l1 = head
        cur_l2 = sn
        prev_l2 = None
        # print_list(cur_l2)

        # reverse l2
        while cur_l2:
            nxt = cur_l2.next
            cur_l2.next = prev_l2
            prev_l2 = cur_l2
            cur_l2 = nxt
            
        cur_l2 = prev_l2
        # print('reversed cur_l2 - ')
        # print_list(cur_l2)

        while cur_l2 != sn:
            cur_l1_nxt = cur_l1.next
            cur_l2_nxt = cur_l2.next
            cur_l2.next = cur_l1_nxt
            cur_l1.next = cur_l2

            cur_l1 = cur_l2.next
            cur_l2 = cur_l2_nxt
            # print('l1 -')
            # print_list(l1)
            # print('cur_l2 -')
            # print_list(cur_l2)

        print_list(head)

sol = Solution()

# hd = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))                                                       # 2 -> 8 -> 4 -> 6 - example 1, even length
# hd = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10)))))                                       # 2 -> 10 -> 4 -> 8 -> 6 - example 2, odd length
# hd = ListNode(1)                                                                                            # 1 - single node
# hd = ListNode(1, ListNode(2))                                                                               # 1 -> 2 - two nodes, order unchanged
# hd = ListNode(1, ListNode(2, ListNode(3)))                                                                  # 1 -> 3 -> 2 - three nodes
hd = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))              # 1 -> 7 -> 2 -> 6 -> 3 -> 5 -> 4 - length 7, like the problem statement
# hd = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))                           # 1 -> 6 -> 2 -> 5 -> 3 -> 4 - length 6
# hd = ListNode(5, ListNode(5, ListNode(5, ListNode(5))))                                                     # 5 -> 5 -> 5 -> 5 - all values equal
# hd = ListNode(1, ListNode(1, ListNode(2, ListNode(2))))                                                     # 1 -> 2 -> 1 -> 2 - duplicate values
# hd = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))                                                     # 9 -> 3 -> 7 -> 5 - values not sorted
# hd = ListNode(9, ListNode(7, ListNode(5, ListNode(3))))                                                     # 9 -> 3 -> 7 -> 5 - values not sorted
# hd = ListNode(1, ListNode(1000, ListNode(1)))                                                               # 1 -> 1 -> 1000 - value limits

print_list(sol.reorder_list(hd))