# 15. 3Sum
# https://leetcode.com/problems/3sum/

def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    nums_set = defaultdict(int)
    for num in nums:
        nums_set[num] += 1

    ans = set()
    cur_min, cur_max = None, None

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a, b = nums[i], nums[j]
            nums_set[a] -= 1
            nums_set[b] -= 1

            c = 0 - a - b
            if c < a or c < b:
                nums_set[a] += 1
                nums_set[b] += 1
                continue
            if nums_set[c] > 0:
                ans.add((a, b, c))
            nums_set[a] += 1
            nums_set[b] += 1

    return list(map(list, ans))
