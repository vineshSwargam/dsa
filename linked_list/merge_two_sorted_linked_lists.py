# Merge Two Sorted Linked Lists
# Easy
# Topics
# Company Tags
# Hints
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []
# Constraints:

# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100


# Topics

# Recommended Time & Space Complexity

# Hint 1
# A brute force solution would involve storing the values of both linked lists in an array, sorting the array, and then converting it back into a linked list. This approach would use O(n) extra space and is trivial. Can you think of a better way? Perhaps the sorted nature of the lists can be leveraged.


# Hint 2
# We create a dummy node to keep track of the head of the resulting linked list while iterating through the lists. Using l1 and l2 as iterators for list1 and list2, respectively, we traverse both lists node by node to build a final linked list that is also sorted. How do you implement this?


# Hint 3
# For example, consider list1 = [1, 2, 3] and list2 = [2, 3, 4]. While iterating through the lists, we move the pointers by comparing the node values from both lists. We link the next pointer of the iterator to the node with the smaller value. For instance, when l1 = 1 and l2 = 2, since l1 < l2, we point the iterator's next pointer to l1 and proceed.


from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def revision(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
            
        # flush out remaining elements
        cur.next = list1 or list2

        return head.next
        

    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_n3 = n3 = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur_n3.next = list1
                list1 = list1.next
            else:
                cur_n3.next = list2
                list2 = list2.next
    
            cur_n3 = cur_n3.next
        
        cur_n3.next = list1 or list2

        return n3.next

    
sol = Solution()

# l1, l2 = ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(5)))      # 1 -> 1 -> 2 -> 3 -> 4 -> 5 - example 1
# l1, l2 = None, ListNode(1, ListNode(2))     # 1 -> 2 - example 2, list1 empty
# l1, l2 = None, None  # None - example 3, both empty
# l1, l2 = ListNode(1, ListNode(2)), None  # 1 -> 2 - list2 empty
# l1, l2 = ListNode(1, ListNode(2, ListNode(3))), ListNode(4, ListNode(5, ListNode(6)))    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 - list1 entirely first
# l1, l2 = ListNode(4, ListNode(5, ListNode(6))), ListNode(1, ListNode(2, ListNode(3)))    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 - list2 entirely first
# l1, l2 = ListNode(1, ListNode(3, ListNode(5))), ListNode(2, ListNode(4, ListNode(6)))    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 - alternating
# l1, l2 = ListNode(1, ListNode(2, ListNode(4, ListNode(5)))), ListNode(3)                 # 1 -> 2 -> 3 -> 4 -> 5 - different lengths
# l1, l2 = ListNode(2, ListNode(2)), ListNode(2, ListNode(2))                              # 2 -> 2 -> 2 -> 2 - all equal
# l1, l2 = ListNode(-100, ListNode(0)), ListNode(-50, ListNode(100))                       # -100 -> -50 -> 0 -> 100 - negatives and value limits
l1, l2 = ListNode(-3, ListNode(-1, ListNode(2))), ListNode(-2, ListNode(0, ListNode(3))) # -3 -> -2 -> -1 -> 0 -> 2 -> 3 - negatives, alternating


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

print_list(sol.revision(l1, l2))