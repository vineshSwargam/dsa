# Longest Repeating Character Replacement
# Medium
# Topics
# Company Tags
# Hints
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5
# Constraints:

# 1 <= s.length <= 100,000
# 0 <= k <= s.length
# s consists of only uppercase english characters.


# Topics

  

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(m) space, where n is the length of the given string and m is the number of unique characters in the string.


# Hint 1
# Which characters would you replace in a string to make all its characters identical? Can you think with respect to the frequency of the characters?


# Hint 2
# For a given substring or window, it is always optimal to replace characters with the most frequent character in that substring. Why? Because using the most frequent character minimizes the number of replacements required to make all characters in the substring identical. How can you find the number of replacements now?


# Hint 3
# The number of replacements is equal to the difference between the length of the current substring and the frequency of the most frequent character in that substring. A brute force solution would be to consider all substrings, use a hash map for frequency counting, and return the maximum length of the substring that has at most k replacements. This would be an O(n^2) solution. Can you think of a better way?


# Hint 4
# We can use the sliding window approach. The window size will be dynamic, and we will shrink the window when the number of replacements exceeds k. The result will be the maximum window size observed at each iteration.
from collections import deque
from collections import defaultdict


class Solution:
    def failed_method(self, s:str, k: int):
        cur_char = s[l]
        max_len = 1 # because s constraint is <= 1 < 100000
        substr_head_q = deque([])
        count = defaultdict(int)
        ab_count = 0 # aberration count
        prev_ab_char = None

        while r < slen:
            print('s, k -', s, k)
            print('l - r', l, r)

            if s[r] != cur_char:
                ab_count += 1
                print('ab_count -', ab_count)
            
            if ab_count > 0:
                count[s[r]] += 1
                if prev_ab_char is None or s[r] != prev_ab_char:
                    print('Appending to Queue.. -', r)
                    prev_ab_char = s[r]
                    substr_head_q.append(r)
    
            if ab_count <= k:
                print('Length -', r-l)
                max_len = max(r-l+1, max_len)
                print('max -', max_len)
                r += 1
                print('=====================')
                continue




            # A A A B A A C | k = 1  { B: 1, A: 2, C: 1 } ab_count = 2 subhead = ([3, 4, 6])
            while ab_count > k and len(substr_head_q) > 0:
                l = substr_head_q.popleft() # 3 | 4
                print('next_head -', l)

                # count[s[3]] - count[B] - 1 | count[s[4]] - count[A] - 2
                char_count_in_sub = count[s[l]] 
                print('char_count_in_sub -', char_count_in_sub)

                sublen = r - l + 1 # 6 - 3 + 1 = 4 | 6-4+1 = 3
                print('sublen -', sublen)

                ab_count = sublen - char_count_in_sub # 4-1= 3 will go round 2 | 3-2= 1
                print('sub abcount -', ab_count)

                print("ab_count <= k and r == slen and l >= 0", ab_count < k and r == slen-1 and l > 0)
                print('l, r', l, r)

            while ab_count < k and r == slen-1 and l > 0:
                l -= 1
                sublen = r - l + 1 # 6 - 3 + 1 = 4 | 6-4+1 = 3
                ab_count = sublen - char_count_in_sub # 4-1= 3 will go round 2 | 3-2= 1
                print('next_head -', l)
                print('sub abcount -', ab_count)
                print('sublen -', sublen)
        

            max_len = max(sublen, max_len)
            cur_char = s[l] # B | A
            print('cur char -', cur_char)
            print('max len -', max_len)
            r += 1
            print('=====================')

        return max_len
    
    def character_replacement(self, s: str, k: int):
        slen = len(s)
        l = 0
        r = 1
        alpha_freq = [0] * 26
        ord_offset = 65
        max_len = 1
        
        def get_ord(c):
            return ord(c) - ord_offset
        alpha_freq[get_ord(s[0])] += 1 

        def get_char_freq(arr):
            max_freq = 0
            char_ind = None
            for i in range(26):
                if arr[i] > max_freq:
                    max_freq = arr[i]
                    char_ind = i
            
            return arr[char_ind]

        while r<slen:
            print(s)
            alpha_freq[get_ord(s[r])] += 1
            char_freq = get_char_freq(alpha_freq)
            sublen = r-l+1
            ab_count = sublen - char_freq
            print(l, r)
            print(sublen, char_freq)
            print(ab_count)
            if ab_count <= k:
                max_len = max(sublen, max_len)
            else:
                alpha_freq[get_ord(s[l])] -= 1
                l += 1

            r += 1
            print('=====================')

        
        return max_len


            
            



sol = Solution()

# s = "XYYX", k = 2 # Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# s, k = "AAABABBBBBC", 1 # 7
# s, k = "AAABAC", 1 # 5
# s, k = "AAABABBBB", 1 # 6
# s, k = "ABAB", 2 # 4
# s, k = "ABBB", 2 # 4
# s, k = "AABABBA", 1 # 4
# s, k = "ABAA", 0 # 2
# s, k = "ABCDE", 1 # 2 
# s, k = "BAAAB", 2 # 5
s, k = "A", 0 # 5

print(sol.character_replacement(s, k))