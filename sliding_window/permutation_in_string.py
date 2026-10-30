# Permutation in String
# Medium
# Topics
# Company Tags
# Hints
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false
# Constraints:

# 1 <= s1.length, s2.length <= 10000


# Topics

   

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the maximum of the lengths of the two strings.


# Hint 1
# A brute force solution would be to check every substring of s2 with s1 by sorting s1 as well as the substring of s2. This would be an O(n^2) solution. Can you think of a better way? Maybe we can use the freqency of the characters of both the strings as we did in checking anagrams.


# Hint 2
# We return false if the length of s1 is greater than the length of s2. To count the frequency of each character in a string, we can simply use an array of size O(26), since the character set consists of a through z (26 continuous characters). Which algorithm can we use now?


# Hint 3
# We use a sliding window approach on s2 with a fixed window size equal to the length of s1. To track the current window, we maintain a running frequency count of characters in s2. This frequency count represents the characters in the current window. At each step, if the frequency count matches that of s1, we return true.

from collections import defaultdict


class Solution:
    def correct_O_of_N_sol(self, s1, s2):
        sl1 = len(s1)
        sl2 = len(s2)
        cd = [0]*26
        ord_offset = 97
        l = 0
        r = sl1-1

        if sl1 > sl2:
            return False

        for st in s1:
            cd[ord(st)-ord_offset] += 1

        for i in range(r-l+1):
            s2_ind = ord(s2[l+i])-ord_offset
            cd[s2_ind] -= 1

        while r<sl2:
            print(s1, sl1)
            print(s2, sl2)
            print(l, r)
            print(cd)

            if l > 0:
                s2l_ind = ord(s2[l-1])-ord_offset
                cd[s2l_ind] += 1

                s2r_ind = ord(s2[r])-ord_offset
                cd[s2r_ind] -= 1
            
            print(cd)
            if cd == [0]*26:
                return True

            l += 1
            r += 1

            print('===================')

        return False

    def check_inclusion(self, s1: str, s2: str):
        # return self.correct_O_of_N_sol(s1, s2)
        sl1 = len(s1)
        sl2 = len(s2)
        cd = defaultdict(int)
        tcd = defaultdict(int)
        l = 0
        r = 0

        for st in s1:
            cd[st] += 1
            tcd[st] += 1


        while r<sl2:
            print(tcd)
            print(s2)
            print(l, r)
            print(s2[r], s2[r] not in tcd)


            if s2[r] not in tcd:
                print('Moving L to R')
                tcd = cd.copy()
                l += 1
                r = l
                continue
            
            tcd[s2[r]] -= 1
            if tcd[s2[r]] == 0:
                tcd.pop(s2[r])
            
            if r - l + 1 == sl1:
                return True
    
            r += 1
            print('===================')

        return False



sol = Solution()

# s1, s2 = 'abc', 'lecabee'
s1, s2 = 'abc', 'lecaabee'
# s1, s2 = 'adc', 'dcda'
# s1, s2 = '', ''

print(sol.check_inclusion(s1, s2))