# Largest Rectangle In Histogram
# Hard
# Topics
# Company Tags
# Hints
# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

# Return the area of the largest rectangle that can be formed among the bars.

# Note: This chart is known as a histogram.


# Example 1:



# Input: heights = [7,1,7,2,2,4]

# Output: 8

# Example 2:



# Input: heights = [1,3,7]

# Output: 7

# Constraints:

# 1 <= heights.length <= 100,000.
# 0 <= heights[i] <= 10,000


# Topics

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A rectangle has a height and a width. Can you visualize how rectangles are formed in the given input? Considering one bar at a time might help. We can try to form rectangles by going through every bar and current bar's height will be the height of the rectangle. How can you determine the width of the rectangle for the current bar being the height of the rectangle? Extending the current bar to the left and right might help determine the rectangle's width.


# Hint 2
# For a bar with height h, try extending it to the left and right. We can see that we can't extend further when we encounter a bar with a smaller height than h. The width will be the number of bars within this extended range. A brute force solution would be to go through every bar and find the area of the rectangle it can form by extending towards the left and right. This would be an O(n^2) solution. Can you think of a better way? Maybe precomputing the left and right boundaries might be helpful.


# Hint 3
# The left and right boundaries are the positions up to which we can extend the bar at index i. The area of the rectangle will be height[i] * (right - left + 1), which is the general formula for height * width. These boundaries are determined by the first smaller bars encountered to the left and right of the current bar. How can we find the left and right boundaries now? Maybe a data structure is helpful.


# Hint 4
# We can use a stack with a monotonically strictly increasing nature, but instead of storing values, we store indices in the stack and perform operations based on the values at those indices. The top of the stack will represent the smaller bar that we encounter while extending the current bar. To find the left and right boundaries, we perform this algorithm from left to right and vice versa, storing the boundaries. Then, we iterate through the array to find the area for each bar and return the maximum area we get.


class Solution:
    def largest_rectangle_area(self, heights) -> int:
        hlen = len(heights)
        lr_bounds = [[0, 0] for _ in range(hlen)]
        max_area = 0
        bound_stack = []

        def calc_area(ind):
            width = lr_bounds[ind][1] - lr_bounds[ind][0] + 1
            return heights[ind] * width


        # go right to left found left boundary
        for i in range(hlen-1, -1, -1):
            while bound_stack and heights[i] < heights[bound_stack[-1]]:
                popped_ind = bound_stack.pop()
                lr_bounds[popped_ind][0] = i+1

            bound_stack.append(i)

        # flush out the stack since they didn't have any lesser index found
        while len(bound_stack) > 0:
            lr_bounds[bound_stack.pop()][0] = 0

        
        # go left to right found right boundary
        for i in range(hlen):
            while bound_stack and heights[i] < heights[bound_stack[-1]]:
                popped_ind = bound_stack.pop()
                lr_bounds[popped_ind][1] = i-1
                max_area = max(calc_area(popped_ind), max_area)

            bound_stack.append(i)

        # flush out the stack since they didn't have any lesser index found
        while len(bound_stack) > 0:
            popped_ind = bound_stack.pop()
            lr_bounds[popped_ind][1] = hlen-1
            max_area = max(calc_area(popped_ind), max_area)

        return max_area



sol = Solution()

hts = [7,1,7,2,2,4] # 8
# hts = [1,3,7] # Output: 7
print(sol.largest_rectangle_area(hts))