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
from collections import defaultdict


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



# l1 = [ 5, 2, 4, 3, 1]
# l1 = [2, 5, 4, 1, 3]
# print(l1)
# merge_sort(l1)

class Solution:
    def using_merge_sort(self, nums):
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
        return max_count

    def longest_consecutive(self, nums) -> int:
        # return self.using_merge_sort(nums)
        
        # [0,3,2,5,4,6,1,1]
        # check if n-1 exists
        # if not, then this is seq starter
        # add it to a hash set { [n]: {n}}
        # { 0: {0}}
        # { 0: {0}, 3: {3} }
        # { 0: {0}, 3: {3} }
        # { 0: {0}, 2: ({2, 3}, None), 3: ({3}, 2) }
        # { 0: 1, 2: {2, 3}, 3: ({3}, 2), 5: {5} }
        # while obj[n-1][1] != None: obj[obj[n-1][1]] = obj[obj[n-1][1]][0].add(n)
        # 
        # { 0: 1, 2: {2, 3, 4}, 3: {2, 3, 4}, 4: {2, 3, 4} 5: {5} }
        # { 0: 1, 2: {2, 3, 4}, 3: {2, 3, 4}, 4: {2, 3, 4} 5: {5} }
        ####################################
        #                              starter is 1, max is 2
        seq = defaultdict(lambda: [set(), int, int])
        # s = { 1 }
        # print(s.add(2))
        # return

        for n in nums:
            # print('N = ', n)
            if n in seq:
                continue

            if n-1 not in seq and n+1 not in seq:
                seq[n] = [{n}, None, n]
                print('Seq - ', seq)
                continue

            if n-1 in seq and n+1 in seq:
                lb_key = seq[n-1][1] if seq[n-1][1] != None else n-1
                ub_key = seq[n+1][1] if seq[n+1][1] != None else n+1
                # print("BOTH in sequence. lbkey -", lb_key, "ub_key -", ub_key)

                #  UNION OF BOTH SETS
                seq[lb_key][0] = seq[lb_key][0] | {n} | seq[ub_key][0]

                # Point UB Starter to LB as it is new starter of union sequence
                ub_seq_end = seq[ub_key][2]
                seq[ub_seq_end][1] = lb_key
                # take the max of ub
                seq[lb_key][2] = ub_seq_end
                print('LB key -', lb_key, 'UB key -', ub_key)
                print('Seq LB and UB - ', seq[lb_key], seq[ub_key])

                continue
            
            if n-1 in seq:
                starter_key = seq[n-1][1] if seq[n-1][1] != None else n-1
                seq[n] = [{n}, starter_key, n]

                seq[starter_key][0].add(n)
                seq_max = seq[starter_key][2]
                if n > seq_max:
                    seq[starter_key][2] = n
                print('In n-1 -', n-1, n, starter_key)
                if starter_key == n-1:
                    print('N-1 is the starter')
                    print('Seq n and n-1 - ', seq[n], seq[n-1])
                else:
                    print('N-1 has a starter - ', starter_key)
                    print('Seq n, n-1, and starter - ', seq[n], seq[n-1], seq[starter_key])
                    
            if n+1 in seq:
                # if seq[n+1][1] != None:
                    # print('Houston we have a problem! - ', n)
                new_set = seq[n+1][0]
                new_set.add(n)
                seq[n] = [new_set, None, seq[n+1][2]]
                seq[n+1][1] = n

                ub_seq_end = seq[n+1][2]
                seq[ub_seq_end][1] = n
                # take the max of ub
                seq[n][2] = ub_seq_end
                print('In n+1 loop -', n, n+1)
                print('So n will become the starter for n+1')
                print('Seq n and n+1 - ', seq[n], seq[n+1])

            # print('Seq - ', seq)

        max_seq_len = 0
        for s in seq.values():
            seq_len = len(s[0])
            if seq_len > max_seq_len:
                max_seq_len = seq_len

            
        return max_seq_len


        

sol = Solution()
# l1 = [0,3,2,5,4,6,1,1] # 7
l2 = [2,20,4,10,3,4,5] # - 4
# l1 = [0,3,7,2,5,8,4,6,0,1] # - 8

# l2 = [2, 3, 1, 5, 4, 0]
# l2 = [2, 3, 5, 1, 4, 0]
# l2 = [2, 5, 3, 1, 4, 0]
# l2 = [3, 2, 1, 5, 4, 0]
# l2 = [3, 2, 5, 1, 4, 0]
# l2 = [3, 5, 2, 1, 4, 0]
# l2 = [5, 2, 3, 1, 4, 0]
# l2 = [5, 3, 2, 1, 4, 0]
print(l2)
print(sol.longest_consecutive(l2))