# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
 
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x >= 0 and x < 10:  # anything from 0-9 is a palindrome
            return True

        elif x < 0 or x%10==0:   # all negative numbers and multiples of 10 are NOT palindromes 
            return False
        else:
            second_half = 0
            while x > second_half:
                second_half = second_half*10 + x%10   # split the number in half and add the numbers to second_half
                x = x//10
            if x == second_half:  # if the reversed second half of the number equals the first half of the number
                return True
            elif x == second_half//10: # check for odd number of digits
                return True
            else:
                return False