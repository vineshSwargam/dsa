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


class Solution:
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:


sol = Solution()
nums = [1,2,1] # Output [[],[1],[1,2],[1,1],[1,2,1],[2]]
# nums = [7,7] # Output [[],[7], [7,7]]



print(sol.subsets_with_dup(nums))
