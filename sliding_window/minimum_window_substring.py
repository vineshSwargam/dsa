# Minimum Window Substring
# Hard
# Topics
# Company Tags
# Hints
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 100,000
# 1 <= t.length <= 100,000
# s and t consist of uppercase and lowercase English letters.


# Topics

# Recommended Time & Space Complexity
# You should aim for a solution with O(n + m) time and O(k) space, where n is the length of the string s, m is the length of the string t, and k is the total number of unique characters in s and t.


# Hint 1
# A brute force solution would involve checking every substring of s against t and returning the minimum length valid substring. This would be an O(n^2) solution. Can you think of a better way? Maybe you should think in terms of frequency of characters.


# Hint 2
# We need to find substrings in s that should have atleast the characters of t. We can use hash maps to maintain the frequencies of characters. It will be O(1) for lookups. Can you think of an algorithm now?


# Hint 3
# We can use a dynamically sized sliding window approach on s. We iterate through s while maintaining a window. If the current window contains at least the frequency of characters from t, we update the result and shrink the window until it is valid.


# Hint 4
# We should ensure that we maintain the result substring and only update it if we find a shorter valid substring. Additionally, we need to keep track of the result substring's length so that we can return an empty string if no valid substring is found.



class Solution:
    def get_ord(self, c):
            if ord(c)>= 65 and ord(c)<= 90:
                return ord(c)-65
            if ord(c)>= 97 and ord(c)<= 122:
                return ord(c)-71

    def get_fr_list(self, st: str, arr):
        for string in st:
            arr[self.get_ord(string)] += 1
        return arr

    def brute_force(self, s, t):
        slen = len(s)
        tlen = len(t)
        valid_sub = ''
        valid_sub_len = float('inf')
            
        tf = self.get_fr_list(t, [0]*52)
        print(tf)


        for i in range(slen):
            cf = [0] * 52
        
            for j in range(i, slen):
                print(s, slen)
                print(t, tlen)
                print('Range - ', i, j)
                if j-i >= valid_sub_len:
                    print('======== B R E A K I N G ===============')
                    break

                sji = self.get_ord(s[j])
                print('sji val -', s[j])
                if tf[sji] > 0 and cf[sji] < tf[sji]:
                    cf[sji] += 1

                print(cf)
                if tf == cf:
                    valid_sub = s[i:j+1]
                    valid_sub_len = len(valid_sub)

                print('valid_sub -', valid_sub)
                print('=======================')
            
        return valid_sub
                
    # def is_valid(s, tf, cf):
    #     is_valid = False
    #     for st in s:
    #         sti = get_ord(st)
    #         if tf[sti] < 0 or cf[sti] < tf[sti]:





    def two_pointer(self, s, t):
        slen = len(s)
        tlen = len(t)
        l = 0
        r = 0
        tf = self.get_fr_list(t, [0]*52)
        sf = [0]*52
        valid_sub = ''
        valid_sub_len = float('inf')
        valid_sub_lr = None
        moving_l = False

        def is_valid(af, bf):
            for i, a in enumerate(af):
                if a > bf[i]:
                    return False

            return True



        while r < slen:
            print('Indexes - ', l, r)
            print('Inputs')
            print(s, slen)
            print(t, tlen)
            print('Active Substring -', s[l:r+1])

            if not moving_l:
                sfr = self.get_ord(s[r])
                print('char at r -', s[r])
                print('count of char in t -', tf[sfr])
                sf[sfr] += 1 if tf[sfr] > 0 else 0
                print('tf - ', tf)
                print('sf - ', sf)


            if is_valid(tf, sf):
                print('=======  I S  V A L I D  =====')
                if r-l < valid_sub_len:
                    valid_sub_lr = (l, r)
                    valid_sub_len = r-l
                slo = self.get_ord(s[l])
                if tf[slo] > 0:
                    sf[slo] -= 1
                l += 1
                moving_l = True
            else:
                moving_l = False
                r += 1
                
            print("========================")
        return s[valid_sub_lr[0]:valid_sub_lr[1]+1] if isinstance(valid_sub_lr, tuple) else ''



    def minimum_window(self, s, t):
        # return self.brute_force(s, t)
        return self.two_pointer(s, t)






sol = Solution()

# s, t = 'OUZODYXAZV', 'XYZ'
# s, t = 'xyz', 'xyz'
# s, t = 'x', 'xy'
# s, t = 'ADOBECODEBANC', 'ABC'  # 'BANC' - answer is at the end, after earlier valid windows
s, t = 'a', 'aa'               # ''     - duplicate in t that s can't satisfy
# s, t = 'axxa', 'aa'            # 'axxa' - extra chars can't be avoided
# s, t = 'bbaac', 'abc'          # 'baac' - shrink past an extra 'b' on the left
# s, t = 'aA', 'A'               # 'A'    - case-sensitive, 'a' doesn't count


print(sol.minimum_window(s, t))