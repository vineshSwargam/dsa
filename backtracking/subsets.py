# Subsets
# Medium
# Topics
# Company Tags
# Hints

# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [7]

# Output: [[],[7]]

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10



# Topics

# Array Backtracking Bit Manipulation


# Recommended Time & Space Complexity

# You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the size of the input array.



# Hint 1

# It is straightforward that if the array is empty we return an empty array. When we have an array [1] which is of size 1, we have two subsets, [[], [1]] as the output. Can you think why the output is so?



# Hint 2

# We can see that one subset includes a number, and another does not. From this, we can conclude that we need to find the subsets that include a number and those that do not. This results in 2^n subsets for an array of size n because there are many combinations for including and excluding the array of numbers. Since the elements are unique, duplicate subsets will not be formed if we ensure that we don't pick the element more than once in the current subset. Which algorithm is helpful to generate all subsets, and how would you implement it?



# Hint 3

# We can use backtracking to generate all possible subsets. We iterate through the given array with an index i and an initially empty temporary list representing the current subset. We recursively process each index, adding the corresponding element to the current subset and continuing, which results in a subset that includes that element. Alternatively, we skip the element by not adding it to the subset and proceed to the next index, forming a subset without including that element. What can be the base condition to end this recursion?



# Hint 4

# When the index i reaches the end of the array, we append a copy of the subset formed in that particular recursive path to the result list and return. All subsets of the given array are generated from these different recursive paths, which represent various combinations of "include" and "not include" steps for the elements of the array. As we are only iterating from left to right in the array, we don't pick an element more than once.



# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 85.1%


from typing import List
from itertools import combinations
import traceback


class Solution:
    def using_rec_dfs(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    def using_backtracking(self, nums: List[int]) -> List[List[int]]:
        res = [] # result array containing all valid subset states
        nl = len(nums) # nl is nums length
        def bt(st, lb): # st is state, lb is lower bound
            res.append(st.copy()) # [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]
            if lb >= nl:
                return
            for i in range(lb, nl):
                st.append(nums[i])
                bt(st, i+1)
                st.pop()
        
        bt([], 0)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.using_backtracking(nums)
        return self.using_rec_dfs(nums)


sol = Solution()

# run from the repo root: python3 -m backtracking.subsets
# (nums, expected) - any order is accepted, both for the subsets and for the values inside each subset
def every_subset(nums):
    """All 2^n subsets, only used to write the expected answer for the big cases."""
    return [list(c) for size in range(len(nums) + 1) for c in combinations(nums, size)]

ten = list(range(10))                       # max length, 1024 subsets
ten_mixed = [10,-10,9,-9,0,5,-5,3,-3,1]     # max length, negatives, unsorted, value limits

tests = [
    ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),     # example 1
    ([7], [[],[7]]),                                            # example 2
    ([0], [[],[0]]),                                            # zero is a real value, [0] is not the same as []
    ([-10], [[],[-10]]),                                        # single negative, value limit
    ([1,2], [[],[1],[2],[1,2]]),                                # two values, 4 subsets
    ([3,1,2], [[],[3],[1],[2],[3,1],[3,2],[1,2],[3,1,2]]),      # unsorted input
    ([-10,10], [[],[-10],[10],[-10,10]]),                       # both value limits
    ([5,-3,0,7], every_subset([5,-3,0,7])),                     # 16 subsets, mixed signs
    (ten, every_subset(ten)),                                   # max length, 1024 subsets
    (ten_mixed, every_subset(ten_mixed)),                       # max length, mixed values
]

def normal(subsets):
    """Ignore order: sort inside each subset, then sort the list of subsets. Duplicates still count."""
    return sorted(sorted(s) for s in subsets)

passed = 0
for nums, expected in tests:
    try:
        got = sol.subsets(list(nums))
        ok = isinstance(got, list) and normal(got) == normal(expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False
    passed += ok
    if isinstance(got, list) and len(got) > 16:
        shown = f"{len(got)} subsets"
    else:
        shown = got
    extra = "" if ok else f"  expected {len(expected)} subsets" + (f" {expected}" if len(expected) <= 16 else "")
    print(f"{'PASS' if ok else 'FAIL'}  {nums} -> {shown}{extra}")

print(f"{passed}/{len(tests)} passed")
