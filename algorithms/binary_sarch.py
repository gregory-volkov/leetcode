# Classic one
# Just returns the id if persists, otherwise -1
def bsearch(nums, target):
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if target < nums[mid]:
            j = mid - 1
        if target > nums[mid]:
            i = mid + 1
        if target == nums[mid]:
            return mid
    return -1

# Upper bound
# Returns the id of required item or the place where it should be
def bsearch_upper(lst, item):
    i, j = 0, len(lst)
    while i < j:
        mid = (i + j) // 2
        if lst[mid] <= item:
            i = mid + 1
        else:
            j = mid
    return i - 1
