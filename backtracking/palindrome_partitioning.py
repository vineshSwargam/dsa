# Palindrome Partitioning
# Medium
# Topics
# Company Tags
# Hints

# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

# You may return the solution in any order.

# Example 1:

# Input: s = "aab"

# Output: [["a","a","b"],["aa","b"]]

# Example 2:

# Input: s = "a"

# Output: [["a"]]

# Constraints:

# 1 <= s.length <= 20
# s contains only lowercase English letters.



# Topics

# String Dynamic Programming Backtracking


# Recommended Time & Space Complexity

# You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the length of the input string.



# Hint 1

# For a given string there are 2^n possible partitions because at each index we have two decisions: we can either partition and start a new string, or continue without partitioning. Can you think of an algorithm to recursively traverse all combinations?



# Hint 2

# We can use backtracking to recursively traverse the string with indices j (start of the current substring) and i (current iterating index). At each step, we either skip partitioning at the current index or, if the substring from j to i is a palindrome, make a partition, update j = i + 1, and start a new substring. The base condition to stop the recursion is when j reaches the end of the string. How do you implement this?



# Hint 3

# We start with j = 0, i = 0 and a temporary list which stores the substrings from the partitions. Then we recursively iterate the string with the index i. At each step we apply the 2 decisions accordingly. At the base condition of the recursive path, we make a copy of the current partition list and add it to the result.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 77.0%


from typing import List
import traceback


# for n len string, n-1 splits are possible
class Solution:
    def using_recur_bt(self, s: str) -> List[List[str]]:
        res = []
        sl = len(s)
        
        # Picture walking along the string with scissors
        # part: the pieces you've already cut off and saved.
        # j: where the piece in your hand starts.
        # i: where you're currently standing.
        # The piece in your hand is s[j..i]. It isn't in part yet
        # The piece in your hand is everything from j to i.
        # At each letter, you decide: cut here (only if the piece in your hand is a palindrome), or keep walking, so the piece gets one letter longer
        
        def bt(sub, j, i): 
            if i >= sl:
                if j == i:
                    res.append(sub.copy())
                return

            piece = s[j:i+1]
            # check if pali
            if piece == piece[::-1]:
                # take the split
                sub.append(piece)
                bt(sub, i+1, i+1)
                # skip the split
                sub.pop()
            
            bt(sub, j, i+1)
            
        bt([], 0, 0)
        return res



    def partition(self, s: str) -> List[List[str]]:
        return self.using_recur_bt(s)


sol = Solution()

# run from the repo root: python3 -m backtracking.palindrome_partitioning
# (s, expected) - the partitions can come in any order, but the pieces inside each partition must stay in string order
# expected is either the full answer, or (for the big cases) just how many partitions there should be.
# For a count, every partition you return is also checked: its pieces must join back into s, every piece must be
# a non-empty palindrome, and no partition may appear twice.
tests = [
    ("aab", [["a","a","b"],["aa","b"]]),                             # example 1
    ("a", [["a"]]),                                                  # example 2
    ("ab", [["a","b"]]),                                             # no palindrome longer than one letter
    ("aa", [["a","a"],["aa"]]),                                      # the whole string is a palindrome too
    ("aaa", [["a","a","a"],["a","aa"],["aa","a"],["aaa"]]),          # "a","aa" and "aa","a" are different partitions
    ("aba", [["a","b","a"],["aba"]]),                                # odd length palindrome, "ab" and "ba" are not
    ("abba", [["a","b","b","a"],["a","bb","a"],["abba"]]),           # even length palindrome, and one inside it
    ("abc", [["a","b","c"]]),                                        # only single letters work
    ("racecar", [["r","a","c","e","c","a","r"],["r","a","cec","a","r"],["r","aceca","r"],["racecar"]]),   # palindromes nested inside each other
    ("noonabbad", 9),                                                # palindromes next to each other and overlapping
    ("abcdefghijklmnopqrst", 1),                                     # max length, all different: one partition
    ("ababababababababab", 2584),                                    # 18 letters, odd palindromes everywhere
    ("aabbaabbaabbaabbaabb", 5185),                                  # max length, mixed
    ("a" * 20, 524288),                                              # max length, worst case: every split works, 2^19 partitions
]

def is_pal(t):
    return t == t[::-1]

def check(s, got, expected):
    if not isinstance(got, list):
        return False, ""
    if isinstance(expected, list):
        return sorted(map(list, got)) == sorted(expected), ""
    for p in got:
        if "".join(p) != s:
            return False, f"  {list(p)} does not join back into {s!r}"
        for piece in p:
            if not piece or not is_pal(piece):
                return False, f"  {piece!r} in {list(p)} is not a palindrome"
    if len(set(map(tuple, got))) != len(got):
        return False, "  the same partition appears more than once"
    return len(got) == expected, ""

passed = 0
for s, expected in tests:
    try:
        got = sol.partition(s)
        ok, why = check(s, got, expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} partitions" if isinstance(got, list) and len(got) > 4 else got
    print(f"{'PASS' if ok else 'FAIL'}  {s!r} -> {shown}" + ("" if ok else f"  expected {expected}{why}"))

print(f"{passed}/{len(tests)} passed")
