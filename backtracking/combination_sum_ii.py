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


class Solution:
    def using_recur_bt(self, nums: List[int], tar: int) -> List[List[int]]:
        res = []
        sub = set()
        nl = len(nums)

        def bt(i, tot):
            left = tar - tot
            if left == 0:
                res.append(sub)
                return
            if i >= nl or left < 0 or nums[i] in sub:
                return
            
            sub.append(nums[i])
            bt(i+1, tot+nums[i])
            sub.pop()
            bt(i+1, tot)
        
        bt(0, 0)

    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.using_recur_bt(candidates, target)


sol = Solution()
candidates, target = [9,2,2,4,6,1,5], 8 # Output [
# candidates, target = [1,2,3,4,5], 7 # Output [



print(sol.combination_sum2(candidates, target))
