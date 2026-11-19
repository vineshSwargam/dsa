# Generate Parentheses
# Medium
# Topics
# Company Tags
# Hints

# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example 1:

# Input: n = 1

# Output: ["()"]

# Example 2:

# Input: n = 3

# Output: ["((()))","(()())","(())()","()(())","()()()"]

# You may return the answer in any order.

# Constraints:

# 1 <= n <= 7



# Topics

# String Dynamic Programming Backtracking


# Recommended Time & Space Complexity

# You should aim for a solution as good or better than O(4^n / sqrt(n)) time and O(n) space, where n is the number of parenthesis pairs in the string.



# Hint 1

# A brute force solution would be to generate all possible strings of size 2n and add only the valid strings. This would be an O(n * 2 ^ (2n)) solution. Can you think of a better way? Maybe you can use pruning to avoid generating invalid strings.



# Hint 2

# We can use backtracking with pruning. But what makes a string invalid? Can you think of a condition for this?



# Hint 3

# When the count of closing brackets exceeds the count of opening brackets, the string becomes invalid. Therefore, we can maintain two variables, open and close, to track the number of opening and closing brackets. We avoid exploring paths where close > open. Once the string length reaches 2n, we add it to the result.



# Company Tags

# Please upgrade to NeetCode Pro to view company tags.

# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 82.0%


from typing import List
import traceback


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        pass


sol = Solution()

# run from the repo root: python3 -m backtracking.generate_parentheses
# (n, expected) - the strings can come in any order
# expected is either the full answer, or (for bigger n) just how many strings there should be.
# For a count, every string you return is also checked: length 2n, only ( and ), never more ) than ( so far,
# equal counts at the end, and no string appears twice.
tests = [
    (1, ["()"]),                                            # example 1
    (2, ["(())","()()"]),                                   # smallest case with a choice
    (3, ["((()))","(()())","(())()","()(())","()()()"]),    # example 2
    (4, 14),
    (5, 42),
    (6, 132),
    (7, 429),                                               # max n
]

def problem(s, n):
    """Returns why s is not a valid answer for n, or None if it is."""
    if not isinstance(s, str) or len(s) != 2 * n:
        return f"{s!r} should be a string of length {2 * n}"
    bal = 0
    for ch in s:
        if ch not in "()":
            return f"{s!r} has a character that is not ( or )"
        bal += 1 if ch == "(" else -1
        if bal < 0:
            return f"{s!r} closes a bracket that was never opened"
    return None if bal == 0 else f"{s!r} leaves {bal} bracket(s) open"

def check(n, got, expected):
    if not isinstance(got, list):
        return False, ""
    if isinstance(expected, list):
        return sorted(got) == sorted(expected), ""
    for s in got:
        why = problem(s, n)
        if why:
            return False, "  " + why
    if len(set(got)) != len(got):
        return False, "  the same string appears more than once"
    return len(got) == expected, ""

passed = 0
for n, expected in tests:
    try:
        got = sol.generate_parenthesis(n)
        ok, why = check(n, got, expected)
    except Exception as e:
        where = traceback.extract_tb(e.__traceback__)[-1]     # the line that actually raised
        got, ok, why = f'ERROR {type(e).__name__}: {e}  (line {where.lineno}: {where.line})', False, ""
    passed += ok
    shown = f"{len(got)} strings" if isinstance(got, list) and len(got) > 5 else got
    print(f"{'PASS' if ok else 'FAIL'}  n={n} -> {shown}" + ("" if ok else f"  expected {expected}{why}"))

print(f"{passed}/{len(tests)} passed")
