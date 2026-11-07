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

from typing import List
from collections import defaultdict

class Solution:
    def using_hash(self, nums: List[int]) -> int:
        nmap = defaultdict(int)

        for n in nums:
            if nmap[n] > 0:
                return n
            nmap[n] += 1

    def using_sort(self, nums: List[int]) -> int:
        nums.sort()
        prev = None
        for n in nums:
            if prev == n:
                return n
            prev = n

    def using_fast_n_slow(self, nums: List[int]) -> int:
        sl = fst = 0

        while True:
            sl = nums[sl]
            fst = nums[nums[fst]]
            if sl == fst:
                break
        sl2 = 0
        while True:
            sl2 = nums[sl2]
            sl = nums[sl]
            if sl == sl2:
                return sl

    def find_duplicate(self, nums: List[int]) -> int:
        # return self.using_sort(nums)
        return self.using_hash(nums)
        # return self.using_fast_n_slow(nums)


sol = Solution()

# (nums, expected)
tests = [
    ([1,2,3,2,2], 2),                           # example 1
    ([1,2,3,4,4], 4),                           # example 2
    ([1,1], 1),                                 # smallest input, n = 1
    ([1,1,2], 1),                               # duplicate is the smallest value
    ([2,2,2,2,2], 2),                           # every value is the duplicate
    ([1,3,4,2,2], 2),                           # duplicate at the end
    ([3,1,3,4,2], 3),                           # duplicate not adjacent
    ([4,3,1,4,2], 4),                           # duplicate at the start
    ([5,4,3,2,1,5], 5),                         # first and last positions
    ([2,2,9,5,7,3,8,4,6,1], 2),                 # your example, indexes 3-8 are never reached
    ([2,5,9,6,9,3,8,9,7,1], 9),                 # appears three times
    (list(range(1, 10001)) + [10000], 10000),   # max size, duplicate is the largest value
    (list(range(1, 10001)) + [1], 1),           # max size, very long cycle
]

passed = 0
for nums, expected in tests:
    got = sol.find_duplicate(list(nums))  # a copy, because using_sort changes the list
    status = "PASS" if got == expected else "FAIL"
    passed += got == expected
    shown = nums if len(nums) <= 20 else f"[{len(nums)} numbers]"
    print(f"{status}  nums={shown} -> {got}  expected {expected}")

print(f"{passed}/{len(tests)} passed")
