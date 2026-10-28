# Trapping Rain Water
# Hard
# Topics
# Company Tags
# Hints
# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the total amount of water that can be trapped between the bars.


# Example 1:



# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9
# Constraints:

# 1 <= height.length <= 20,000
# 0 <= height[i] <= 100,000


# Topics

    

# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# How can we determine the amount of water that can be trapped at a specific position in the array? Perhaps looking at the image might help clarify.


# Hint 2
# From the image, we can see that to calculate the amount of water trapped at a position, the greater element to the left l and the greater element to the right r of the current position are crucial. The formula for the trapped water at index i is given by: min(height[l], height[r]) - height[i].


# Hint 3
# A brute force solution would involve iterating through the array with index i, finding the greater elements to the left (l) and right (r) for each index, and then calculating the trapped water for that position. The total amount of trapped water would be the sum of the water trapped at each index. Finding l and r for each index involves repeated work, resulting in an O(n^2) solution. Can you think of a more efficient approach? Maybe there is something that we can precompute and store in arrays.


# Hint 4
# We can store the prefix maximum in an array by iterating from left to right and the suffix maximum in another array by iterating from right to left. For example, in [1, 5, 2, 3, 4], for the element 3, the prefix maximum is 5, and the suffix maximum is 4. Once these arrays are built, we can iterate through the array with index i and calculate the total water trapped at each position using the formula: min(prefix[i], suffix[i]) - height[i].

class Solution:
    def using_pref_suf(self, height):
        # lets write a stupid solution
        hl = len(height)
        max_ht = height[0]
        pref_area = [0] * hl
        suf_area = [0] * hl
        area = 0

        # [ 0, 2, 0, 3, 1, 0, 1, 3, 2, 1 ] 

        for i in range(hl):
            if height[i] == max_ht:
                pref_area[i] = 0
            elif height[i] > max_ht:
                pref_area[i] = 0
                max_ht = height[i]
            else:
                pref_area[i] = max_ht - height[i]

        max_ht = height[hl-1]

        for i in range(hl-1, -1, -1):
            if height[i] == max_ht:
                suf_area[i] = 0
            elif height[i] > max_ht:
                suf_area[i] = 0
                max_ht = height[i]
            else:
                suf_area[i] = max_ht - height[i]

        for i in range(hl):
            area += min(pref_area[i], suf_area[i])
        
        return area

    
    def using_two_pointers(self, height):
        hl = len(height)
        i = 0
        j = hl-1
        left_max = height[i]
        right_max = height[j]
        area = 0

        while i<j:
            if height[i] >= left_max:
                left_max = height[i]

            if height[j] >= right_max:
                right_max = height[j]

            if left_max <= right_max:
                area += left_max - height[i]
                i += 1
            else:
                area += right_max - height[j]
                j -= 1

        return area


    def trap(self, height) -> int:
        # return self.using_pref_suf(height)
        return self.using_two_pointers(height)
        
            





sol = Solution()

hts = [0,2,0,3,1,0,1,3,2,1] # Output: 9

print(sol.trap(hts))