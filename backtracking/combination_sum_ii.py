# Combination Sum II
# Medium
# Topics
# Company Tags
# Hints

# You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input: candidates = [9,2,2,4,6,1,5], target = 8

# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]

# Example 2:

# Input: candidates = [1,2,3,4,5], target = 7

# Output: [
#   [1,2,4],
#   [2,5],
#   [3,4]
# ]

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30



# Topics

# Array Backtracking


# Recommended Time & Space Complexity

# You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the size of the input array.



# Hint 1

# A brute-force solution would be to create a hash set, which is used to detect duplicates, to get combinations without duplicates. Can you think of a better way without using a hash set? Maybe you should sort the input array and observe the recursive calls that are responsible for duplicate combinations.



# Hint 2

# We can use backtracking to generate all combinations whose sum equals the given target. When the input array contains duplicate elements, it may result in duplicate combinations. To avoid this, we can sort the array. Why does sorting help? Because as we traverse the array from left to right, we form combinations with the current element. By skipping duplicate elements, we ensure that the same combinations are not repeated for identical elements. How can you implement this?



# Hint 3

# We recursively traverse the given array starting at index i, with a variable sum representing the sum of the picked elements. We explore elements from i to the end of the array and extend the recursive path if adding the current element results in sum <= target. When we processed an element, we backtrack and proceed to the next distinct element, skipping any similar elements in the middle to avoid duplicate combinations.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 61.2%


from typing import List
from collections import Counter
import traceback


class Solution:
    def using_recur_bt(self, nums: List[int], tar: int) -> List[List[int]]:
        res = set()
        sub = []
        nl = len(nums)

        def bt(i, tot):
            left = tar - tot
            if left == 0:
                res.add(tuple(sorted(sub)))
                return
            if i >= nl or left < 0:
                return
            
            sub.append(nums[i])
            bt(i+1, tot+nums[i])
            sub.pop()
            bt(i+1, tot)
        
        bt(0, 0)
        return [list(sub) for sub in res]

    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.using_recur_bt(candidates, target)


sol = Solution()

# run from the repo root: python3 -m backtracking.combination_sum_ii
# (candidates, target, expected) - any order is accepted, both for the combinations and for the numbers inside each one
# expected is either the full answer, or (for the big cases) just how many combinations there should be.
# For a count, every combination you return is also checked: it must add up to target, not use a number
# more times than it appears in candidates, and not repeat another combination in a different order.
ones_100 = [1] * 100                                    # 100 copies of the same number
fifties_100 = [50] * 100                                # 100 numbers, all bigger than any target
one_to_25_x4 = list(range(1, 26)) * 4                   # 1..25 four times each, 100 numbers
one_to_50_x2 = list(range(1, 51)) + list(range(50, 0, -1))   # 1..50 twice each, unsorted, 100 numbers

tests = [
    ([9,2,2,4,6,1,5], 8, [[1,2,5],[2,2,4],[2,6]]),      # example 1
    ([1,2,3,4,5], 7, [[1,2,4],[2,5],[3,4]]),            # example 2
    ([1], 1, [[1]]),                                    # single number, it is the target
    ([2], 1, []),                                       # single number, too big
    ([3], 6, []),                                       # a number can't be reused: 3 + 3 is not allowed
    ([1,1], 2, [[1,1]]),                                # two copies of 1 are two different numbers, both usable
    ([1,1,1], 2, [[1,1]]),                              # three ways to pick two 1s, but only one answer
    ([2,2,2], 4, [[2,2]]),                              # same trap with 2s
    ([1,1,1,1,1], 3, [[1,1,1]]),                        # ten ways to pick, one answer
    ([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]),   # classic
    ([2,5,2,1,2], 5, [[1,2,2],[5]]),                    # unsorted, a repeated number used twice
    ([50,30], 30, [[30]]),                              # value limits, 50 is above the target
    (ones_100, 30, [[1]*30]),                           # 100 copies: one answer, but a huge number of ways to pick it
    (fifties_100, 30, []),                              # 100 numbers, none fit
    (one_to_25_x4, 30, 3014),                           # max length, lots of repeats
    (one_to_50_x2, 30, 1225),                           # max length, value limits, unsorted
]

def normal(combos):
    """Ignore order: sort inside each combination, then sort the list. Duplicates still count."""
    return sorted(sorted(c) for c in combos)

def check(candidates, target, got, expected):
    if not isinstance(got, list):
        return False, ""
    if isinstance(expected, list):
        return normal(got) == normal(expected), ""
    have = Counter(candidates)
    for c in got:
        if sum(c) != target:
            return False, f"  {c} adds up to {sum(c)}, not {target}"
        if Counter(c) - have:
            return False, f"  {c} uses a number more times than it appears in candidates"
    if len(set(map(tuple, normal(got)))) != len(got):
        return False, "  the same combination appears more than once"
    return len(got) == expected, ""

passed = 0
for candidates, target, expected in tests:
    try:
        got = sol.combination_sum2(list(candidates), target)
        ok, why = check(candidates, target, got, expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} combinations" if isinstance(got, list) and len(got) > 8 else got
    want = expected if isinstance(expected, int) or len(expected) <= 8 else f"{len(expected)} combinations"
    cands_shown = candidates if len(candidates) <= 8 else f"[{len(candidates)} numbers]"
    print(f"{'PASS' if ok else 'FAIL'}  {cands_shown} target={target} -> {shown}" + ("" if ok else f"  expected {want}{why}"))

print(f"{passed}/{len(tests)} passed")
