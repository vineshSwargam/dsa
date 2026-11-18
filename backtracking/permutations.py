# Permutations
# Medium
# Topics
# Company Tags
# Hints

# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:

# Input: nums = [7]

# Output: [[7]]

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10



# Topics

# Array Backtracking


# Recommended Time & Space Complexity

# You should aim for a solution with O(n * n!) time and O(n) space, where n is the size of the input array.



# Hint 1

# A permutation is the same as the array but with the numbers arranged in a different order. The given array itself is also considered a permutation. This means we should make a decision at each step to take any element from the array that has not been chosen previously. By doing this recursively, we can generate all permutations. How do you implement it?



# Hint 2

# We can use backtracking to explore all possible permutation paths. We initialize a temporary list to append the chosen elements and a boolean array of size n (the same size as the input array) to track which elements have been picked so far (true means the element is chosen; otherwise, false). At each step of recursion, we iterate through the entire array, picking elements that have not been chosen previously, and proceed further along that path. Can you think of the base condition to terminate the current recursive path?



# Hint 3

# We observe that every permutation has the same size as the input array. Therefore, we can append a copy of the list of chosen elements in the current path to the result list if the size of the list equals the size of the input array terminating the current recursive path.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 85.9%


from typing import List
from math import factorial
import traceback


class Solution:
    def using_recur_bt(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        nl = len(nums)
    
        def bt(i):
            if i >= nl:
                res.append(sub)
                return
            sub.append(nums[i])
            bt(i+1)
            sub.pop()
            bt(i+1)

        bt(0)
        return res

    # def using_recur_bt(self, nums: List[int]) -> List[List[int]]:
    #     res = []

    #     def bt(ind, sub): # [1, 2, 3]
    #         if ind >= nl:
    #             return
    #         res.append(sub.copy())
    #         for i in range(nl):
    #             if i == ind:
    #                 continue
    #             sub.append(nums[i])
    #             bt(i+1, sub)
    #             sub.pop()

    #     bt(0, [])
    #     return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.using_recur_bt(nums)


sol = Solution()

# run from the repo root: python3 -m backtracking.permutations
# (nums, expected) - the permutations can come in any order, but the order INSIDE each one matters
# expected is either the full answer, or (for the big cases) just how many permutations there should be.
# For a count, every permutation you return is also checked: it must use every number exactly once,
# and no permutation may appear twice.
tests = [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),   # example 1
    ([7], [[7]]),                                                   # example 2, one number, one permutation
    ([0,1], [[0,1],[1,0]]),                                         # zero is a real value
    ([-10,10], [[-10,10],[10,-10]]),                                # value limits
    ([3,1,2], [[3,1,2],[3,2,1],[1,3,2],[1,2,3],[2,3,1],[2,1,3]]),   # unsorted input, same 6 answers
    ([0,-1,1], [[0,-1,1],[0,1,-1],[-1,0,1],[-1,1,0],[1,0,-1],[1,-1,0]]),   # negatives
    ([1,2,3,4], 24),                                                # 4! = 24
    ([5,4,3,2,1], 120),                                             # 5! = 120, reversed input
    ([1,2,3,4,5,6], 720),                                           # max length, 6! = 720
    ([10,-10,0,5,-5,1], 720),                                       # max length, mixed values
]

def check(nums, got, expected):
    if not isinstance(got, list):
        return False, ""
    if isinstance(expected, list):
        return sorted(map(list, got)) == sorted(expected), ""
    for p in got:
        if sorted(p) != sorted(nums):
            return False, f"  {list(p)} is not a reordering of {nums}"
    if len(set(map(tuple, got))) != len(got):
        return False, "  the same permutation appears more than once"
    return len(got) == expected, ""

passed = 0
for nums, expected in tests:
    try:
        got = sol.permute(list(nums))
        ok, why = check(nums, got, expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} permutations" if isinstance(got, list) and len(got) > 6 else got
    print(f"{'PASS' if ok else 'FAIL'}  {nums} -> {shown}" + ("" if ok else f"  expected {expected}{why}"))

print(f"{passed}/{len(tests)} passed")
