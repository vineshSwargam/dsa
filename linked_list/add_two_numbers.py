# Add Two Numbers
# Medium
# Topics
# Company Tags
# Hints

# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.

# Example 1:

# Input: l1 = [1,2,3], l2 = [4,5,6]

# Output: [5,7,9]

# Explanation: 321 + 654 = 975.

# Example 2:

# Input: l1 = [9], l2 = [9]

# Output: [8,1]

# Constraints:

# 1 <= l1.length, l2.length <= 100.
# 0 <= Node.val <= 9



# Topics

# Linked List Math Recursion


# Recommended Time & Space Complexity

# You should aim for a solution with O(m + n) time and O(1) space, where m is the length of list l1 and n is the length of list l2.



# Hint 1

# Try to visualize the addition of two numbers. We know that the addition of two numbers is done by starting at the one's digit. We add the numbers by going through digit by digit. We track the extra value as a carry because the addition of two digits can result in a number with two digits. The carry is then added to the next digits, and so on. How do you implement this in case of linked lists?



# Hint 2

# We track the extra value, carry, here as well. We iterate through the lists l1 and l2 until both lists reach null. We add the values of both nodes as well as the carry. If either of the nodes is null, we add 0 in its place and continue the process while tracking the carry simultaneously. Once we complete the process, if we are left with any carry, we add an extra node with that carry value and return the head of the result list.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 60.3%


from typing import Optional
from utils.linked_list import ListNode, build_list, to_list, print_list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None
        head = None

        def add_to_ll(ld: int, pr, head):
            hd = head
            node = ListNode(ld)
            if pr:
                pr.next = node
            else:
                hd = node
            pr = node
            return hd, pr

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            ls = l1_val + l2_val + carry
            lower_dig = ls%10
            carry = ls//10

            head, prev = add_to_ll(lower_dig, prev, head)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            head, prev = add_to_ll(carry, prev, head)

        return head


    #     153  351
    #     456  654
    #    5001 1005 
        



sol = Solution()

# (l1, l2, expected) - digits are in reverse order
tests = [
    # ([1,2,3], [4,5,6], [5,7,9]),                       # example 1: 321 + 654 = 975
    # ([9], [9], [8,1]),                                 # example 2: 9 + 9 = 18
    # ([0], [0], [0]),                                   # both zero
    # ([0], [1,2], [1,2]),                               # one number is zero: 0 + 21 = 21
    ([5], [5], [0,1]),                                 # carry creates a new digit: 5 + 5 = 10
    ([1,2,3], [4], [5,2,3]),                           # l1 longer: 321 + 4 = 325
    ([4], [1,2,3], [5,2,3]),                           # l2 longer: 4 + 321 = 325
    ([5,6], [5,6], [0,3,1]),                           # carry in the middle: 65 + 65 = 130
    ([9,9,9], [1], [0,0,0,1]),                         # carry runs through l1: 999 + 1 = 1000
    ([1], [9,9,9], [0,0,0,1]),                         # carry runs through l2: 1 + 999 = 1000
    ([9,9], [9,9], [8,9,1]),                           # carry at every digit: 99 + 99 = 198
    ([9]*100, [1], [0]*100 + [1]),                     # max length, carry runs through all of it
    ([9]*100, [9]*100, [8] + [9]*99 + [1]),            # both max length, result is 101 digits
]

for a, b, expected in tests:
    got = to_list(sol.addTwoNumbers(build_list(a), build_list(b)))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  l1={a} l2={b} -> {got}  expected {expected}")
