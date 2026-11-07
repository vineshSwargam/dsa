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

# Linked List Divide and Conquer Heap (Priority Queue) Merge Sort


# Recommended Time & Space Complexity

# You should aim for a solution with O(k + n log k) time and O(k) auxiliary space, where k is the total number of lists and n is the total number of nodes across all lists. The O(k) term accounts for visiting all input list heads, including empty lists. The hints below use iterative divide and conquer with arrays of merged list heads.



# Hint 1

# Collecting all n node values, sorting them, and building a new linked list takes O(n log n) time and O(n) extra space. Can you use the fact that each input list is already sorted? Think about how to merge two sorted linked lists by relinking their existing nodes.



# Hint 2

# Merging lists one by one into a growing result is a slower O(n * k) baseline and can exceed the time limit. Instead, merge adjacent lists in pairs during each round, then repeat with the merged lists. How does this change the number of times each node is processed?



# Hint 3

# If lists is empty, return null. While more than one list remains, create a new mergedLists array and merge lists[0] with lists[1], lists[2] with lists[3], and so on, appending each merged head. If the final list has no partner, carry it into the next round unchanged. Replace lists with mergedLists and repeat, then return the remaining head. Use an iterative two-list merge that reuses the existing nodes. There are O(log k) rounds, each processing at most n nodes, and the arrays of list heads use O(k) auxiliary space.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

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
