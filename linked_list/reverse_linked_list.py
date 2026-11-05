# Reverse Linked List
# Easy
# Topics
# Company Tags
# Hints
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000


# Topics

 

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.


# Hint 1
# A brute force solution would be to store the node values of the linked list into an array, then reverse the array, convert it back into a linked list, and return the new linked list's head. This would be an O(n) time solution but uses extra space. Can you think of a better way? Maybe there is an approach to reverse a linked list in place.


# Hint 2
# As you can see, the head of the linked list becomes the tail after we reverse it. Can you think of an approach to change the references of the node pointers? Perhaps reversing a simple two-node list might help clarify the process.


# Hint 3
# For example, consider a list [2, 3], where 2 is the head of the list and 3 is the tail. When we reverse it, 3 becomes the new head, and its next pointer will point to 2. Then, 2's next pointer will point to null. Can you figure out how to apply this approach to reverse a linked list of length n by iterating through it?


# Hint 4
# We can reverse the linked list in place by reversing the pointers between two nodes while keeping track of the next node's address. Before changing the next pointer of the current node, we must store the next node to ensure we don't lose the rest of the list during the reversal. This way, we can safely update the links between the previous and current nodes.

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, head: Optional[ListNode]) -> None:
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next # save the rest of the list
            curr.next = prev # point node to prev
            prev = curr # move curr to prev
            curr = nxt # move nxt to curr

        self.print_list(prev)
        return prev

        


        

sol = Solution()

head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))    # 3 -> 2 -> 1 -> 0 - example 1
# head = None                                                # None - example 2, empty list
# head = ListNode(5)                                         # 5 - single node
# head = ListNode(2, ListNode(3))                            # 3 -> 2 - two nodes
# head = ListNode(1, ListNode(1, ListNode(2)))               # 2 -> 1 -> 1 - duplicate values
# head = ListNode(-1000, ListNode(0, ListNode(1000)))        # 1000 -> 0 -> -1000 - negatives and value limits

# head = [] # []


# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000
print(sol.reverseList(head))
        