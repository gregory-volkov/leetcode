# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums: List[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[j - 1]:
            nums[j] = nums[i]
            j += 1
    return j
