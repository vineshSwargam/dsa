# Valid Palindrome
# Easy
# Topics
# Company Tags
# Hints
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.


# Topics

 

# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.


# Hint 1
# A brute force solution would be to create a copy of the string, reverse it, and then check for equality. This would be an O(n) solution with extra space. Can you think of a way to do this without O(n) space?


# Hint 2
# Can you find the logic by observing the definition of pallindrome or from the brute force solution?


# Hint 3
# A palindrome string is a string that is read the same from the start as well as from the end. This means the character at the start should match the character at the end at the same index. We can use the two pointer algorithm to do this efficiently.

class Solution:
    def using_rev_str(self, s: str) -> bool:
        s_len = len(s)
        if s_len == 1:
            return True
        clean_s = ''
        rev_s = ''
        alpha_num_range = set(range(ord('A'), ord('Z')+1)) | set(range(ord('a'), ord('z'))) | set(range(ord('0'), ord('9')))
        print(alpha_num_range)
        print(s, s_len)

        for i in range(s_len-1, -1, -1):
            rev_i = s_len-i-1
            if ord(s[rev_i]) in alpha_num_range:
                clean_s+= s[rev_i] if i >= 0 else ''
            
            if ord(s[i]) not in alpha_num_range:
                print('Ignoring - ', s[i])
                continue
            rev_s += s[i]

        print(rev_s, clean_s)
        if rev_s == clean_s:
            return True
        return False


    def is_palindrome(self, s: str) -> bool:
        # return self.using_rev_str(s)
        i = 0
        j = len(s) - 1
        if j==0:
            return True
        alpha_range = set(range(ord('A'), ord('Z')+1)) | set(range(ord('a'), ord('z')))
        num_range = set(range(ord('0'), ord('9')))
        alpha_num_range = alpha_range | num_range
        case_offset = 97-65
        is_pali = True
        print(set(range(ord('A'), ord('Z')+1)))
        print(set(range(ord('a'), ord('z')+1)))
        print(set(range(ord('0'), ord('9')+1)))
        # 'Was it a car or a cat I saw?'
        while i<j:
            # print(i, j)
            if ord(s[i]) not in alpha_num_range:
                i += 1
                continue
            if ord(s[j]) not in alpha_num_range:
                j -= 1
                continue
            print('abs(ord(s[i]) - ord(s[j])) == 32', abs(ord(s[i]) - ord(s[j])) == 32, ord(s[i]) - ord(s[j]))
            print('s[i] s[j]', s[i], s[j])

            leftIsNum = ord(s[i]) in num_range
            rightIsNum = ord(s[j]) in num_range
            areBothNums = leftIsNum and rightIsNum

            if areBothNums and ord(s[i]) != ord(s[j]):
                    is_pali = False
                    break

            leftIsAlpha = ord(s[i]) in alpha_range
            rightIsAlpha = ord(s[j]) in alpha_range
            areBothAlpha = leftIsAlpha and rightIsAlpha

            if areBothAlpha and abs(ord(s[i]) - ord(s[j])) != 32 and abs(ord(s[i]) - ord(s[j])) != 0:
                is_pali = False
                break

            if (leftIsAlpha and rightIsNum) or (rightIsAlpha and leftIsNum):
                is_pali = False
                break

            i += 1
            j -= 1

        print(is_pali)
        return is_pali

        

        

# s = 'Was it a car or a cat I saw?'
# s = "tab a cat"
s = '0P'

sol = Solution()
sol.is_palindrome(s)