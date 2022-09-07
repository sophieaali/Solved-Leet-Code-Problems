# Number of Steps to Reduce a Number to Zero

# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, 
# you have to subtract 1 from it.

def numberOfSteps(num):
    ans = 0

    while num > 0:
        while num%2 == 0:
            num/=2
            ans += 1
        num -= 1
        ans += 1
    return ans




# Example 1:
print(numberOfSteps(14))
# Output: 6

# Example 2:
print(numberOfSteps(8))
# Output: 4

# Example 3:
print(numberOfSteps(123))
# Output: 12