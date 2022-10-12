# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        while (re.search('\{\}', s) or re.search('\(\)', s) or re.search('\[\]', s)):
            s = re.sub('\{\}', '', s)
            s = re.sub('\[\]', '', s)
            s = re.sub('\(\)', '', s)

        return s == ''

print(Solution().isValid("()"))             # True
print(Solution().isValid("()[]{}"))         # True
print(Solution().isValid("([)]"))           # False
print(Solution().isValid("(]"))             # False
print(Solution().isValid("({{{{}}}))"))     # False

