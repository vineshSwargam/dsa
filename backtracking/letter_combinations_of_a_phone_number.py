# Letter Combinations of a Phone Number
# Medium
# Topics
# Company Tags
# Hints

# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.

# Example 1:

# Input: digits = "34"

# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

# Example 2:

# Input: digits = ""

# Output: []

# Constraints:

# 0 <= digits.length <= 4
# 2 <= digits[i] <= 9



# Topics

# Hash Table String Backtracking


# Recommended Time & Space Complexity

# You should aim for a solution with O(n * (4^n)) time and O(n) space, where n is the length of the input string.



# Hint 1

# We can use a hash map to pair all the digits with their corresponding letters. Think of this as a decision tree, where at each step, we have a digit, and we select one of multiple characters to proceed to the next digit in the given string digits. Can you think of an algorithm to generate all combinations of strings?



# Hint 2

# We can use backtracking where we select a character and process it, then backtrack to process another character. We recursively iterate on the given string with index i. At each step, we consider the letters from the hash map that correspond to the digit at the i-th index. Can you think of the base condition to stop this recursive path?



# Hint 3

# We initialize an empty string that represents the choices of the characters throughout the current recursive path. When the index i reaches the end of the string, we add the current string to the result list and return.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 77.7%


from typing import List
import traceback


class Solution:
    def using_recur_bt(self, digits: str) -> List[str]:
        res = []
        dm = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def bt(s, ind):
            if not digits:
                return res
            
            slot = len(s)

            if slot == len(str(digits)):
                res.append(s)
                return

            cur_chars = dm[int(digits[slot])]
            if ind >= len(cur_chars):
                return

            ch = cur_chars[ind]  # ch is the letter to append
            bt(s+ch, 0)
            bt(s, ind+1)  # no pop needed, s was never touched
        
        bt('', 0)
        return res
        
    def letter_combinations(self, digits: str) -> List[str]:
        return self.using_recur_bt(digits)


sol = Solution()

# run from the repo root: python3 -m backtracking.letter_combinations_of_a_phone_number
# The keypad (the picture missing from the problem text):
#   2: abc   3: def   4: ghi   5: jkl   6: mno   7: pqrs   8: tuv   9: wxyz
# (digits, expected) - the strings can come in any order
# expected is either the full answer, or (for the big cases) just how many strings there should be.
# For a count, every string you return is also checked: one letter per digit, each letter from that digit's key,
# and no string appears twice.
KEYS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

tests = [
    ("34", ["dg","dh","di","eg","eh","ei","fg","fh","fi"]),     # example 1
    ("", []),                                                   # example 2: no digits means no combinations, not [""]
    ("2", ["a","b","c"]),                                       # one digit
    ("7", ["p","q","r","s"]),                                   # one of the two keys with 4 letters
    ("9", ["w","x","y","z"]),                                   # the other one
    ("22", ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]),     # the same digit twice: a letter can repeat
    ("79", 16),                                                 # 4 x 4
    ("234", 27),                                                # 3 x 3 x 3
    ("2793", 144),                                              # max length, mixed 3 and 4 letter keys
    ("5555", 81),                                               # max length, one digit repeated
    ("7979", 256),                                              # max length, worst case: 4^4
]

def problem(word, digits):
    """Returns why word is not a valid answer for digits, or None if it is."""
    if not isinstance(word, str) or len(word) != len(digits):
        return f"{word!r} should be a string of length {len(digits)}"
    for ch, d in zip(word, digits):
        if ch not in KEYS[d]:
            return f"{word!r}: {ch!r} is not on key {d} ({KEYS[d]})"
    return None

def check(digits, got, expected):
    if not isinstance(got, list):
        return False, ""
    if isinstance(expected, list):
        return sorted(got) == sorted(expected), ""
    for word in got:
        why = problem(word, digits)
        if why:
            return False, "  " + why
    if len(set(got)) != len(got):
        return False, "  the same string appears more than once"
    return len(got) == expected, ""

passed = 0
for digits, expected in tests:
    try:
        got = sol.letter_combinations(digits)
        ok, why = check(digits, got, expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} strings" if isinstance(got, list) and len(got) > 9 else got
    print(f"{'PASS' if ok else 'FAIL'}  {digits!r} -> {shown}" + ("" if ok else f"  expected {expected}{why}"))

print(f"{passed}/{len(tests)} passed")
