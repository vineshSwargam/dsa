# Longest Substring Without Repeating Characters
# Medium
# Topics
# Company Tags
# Hints
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.


# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.


# Example 2:

# Input: s = "xxxx"

# Output: 1

# Constraints:

# 0 <= s.length <= 50,000
# s may consist of printable ASCII characters.


# Topics

  

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(m) space, where n is the length of the string and m is the number of unique characters in the string.


# Hint 1
# A brute force solution would be to try the substring starting at index i and try to find the maximum length we can form without duplicates by starting at that index. We can use a hash set to detect duplicates in O(1) time. Can you think of a better way?


# Hint 2
# We can use the sliding window algorithm. Since we only care about substrings without duplicate characters, the sliding window can help us maintain valid substring with its dynamic nature.


# Hint 3
# We can iterate through the given string with index r as the right boundary and l as the left boundary of the window. We use a hash set to check if the character is present in the window or not. When we encounter a character at index r that is already present in the window, we shrink the window by incrementing the l pointer until the window no longer contains any duplicates. Also, we remove characters from the hash set that are excluded from the window as the l pointer moves. At each iteration, we update the result with the length of the current window, r - l + 1, if this length is greater than the current result.


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        str_set = set()
        i = 0
        j = 0
        sl = len(s)
        max_len = 0

        while j < sl:
            if s[j] not in str_set:
                str_set.add(s[j])
                j += 1
                max_len = max(j-i, max_len)
                continue
            
            str_set.remove(s[i])
            i += 1
            j = i
        
        return max_len


sol = Solution()

s = "zxyzxyz" # Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# s = "xxxx" # Output: 1
# s = "aab" # Output: 2
# s = "aabc" # Output: 3
# s = "aabcabcd" # Output: 4
s = """N3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S
<
Y{
>
M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S
<
Y{
>
M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S
<
Y{
>
M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S
<
Y{
>
M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S
<
Y{
>
M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S<Y{>M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P|v@qsN3W-a`,:;bcze+7lnTAm!pu#S
<
Y{
>
M9CX(fHO2G$ij_oR%wdxyILZ&'DEk56Ut)V^rhB?g*1K0~4/QF.]J[8}P
"""

print(sol.length_of_longest_substring(s))