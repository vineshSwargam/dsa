# Remove Nth Node From End of List
# Medium
# Topics
# Company Tags
# Hints

# Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4], n = 2

# Output: [1,2,4]

# Example 2:

# Input: head = [5], n = 1

# Output: []

# Example 3:

# Input: head = [1,2], n = 2

# Output: [2]

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz



# Topics

# Linked List Two Pointers


# Recommended Time & Space Complexity

# You should aim for a solution with O(N) time and O(1) space, where N is the length of the given list.



# Hint 1

# A brute force solution would involve storing the nodes of the list into an array, removing the nth node from the array, and then converting the array back into a linked list to return the new head. However, this requires O(N) extra space. Can you think of a better approach to avoid using extra space? Maybe you should first solve with a two pass approach.



# Hint 2

# We can use a two-pass approach by first finding the length of the list, N. Since removing the nth node from the end is equivalent to removing the (N - n)th node from the front, as they both mean the same. How can you remove the node in a linked list?



# Hint 3

# For example, consider a three-node list [1, 2, 3]. If we want to remove 2, we update the next pointer of 1 (initially pointing to 2) to point to the node after 2, which is 3. After this operation, the list becomes [1, 3], and we return the head. But, can we think of a more better approach? Maybe a greedy calculation can help.



# Hint 4

# We can avoid a separate length-counting pass with two pointers. Move the first pointer n steps ahead from the head. Then, start another pointer second at a dummy node before the head and iterate both pointers simultaneously until first reaches null. At this point, the second pointer is just before the node to be removed. We then remove the node that is next to the second pointer. Why does this work?



# Hint 5

# This works because first stays n nodes ahead of second.next. When first reaches the end, second.next is exactly the nth node from the end. This positioning allows us to remove that node efficiently.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 60.8%

from utils.print import print_list
from utils.linked_list import build_list, to_list
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # run two pointers first and sec. first will start from i = 0 + n, sec will start at -1, a dummy node before the head
        # once first reaches None, sec becomes the right node to pop

        # 1, 2, 3, 4, 5 and n = 5
        i=n

        # move fst to nth position
        fst = head # first position
        while i>0: # n=5, 5-1 = 4
            fst = fst.next #runs 4 times. doing head.next.next.next.next
            i -= 1

        # print('fst -')
        # print_list(fst)
        # now fst is at nth position
        sec = ListNode(None, head) # dummy node -1
        # print('sec -')
        # print_list(sec)

        while fst != None:
            fst = fst.next # ind 6 is none
            sec = sec.next # ind

        # sec.next is now the node to pop
        # 1, 2, 3 - 2 is popping, so sec is 1

        if sec.next == head:
            return head.next

        sec.next = sec.next.next
        
        # print('head -')
        print_list(head)



        return head


sol = Solution()

# (head, n, expected)
tests = [
    ([1,2,3,4], 2, [1,2,4]),      # example 1
    ([5], 1, []),                 # example 2: only node
    ([1,2], 2, [2]),              # example 3: remove head
    ([1,2], 1, [1]),              # remove tail
    ([1,2,3,4,5], 5, [2,3,4,5]),  # remove head of longer list
    ([1,2,3,4,5], 1, [1,2,3,4]),  # remove tail of longer list
    ([1,2,3,4,5], 3, [1,2,4,5]),  # remove middle
    (list(range(1, 31)), 15, [v for v in range(1, 31) if v != 16]),  # max size
]

for vals, n, expected in tests:
    got = to_list(sol.removeNthFromEnd(build_list(vals), n))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  head={vals} n={n} -> {got}  expected {expected}")
