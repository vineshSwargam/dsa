# Products of Array Except Self
# Medium
# Topics
# Company Tags
# Hints
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 100,000
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# Topics

 

# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute-force solution would be to iterate through the array with index i and compute the product of the array except for that index element. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# Is there a way to avoid the repeated work? Maybe we can store the results of the repeated work in an array.


# Hint 3
# We can use the prefix and suffix technique. First, we iterate from left to right and store the prefix products for each index in a prefix array, excluding the current index's number. Then, we iterate from right to left and store the suffix products for each index in a suffix array, also excluding the current index's number. Can you figure out the solution from here?


# Hint 4
# We can use the stored prefix and suffix products to compute the result array by iterating through the array and simply multiplying the prefix and suffix products at each index. -->


class Solution:
    def product_except_self(self, nums):
        # prod = 1
        # prod_zero = 1
        # zero_counter = 0
        # zero_index = []
        # for i, n in enumerate(nums):
        #     if n == 0:
        #         zero_index.append(i)
        #         zero_counter += 1
        #         prod = 0
        #         if zero_counter > 1:
        #             prod_zero = 0
        #             break
                
        #         continue
            
        #     prod *= n
        #     prod_zero *= n

        # if prod_zero == 0:
        #     return [0]*len(nums)

        # res = []
        # for i, n in enumerate(nums):
        #     if i in zero_index:
        #         res.append(prod_zero)
        #     else:
        #         res.append(int(prod/n))
        
        # return res

        # two pointer trial

        # n = len(nums) # 5
        # ltr_prod = []
        # rtl_prod = [1]*n
        # i = 0
        # j=n-1
        # print(nums)

        # while i<n and j>=0: # 0, 4
        #     if i > 0:
        #         l_prod = ltr_prod[i-1] # get last computed prod val till this index
        #     else:
        #         l_prod = 1 # no prod values exist in the array yet

        #     ltr_prod.append(l_prod*nums[i]) # multiply curr val with last known prod val
            
        #     if j < n-1:
        #         r_prod = rtl_prod[j+1] # get last computed prod val till this index
        #     else:
        #         r_prod = 1 # no prod values exist in the array yet

        #     rtl_prod[j] = r_prod*nums[j] # multiply curr val with last known prod val

        #     i+=1
        #     j-=1
        
        # res = []
        # for ind in range(n):
        #     prod = 1
        #     if ind-1<0:
        #         prod = rtl_prod[ind+1]
        #     elif ind+1 >= n:
        #         prod = ltr_prod[ind-1]
        #     else:
        #         prod = ltr_prod[ind-1] * rtl_prod[ind+1]
            
        #     res.append(prod)

        # return res

        # optimised prefix postfix
        n = len(nums)
        res = [0]*n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res



sol = Solution()
print(sol.product_except_self([1, 2, 3, 4, 5]))
# print(sol.product_except_self([1, 2, 4, 6, 0]))
# print(sol.product_except_self([-1,0,1,2,3]))
