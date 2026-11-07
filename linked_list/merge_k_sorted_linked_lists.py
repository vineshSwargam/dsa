# Merge K Sorted Linked Lists
# Hard
# Topics
# Company Tags
# Hints

# You are given an array of k linked lists lists, where each list is sorted in ascending order.

# Return the sorted linked list that is the result of merging all of the individual linked lists.

# Example 1:

# Input: lists = [[1,2,4],[1,3,5],[3,6]]

# Output: [1,1,2,3,3,4,5,6]

# Example 2:

# Input: lists = []

# Output: []

# Example 3:

# Input: lists = [[]]

# Output: []

# Constraints:

# 0 <= lists.length <= 10000
# 0 <= lists[i].length <= 500
# -10000 <= lists[i][j] <= 10000
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10000.



# Topics


# Recommended Time & Space Complexity


# Hint 1


# Hint 2


# Hint 3


# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 73.4%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


sol = Solution()
lists = [[1,2,4],[1,3,5],[3,6]] # Output [1,1,2,3,3,4,5,6]
# lists = [] # Output []
# lists = [[]] # Output []



print(sol.merge_k_lists(lists))
