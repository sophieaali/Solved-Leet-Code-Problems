# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    r = False
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            r = True
            break
    return r

nums = [1,2,3,1]
print(containsDuplicate(nums))

nums = [1,2,3,4]
print(containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
