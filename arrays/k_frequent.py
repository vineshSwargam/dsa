# https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# git remote add origin git@github-personal.com:/leet.git

from collections import defaultdict

def k_freq(nums, k):
    # naive hash map solution
    # print(nums)
    # nums_dict = defaultdict(int)

    # for num in nums:
    #     nums_dict[num] += 1
    # # 1, 2, 0, 3, 0, 0

    # result = []
    # s_f = sorted(nums_dict.items(), key=lambda pair: pair[1])

    # # 0, 0, 0, 1, 2, 3
    # for n in s_f[-k:]:
    #     result.append(n[0])

    # print(s_f)
    # print(result)

    # bucket sort solution. Init an list of lists of len n, store num inside the list at index of freq n. if 3 appears 4 times, store it in the list, the list is at index=4, append 3 to the list at index 4
    
    count = defaultdict(list)
    freq = [[] for i in range(len(nums) + 1)]

    for ind, num in enumerate(nums):
        count[num].append(ind)
    for num, idxs in count.items():
        freq[len(idxs)].append((num, idxs))

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num[1])
            if len(res) == k:
                print(res)
                return res





k_freq([1, 3, 4, 3, 2, 2, 5, 2], 2)
k_freq([1,2], 2)


