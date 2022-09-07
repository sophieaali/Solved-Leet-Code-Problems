# Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# solution idea 1:
def runningSum(nums):
    newList = []
    for x in range(len(nums)):
        newList.append(sum(nums[0:x+1]))
    return newList

print(runningSum([1,2,3,4]))
# Output: [1,3,6,10]

print(runningSum([1,1,1,1,1]))
# Output: [1,2,3,4,5]

# solution idea 2:
def runningSum(nums):
    newList = []
    result = 0
    for x in nums:
        result += x
        newList.append(result)
    return newList

print(runningSum([1,2,3,4]))
# Output: [1,3,6,10]

print(runningSum([1,1,1,1,1]))
# Output: [1,2,3,4,5]