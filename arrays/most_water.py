# Container With Most Water
# Medium
# Topics
# Company Tags
# Hints
# You are given an integer array heights where heights[i] represents the height of the 
# i
# t
# h
# i 
# th
#   bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.


# Example 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Explanation: The bars at indices 1 and 7 have heights 7 and 6. The container has width 7 - 1 = 6 and height min(7, 6) = 6, so it can store 6 * 6 = 36 units of water. This is the maximum possible area.


# Example 2:

# Input: height = [2,2,2]

# Output: 4

# Constraints:

# 2 <= height.length <= 100,000
# 0 <= height[i] <= 10,000


# Topics

  

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to try all pairs of bars in the array, compute the water for each pair, and return the maximum water among all pairs. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# Can you think of an algorithm that runs in linear time and is commonly used in problems that deal with pairs of numbers? Find a formula to calculate the amount of water when we fix two heights.


# Hint 3
# We can use the two pointer algorithm. One pointer is at the start and the other at the end. At each step, we calculate the amount of water using the formula (j - i) * min(heights[i], heights[j]). Then, we move the pointer that has the smaller height value. Can you think why we only move the pointer at smaller height?


# Hint 4
# If heights[i] is smaller, then any future container using index i will have a smaller width, and its height is still at most heights[i]. So it cannot produce a larger area than the current pair. Therefore, we can safely discard the smaller height and move that pointer inward. The same logic applies when heights[j] is smaller.

class Solution:
    def max_area(self, heights):
        nl = len(heights)
        i = 0
        j = nl-1
        max_area = 0

        while i<j:
            av_ht = min(heights[i], heights[j])
            av_wd = j - i
            area = av_wd * av_ht
            max_area = max(area, max_area)

            if heights[j] <= heights[i]:
                j -= 1
            else:
                i += 1
        
        return max_area




sol = Solution()

hts = [1,7,2,5,4,7,3,6] # Output: 36

print(sol.max_area(hts))