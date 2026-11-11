# Linked List Cycle Detection
# Easy
# Topics
# Company Tags
# Hints
# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

# Note: index is not given to you as a parameter.

# Example 1:



# Input: head = [1,2,3,4], index = 1

# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:



# Input: head = [1,2], index = -1

# Output: false
# Constraints:

# 0 <= Length of the list <= 1000.
# -1000 <= Node.val <= 1000
# index is -1 or a valid index in the linked list.


# Topics

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.


# Hint 1
# A naive approach would be to use a hash set, which takes O(1) time to detect duplicates. Although this solution is acceptable, it requires O(n) extra space. Can you think of a better solution that avoids using extra space? Maybe there is an efficient algorithm which uses two pointers.


# Hint 2
# We can use the fast and slow pointers technique, which is primarily used to detect cycles in a linked list. We iterate through the list using two pointers. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If the list has a cycle, these two pointers will eventually meet. Why does this work?


# Hint 3
# When there is no cycle in the list, the loop ends when the fast pointer becomes null. If a cycle exists, the fast pointer moves faster and continuously loops through the cycle. With each step, it reduces the gap between itself and the slow pointer by one node. For example, if the gap is 10, the slow pointer moves by 1, increasing the gap to 11, while the fast pointer moves by 2, reducing the gap to 9. This process continues until the fast pointer catches up to the slow pointer, confirming a cycle.

from typing import Optional, List

from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def using_fpsp(self, head: Optional[ListNode]) -> bool:
        sp = fp = head
        # fp = head.next.next if head != None and head.next != None else None

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if fp == sp:
                return True

        return False

    def using_hash_map(self, head: Optional[ListNode]) -> bool:
        node_ind = defaultdict(int)
        cur_node = head
        ind = 0

        while cur_node and cur_node.next != None:
            if cur_node not in node_ind:
                node_ind[cur_node] = ind
                ind += 1
                cur_node = cur_node.next
                continue
            
            return True

        return False


    def using_two_pointers(self, head):
        sp_node = head
        fp_node = head.next.next if head != None and head.next != None else None

        while fp_node != None and fp_node.next != None:
            if sp_node == fp_node:
                return True
            
            sp_node = sp_node.next
            fp_node = fp_node.next.next


        
        return False



    def has_cycle(self, head: Optional[ListNode]) -> bool:
        # return self.using_hash_map(head)
        return self.using_two_pointers(head)
            


        


sol = Solution()

# hd = ListNode(1, ListNode(2, ListNode(3, ListNode(4)))); hd.next.next.next.next = hd.next          # True  - example 1, tail to index 1
# hd = ListNode(1, ListNode(2))                                                                    # False - example 2, no cycle
# hd = None     # False - empty list
hd = ListNode(1)   # False - single node, no cycle
# hd = ListNode(1); hd.next = hd    # True  - single node points to itself
# hd = ListNode(1, ListNode(2)); hd.next.next = hd  # True  - two nodes, tail to head
# hd = ListNode(1, ListNode(2, ListNode(3, ListNode(4)))); hd.next.next.next.next = hd             # True  - tail to head, whole list is the cycle
# hd = ListNode(1, ListNode(2, ListNode(3))); hd.next.next.next = hd.next.next                     # True  - tail points to itself
# hd = ListNode(1, ListNode(2, ListNode(1, ListNode(2))))                                          # False - values repeat, no cycle
# hd = ListNode(1, ListNode(1, ListNode(1))); hd.next.next.next = hd.next                          # True  - all values equal, cycle
# hd = ListNode(1, ListNode(2)); hd.next.next = hd # True
# hd = ListNode(1, ListNode(2));  # True  - all values equal, cycle
# hd = ListNode(1, ListNode(1, ListNode(1)))                                                       # False - all values equal, no cycle

print(sol.has_cycle(hd))
        
        