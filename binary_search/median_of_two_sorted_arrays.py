# Median of Two Sorted Arrays
# Hard
# Topics
# Company Tags
# Hints
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution should run in 
# O
# (
# l
# o
# g
# (
# m
# +
# n
# )
# )
# O(log(m+n)) time.


# Example 1:

# Input: nums1 = [1,2], nums2 = [3]

# Output: 2.0
# Explanation: Among [1, 2, 3] the median is 2.


# Example 2:

# Input: nums1 = [1,3], nums2 = [2,4]

# Output: 2.5
# Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.


# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6


# Topics

  

# Recommended Time & Space Complexity
# You should aim for a solution with O(log(min(n, m))) time and O(1) space, where n is the size of nums1 and m is the size of nums2.


# Hint 1
# A brute force solution would be to create a new array by merging elements from both arrays, then sorting it and returning the median. This would be an O(n + m) solution. Can you think of a better way? Maybe you can use the criteria of both the arrays being sorted in ascending order.


# Hint 2
# Suppose we merged both arrays. Then, we would have half = (m + n) / 2 elements to the left of the median. So, without merging, is there any way to use this information to find the median? You can leverage the fact that the arrays are sorted. Consider the smaller array between the two and use binary search to find the correct partition between the two arrays, which will allow you to directly find the median without fully merging the arrays. How will you implement this?


# Hint 3
# We will always try to keep array A smaller and interchange it with array B if len(A) > len(B). Now, we perform binary search on the number of elements we will choose from array A. It is straightforward that when we choose x elements from array A, we have to choose half - x elements from array B. But we should also ensure that this partition is valid. How can we do this?


# Hint 4
# When we do a partition for both arrays, we should ensure that the maximum elements from the left partitions of both arrays are smaller than or equal to the minimum elements of the right partitions of both the arrays. This will ensure that the partition is valid, and we can then find the median. We can find the min or max of these partitions in O(1) as these partitions are sorted in ascending order. Why does this work?


# Hint 5
# For example, consider the arrays A = [1, 2, 3, 4, 5] and B = [1, 2, 3, 4, 5, 6, 7, 8]. When we select x = 2, we take 4 elements from array B. However, this partition is not valid because value 4 from the left partition of array B is greater than the value 3 from the right partition of array A. So, we should try to take more elements from array A to make the partition valid. Binary search will eventually help us find a valid partition.

class Solution:
    

    def find_median_sorted_arrays(self, nums1, nums2) -> float:
        n1l = len(nums1)
        n2l = len(nums2)

        if n1l <= n2l:
            sml = nums1 # smaller list
            lgl = nums2 # larger list
        else:
            sml = nums2 # smaller list
            lgl = nums1 # larger list

        sml_len = len(sml) # 5
        lgl_len = len(lgl) # 6
        tot_len = sml_len + lgl_len # 11
        half = tot_len//2 # 5

        def get_median(sm_lh_end, sm_rh_start, lg_lh_end, lg_rh_start):
            max_left = max(sm_lh_end, lg_lh_end)
            min_right = min(sm_rh_start, lg_rh_start)
            if tot_len % 2 == 0:
                return (max_left + min_right)/2
            return min_right

        def binary_search(l, r):
            i = (l+r)//2 # 5

            j = half - i # 5-2 = 3
            sm_lh_end = sml[i-1] if i > 0 else float('-inf')
            sm_rh_start = sml[i] if i < sml_len else float('inf')
            lg_lh_end = lgl[j-1] if j > 0 else float('-inf')
            lg_rh_start = lgl[j] if j < lgl_len else float('inf')
            
            if sm_lh_end > lg_rh_start:
                return binary_search(l, i-1)
            if sm_rh_start < lg_lh_end:
                return binary_search(i+1, r)

            return get_median(sm_lh_end, sm_rh_start, lg_lh_end, lg_rh_start)
        
        return binary_search(0, sml_len) # 2
        
        


sol = Solution()

a, b = [1,2], [3]                                    # 2.0  - example 1, odd total
# a, b = [1,3], [2,4]                                # 2.5  - example 2, even total
# a, b = [1,50,60,80,100], [70,90,95,110,120]        # 85.0 - your first walkthrough (i = 4)
# a, b = [1,50,60,80,100], [59,85,90,95,100]         # 82.5 - your second walkthrough, duplicate 100
# a, b = [10,20,30,40], [1,2,3,4,5,6]                # 5.5  - shorter array all bigger (i = 0)
# a, b = [2,8,15], [1,4,9,12,20]                     # 8.5  - interleaved
# a, b = [1,2,3], [7,8,9,10]                         # 7.0  - shorter array all smaller (i = len), odd total
# a, b = [], [1]                                     # 1.0  - one array empty
# a, b = [], [2,3]                                   # 2.5  - one array empty, even total
# a, b = [5], []                                     # 5.0  - empty array passed second
# a, b = [1,1,1], [1,1]                              # 1.0  - all duplicates
# a, b = [-5,-3], [-4,-2,-1]                         # -3.0 - negatives
# a, b = [3], [1,2,4,5]                              # 3.0  - single element lands in the middle
print(sol.find_median_sorted_arrays(a, b))