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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


sol = Solution()
head, n = [1,2,3,4], 2 # Output [1,2,4]
# head, n = [5], 1 # Output []
# head, n = [1,2], 2 # Output [2]



print(sol.removeNthFromEnd(head, n))
