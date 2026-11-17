# Combination Sum
# Medium
# Topics
# Company Tags
# Hints

# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input:
# nums = [2,5,6,9]
# target = 9

# Output: [[2,2,5],[9]]

# Explanation:
# 2 + 2 + 5 = 9. We use 2 twice, and 5 once.
# 9 = 9. We use 9 once.

# Example 2:

# Input:
# nums = [3,4,5]
# target = 16

# Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

# Example 3:

# Input:
# nums = [3]
# target = 5

# Output: []

# Constraints:

# All elements of nums are distinct.
# 1 <= nums.length <= 20
# 2 <= nums[i] <= 30
# 2 <= target <= 30



# Topics

# Array Backtracking


# Recommended Time & Space Complexity

# You should aim for a solution with O(2^(t/m)) time and O(t/m) space, where t is the given target and m is the minimum value in the given array.



# Hint 1

# Can you think of this problem in terms of a decision tree, where at each step, we have n decisions, where n is the size of the array? In this decision tree, we can observe that different combinations of paths are formed. Can you think of a base condition to stop extending a path? Maybe you should consider the target value.



# Hint 2

# We can use backtracking to recursively traverse these paths and make decisions to choose an element at each step. We maintain a variable sum, which represents the sum of all the elements chosen in the current path. We stop this recursive path if sum == target, and add a copy of the chosen elements to the result. How do you implement it?



# Hint 3

# We recursively traverse the array starting from index i. At each step, we select an element from i to the end of the array. We extend the recursive path with elements where sum <= target after including that element. This creates multiple recursive paths, and we append the current list to the result whenever the base condition is met.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 78.8%


from typing import List
import traceback


class Solution:
    def using_dfs_bt(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        nl = len(nums)

        def bt(i, tot):
            left = target - tot
            if left < 0 or i >= nl:
                return
            if left == 0:
                res.append(sub.copy())
                return
            sub.append(nums[i])
            bt(i, tot+nums[i])
            sub.pop()
            bt(i+1, tot)
        
        bt(0, 0)
        return res

    def combination_sum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.using_dfs_bt(nums, target)


sol = Solution()

# run from the repo root: python3 -m backtracking.combination_sum
# (nums, target, expected) - any order is accepted, both for the combinations and for the numbers inside each one
# expected is either the full answer, or (for the big cases) just how many combinations there should be.
# For a count, every combination you return is also checked: it must add up to target, use only numbers
# from nums, and not repeat another combination in a different order.
big_20 = list(range(2, 22))                                   # 20 numbers 2..21, sorted
big_20_mixed = [21,2,20,3,19,4,18,5,17,6,16,7,15,8,14,9,13,10,12,11]   # the same 20 numbers, unsorted
high_20 = list(range(11, 31))                                 # 20 numbers, all at least 11: no number can be used 3 times

tests = [
    ([2,5,6,9], 9, [[2,2,5],[9]]),                              # example 1
    ([3,4,5], 16, [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]), # example 2
    ([3], 5, []),                                               # example 3, nothing works
    ([2], 2, [[2]]),                                            # smallest case, the number is the target
    ([2], 30, [[2]*15]),                                        # one number reused 15 times
    ([7], 30, []),                                              # reuse never lands exactly on the target
    ([30], 30, [[30]]),                                         # value limits
    ([8,9,10], 7, []),                                          # every number is bigger than the target
    ([4,6], 11, []),                                            # even numbers, odd target
    ([2,3], 6, [[2,2,2],[3,3]]),                                # [2,2,2] and [3,3] only, no reordered copies
    ([2,3,6,7], 7, [[2,2,3],[7]]),                              # classic
    ([5,3,2], 8, [[2,2,2,2],[2,3,3],[3,5]]),                    # unsorted input
    (high_20, 30, [[11,19],[12,18],[13,17],[14,16],[15,15],[30]]),  # max length, 15 + 15 reuses one number
    ([2,3,5], 30, 21),                                          # many combinations from few numbers
    (big_20, 30, 1017),                                         # max length, small numbers: 1017 combinations
    (big_20_mixed, 30, 1017),                                   # same, unsorted
]

def normal(combos):
    """Ignore order: sort inside each combination, then sort the list. Duplicates still count."""
    return sorted(sorted(c) for c in combos)

def check(nums, target, got, expected):
    if not isinstance(got, list):
        return False, ""
    if isinstance(expected, list):
        return normal(got) == normal(expected), ""
    allowed = set(nums)
    for c in got:
        if sum(c) != target:
            return False, f"  {c} adds up to {sum(c)}, not {target}"
        if not set(c) <= allowed:
            return False, f"  {c} uses a number that is not in nums"
    if len(set(map(tuple, normal(got)))) != len(got):
        return False, "  the same combination appears more than once"
    return len(got) == expected, ""

passed = 0
for nums, target, expected in tests:
    try:
        got = sol.combination_sum(list(nums), target)
        ok, why = check(nums, target, got, expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} combinations" if isinstance(got, list) and len(got) > 8 else got
    want = expected if isinstance(expected, int) or len(expected) <= 8 else f"{len(expected)} combinations"
    nums_shown = nums if len(nums) <= 6 else f"[{len(nums)} numbers]"
    print(f"{'PASS' if ok else 'FAIL'}  {nums_shown} target={target} -> {shown}" + ("" if ok else f"  expected {want}{why}"))

print(f"{passed}/{len(tests)} passed")
