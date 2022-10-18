# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

 
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        listSubstrings = []
        for i in range(len(s)):
            r = '' 
            for x in range(i, len(s)):
                if s[x] not in r:
                    r+= s[x]
                else:
                    break
            
            listSubstrings.append(r)
            
        if len(listSubstrings)>0:
            return len(max(listSubstrings, key=len))
        else:
            return 0


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
s = ''
print(Solution().lengthOfLongestSubstring(s))
