# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):

    prefix = ''

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))