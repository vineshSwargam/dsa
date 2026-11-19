# Subsets II
# Medium
# Topics
# Company Tags
# Hints

# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

# The solution must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,1]

# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

# Example 2:

# Input: nums = [7,7]

# Output: [[],[7], [7,7]]

# Constraints:

# 1 <= nums.length <= 11
# -20 <= nums[i] <= 20



# Topics

# Array Backtracking Bit Manipulation


# Recommended Time & Space Complexity

# You should aim for a solution as good or better than O(n * (2^n)) time and O(n) space, where n is the size of the input array.



# Hint 1

# A brute-force solution would involve creating a hash set and inserting every subset into it. Then, converting the hash set to a list and returning it. However, this approach would require extra space of O(2^n). Can you think of a better way? Maybe you should sort the input array and observe which recusive calls are resposible to make duplicate subsets.



# Hint 2

# We can use backtracking to generate subsets of an array. If the input contains duplicates, duplicate subsets may be created. To prevent this, we sort the array beforehand. For example, in [1, 1, 2], sorting allows us to create subsets using the first 1 and skip the second 1, ensuring unique subsets. How can you implement this?



# Hint 3

# We start by sorting the input array. Then, we recursively iterate through the array from left to right, extending recursive paths by including or excluding each element. To avoid duplicate subsets, we skip an element if it is the same as the previous one. Finally, we return the generated subsets as a list.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 81.7%


from typing import List
from collections import Counter
import traceback


class Solution:
    def using_recur_bt(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        nums.sort()
        nl = len(nums)

        def bt(i):
            if i >= nl:
                res.append(sub.copy())
                return

            sub.append(nums[i])
            bt(i+1)

            sub.pop()
            while i+1 < nl and nums[i+1] == nums[i]:
                i += 1
            bt(i+1)

        bt(0)
        return res



    def subsets_for_loop(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        nl = len(nums)

        # [ 1, 2, 3 ] => [ [], [1], [2], [3], [1, 2], [1, 3], [1, 2, 3], [2, 3] ]
        # now if you have [1, 2, 1] => [ [], [1], [2], [1], [1, 2], [2, 1], [1, 2, 1]
        # you'd have to sort it first to avoid adding duplicate items
        # [1, 1, 2] => [ [], continue, [1], [2], [1, 2] ]

        def bt(sub, lb):
            res.append(sub.copy())
            for i in range(lb, nl):
                if i>lb and nums[i] == nums[i-1]:
                    continue
                sub.append(nums[i]) # []
                bt(sub, i+1)
                sub.pop()

        bt([], 0)
        return res

    
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # return self.subsets_for_loop(nums)
        return self.using_recur_bt(nums)


sol = Solution()

# run from the repo root: python3 -m backtracking.subsets_ii
# (nums, expected) - any order is accepted, both for the subsets and for the values inside each subset
# expected is either the full answer, or (for the big cases) just how many subsets there should be.
# For a count, every subset you return is also checked: it must not use a value more times than it
# appears in nums, and no subset may appear twice (in any order).
tests = [
    ([1,2,1], [[],[1],[1,2],[1,1],[1,2,1],[2]]),                # example 1
    ([7,7], [[],[7],[7,7]]),                                    # example 2
    ([0], [[],[0]]),                                            # zero is a real value
    ([-20,20], [[],[-20],[20],[-20,20]]),                       # no duplicates at all, value limits
    ([1,1,1], [[],[1],[1,1],[1,1,1]]),                          # only duplicates: pick 0, 1, 2 or 3 of them
    ([2,1,2,1], [[],[1],[1,1],[2],[2,2],[1,2],[1,1,2],[1,2,2],[1,1,2,2]]),   # two pairs, unsorted
    ([4,4,4,1,4], [[],[1],[4],[1,4],[4,4],[1,4,4],[4,4,4],[1,4,4,4],[4,4,4,4],[1,4,4,4,4]]),   # the odd one out in the middle
    ([3]*11, [[3]*k for k in range(12)]),                       # max length, all the same: only 12 answers, not 2048
    (list(range(1, 12)), 2048),                                 # max length, all different: every one of the 2^11 subsets
    ([1,1,2,2,3,3,4,4,5,5,6], 486),                             # max length, five pairs
    ([-20,20,0,-20,20,0,5,5,5,-1,-1], 324),                     # max length, unsorted, mixed repeats
]

def normal(subsets):
    """Ignore order: sort inside each subset, then sort the list of subsets. Duplicates still count."""
    return sorted(sorted(s) for s in subsets)

def check(nums, got, expected):
    if not isinstance(got, list):
        return False, ""
    if isinstance(expected, list):
        return normal(got) == normal(expected), ""
    have = Counter(nums)
    for s in got:
        if Counter(s) - have:
            return False, f"  {list(s)} uses a value more times than it appears in nums"
    if len(set(map(tuple, normal(got)))) != len(got):
        return False, "  the same subset appears more than once"
    return len(got) == expected, ""

passed = 0
for nums, expected in tests:
    try:
        got = sol.subsets_with_dup(list(nums))
        ok, why = check(nums, got, expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} subsets" if isinstance(got, list) and len(got) > 12 else got
    want = expected if isinstance(expected, int) else f"{len(expected)} subsets {expected}"
    print(f"{'PASS' if ok else 'FAIL'}  {nums} -> {shown}" + ("" if ok else f"  expected {want}{why}"))

print(f"{passed}/{len(tests)} passed")
