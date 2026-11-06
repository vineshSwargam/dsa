# Find the Duplicate Number
# Medium
# Topics
# Company Tags
# Hints

# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

# There is exactly one repeated integer in nums, and every other integer appears at most once.

# Return the repeated integer.

# Example 1:

# Input: nums = [1,2,3,2,2]

# Output: 2

# Example 2:

# Input: nums = [1,2,3,4,4]

# Output: 4

# Follow-up: Can you solve the problem without modifying the array nums and using
# 𝑂
# (
# 1
# )
# O(1) extra space?

# Constraints:

# 1 <= n <= 10,000
# nums.length == n + 1
# 1 <= nums[i] <= n



# Topics

# Array Two Pointers Binary Search Bit Manipulation


# Recommended Time & Space Complexity

# You should aim for a solution with O(n) time and O(1) space without modifying the input array, where n is the size of the input array.



# Hint 1

# A naive approach would be to use a hash set, which provides O(1) average-time lookups but requires O(n) extra space. To avoid extra space, consider treating the array like a linked list: from an index i, the next index is nums[i]. Every value is in the range 1 to len(nums) - 1, so every value is also a valid index.



# Hint 2

# Since one value is repeated, multiple indices point to the same next index. Following the indices starting from index 0 must therefore lead to a cycle, whose entry corresponds to the duplicate value. Which algorithm can detect a cycle using constant extra space without modifying the array?



# Hint 3

# Use Floyd's cycle detection algorithm. Initialize a slow and a fast pointer at index 0. Repeatedly move the slow pointer one step with slow = nums[slow] and the fast pointer two steps with fast = nums[nums[fast]] until they meet. Is this first meeting point necessarily the duplicate?



# Hint 4

# The first meeting point may be anywhere inside the cycle. After the pointers meet, initialize a second slow pointer at index 0. Move both slow pointers one step at a time using the values in nums. The index where they meet is the cycle entry, which is the duplicate number.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 66.0%


class Solution:
    def find_duplicate(self, nums: List[int]) -> int:


sol = Solution()
nums = [1,2,3,2,2] # Output 2
# nums = [1,2,3,4,4] # Output 4



print(sol.find_duplicate(nums))
