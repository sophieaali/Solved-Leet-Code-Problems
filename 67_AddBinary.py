# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# step 1: convert binary string to numbers
# step 2: sum numbers
# step 3: convert result back to binary

# Notes on binary conversions from: https://www.britannica.com/technology/binary-code and https://www.youtube.com/watch?v=rsxT4FfRBaM


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
         # step 1: convert binary string to numbers
        y_a = len(a)-1
        y_b = len(b)-1
        result_a = 0
        result_b = 0
    
        for x in a:
            result_a += int(x)*(2**y_a)
            y_a -= 1
        for x in b:
            result_b += int(x)*(2**y_b)
            y_b -= 1

    
        # step 2: sum numbers
        result = result_a + result_b
    

        # step 3: convert result back to binary
        x=0
        y=0
        my_list = []

        while x <= result:
            x = 2**y
            my_list.insert(0, x)
            y+=1

        if len(my_list)>1:
            my_list.pop(0)

        binary_result = ''

        for x in my_list:
            if x <= result:
                binary_result += '1'
                result -= x
            else: 
                binary_result += '0'

        return binary_result


# testing
print(Solution().addBinary(a = "11", b = "1")) # results should be '100'
print(Solution().addBinary(a = "1010", b = "1011")) # results should be '10101'
