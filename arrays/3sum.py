# 3Sum
# Medium
# Topics
# Company Tags
# Hints
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5


# Topics

  

# Recommended Time & Space Complexity
# You should aim for a solution with O(n^2) time and O(1) auxiliary space, plus the space used by the sorting algorithm, where n is the size of the input array. This excludes the space used for the output list.

# In Python (CPython), nums.sort() modifies the list in place but can use O(n) auxiliary space in the worst case.


# Hint 1
# A brute force solution would be to check for every triplet in the array. This would be an O(n^3) solution. Can you think of a better way?


# Hint 2
# Can you think of an algorithm after sorting the input array? What can we observe by rearranging the given equation in the problem?


# Hint 3
# We can iterate through nums with index i and get nums[i] = -(nums[j] + nums[k]) after rearranging the equation, making -nums[i] = nums[j] + nums[k]. For each index i, we should efficiently calculate the j and k pairs without duplicates. Which algorithm is suitable to find j and k pairs?


# Hint 4
# To efficiently find the j and k pairs, we run the two pointer approach on the elements to the right of index i as the array is sorted. When we run two pointer algorithm, consider j and k as pointers (j is at left, k is at right) and target = -nums[i], if the current sum num[j] + nums[k] < target then we need to increase the value of current sum by incrementing j pointer. Else if the current sum num[j] + nums[k] > target then we should decrease the value of current sum by decrementing k pointer. How do you deal with duplicates?


# Hint 5
# When the current sum nums[j] + nums[k] == target add this pair to the result. We can move j or k pointer until j < k and the pairs are repeated. This ensures that no duplicate pairs are added to the result.

from collections import defaultdict

class Solution:

    def using_hash(self, nums):
        freq = defaultdict(int)
        nums.sort()
        print(nums)
        nl = len(nums)
        res = []

        # freq dict
        for num in nums:
            freq[num] += 1

        # i, j loop
        for i, ni in enumerate(nums):
            if ni > 0:
                break

            if i > 0  and ni == nums[i-1]:
                continue

            print('i -', i)
            f = freq.copy()
            for j in range(i+1, nl-1):
                nj = nums[j]
                f[nj] -= 1
                if j > i+1 and nj == nums[j-1]:
                    # print('skipping - ', nums[j], 'at index -', j, ' since nums[j-1] is - ', nums[j-1])
                    continue
                # print('j:', j)
                # print('nums[j-1]:', nums[j-1], 'nj:', nj)
                # print('==================')

                tar = 0 - ni - nj

                # find k in freq, then decrement k freq from freq dict
                if tar >= nj and tar in f and f[tar] > 0:
                    res.append((ni, nj, tar))
                    f[tar] -= 1

            # reset freq on j loop end


        return res


    def using_two_sum(self, nums):
        #[-1,0,1,2,-1,-4]
        nl = len(nums)
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        print(nums)
        res = []
        
        for (k, n) in enumerate(nums):
            # 0 -> -4
            if k > 0 and n == nums[k-1]:
                continue
            
            target = 0 - n # 4
            i = k+1
            j = nl-1 # 5

            while i < j:
                # i = 1
                if nums[i] + nums[j] == target:
                    # found a triplet
                    # print('Nums -', nums[k], nums[i], nums[j])

                    # print('nums[i] <= nums[j] <= nums[k]', nums[i] <= nums[j] <= nums[k])
                    # print('nums[j] <= nums[k] <= nums[i]', nums[j] <= nums[k] <= nums[i])
                    # print('nums[k] <= nums[i] <= nums[j]', nums[k] <= nums[i] <= nums[j])
                    # print('nums[i] <= nums[k] <= nums[j]', nums[i] <= nums[k] <= nums[j])
                    # print('nums[k] <= nums[j] <= nums[i]', nums[k] <= nums[j] <= nums[i])
                    # print('nums[j] <= nums[i] <= nums[k]', nums[j] <= nums[i] <= nums[k])

                    res.append([nums[k], nums[i], nums[j]])

                    while nums[i] == nums[i+1] and i+1 < j:
                        i += 1
                    while nums[j] == nums[j-1] and i+1 < j:
                        j -= 1

                    i += 1
                    j -= 1
                    print('=========================')

                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    i += 1
                
                print('=========================')
                
        return res


    def threeSum(self, nums):
        # return self.using_two_sum(nums)
        return self.using_hash(nums)
        

        


sol = Solution()

# nums = [-1,0,1,2,-1,-4] # Output: [[-1,-1,2],[-1,0,1]]

# nums = [0,1,1] # Output: []
# nums = [-2, 0, 0, 2, 2]
# nums = [0,0,0] # [[0,0,0]]
nums = [-1,0,1,0] # [-1,0,1]
print(sol.threeSum(nums))