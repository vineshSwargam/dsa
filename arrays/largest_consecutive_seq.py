# Longest Consecutive Sequence
# Medium
# Topics
# Company Tags
# Hints
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 100,000
# -10^9 <= nums[i] <= 10^9

# Topics

  

# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.


# Hint 1
# A brute force solution would be to consider every element from the array as the start of the sequence and count the length of the sequence formed with that starting element. This would be an O(n^2) solution. Can you think of a better way?


# Hint 2
# Is there any way to identify the start of a sequence? For example, in [1, 2, 3, 10, 11, 12], only 1 and 10 are the beginning of a sequence. Instead of trying to form a sequence for every number, we should only consider numbers like 1 and 10.


# Hint 3
# We can consider a number num as the start of a sequence if and only if num - 1 does not exist in the given array. We iterate through the array and only start building the sequence if it is the start of a sequence. This avoids repeated work. We can use a hash set for O(1) lookups by converting the array to a hash set.

from math import floor


def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    mid = floor(n/2)
    ll = nums[0:mid]
    rl = nums[mid:n]
    ml = []

    print('ll - ', ll)
    print('rl - ', rl)
    print("ENTERING RECURSION")

    ll = merge_sort(ll)
    print('After Rec - rl - ', rl)
    rl = merge_sort(rl)
    # print('AFter Rec - ll - ', ll)
    # print('After Rec - ml - ', ml)
    
    lll = mid
    rll = n - mid
    lli = 0
    rli = 0
    print(f'length lll - {lll}, rll = {rll}')

    while lli < lll and rli < rll:
        left = ll[lli]
        right = rl[rli]
        # print(f'{left} <= {right}')
        if left <= right:
            # print(f'left is lesser')
            ml.append(left)
            lli += 1
        else:
            # print(f'right is lesser')
            ml.append(right)
            rli += 1
    
    while lli < lll:
        ml.append(ll[lli])
        lli += 1

    while rli < rll:
        ml.append(rl[rli])
        rli += 1

    print('ml - ', ml)
    print("EXITING RECURSION")
    print("======================")
    return ml



l1 = [ 5, 2, 4, 3, 1]
# l1 = [2, 5, 4, 1, 3]
print(l1)
# merge_sort(l1)

class Solution:
    def longest_consecutive(self, nums) -> int:
        s_nums = merge_sort(nums)
        nl = len(s_nums)
        if nl < 1:
            return 0
        count = 1
        max_count = 1
        print('length - ', nl)
        for i, num in enumerate(s_nums):
            if i+1 > nl-1:
                break
            print(f'index-{i} - {s_nums[i+1]} minus {num}')
            print(f'subtraction - {s_nums[i+1] - num}')
            next_diff = s_nums[i+1] - num
            if next_diff == 1:
                count +=1
                max_count = count if count > max_count else max_count
            elif next_diff == 0:
                continue
            else:
                count = 1
            print('Count -', count)

        print(max_count)

        

sol = Solution()
# l3 = [0,3,2,5,4,6,1,1]
# l4 = [2,20,4,10,3,4,5]
l5 = [0,3,2,5,4,6,1,1]
print(sol.longest_consecutive(l5))