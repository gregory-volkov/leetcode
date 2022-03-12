# 1. Two Sum
# https://leetcode.com/problems/two-sum/

    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # elem: int, ls: list of tuples (index, value)
        def bin_search(elem: int, ls):
            if len(ls) == 0:
                return None
            i, j = 0, len(ls) - 1
            while True:
                mid = (i + j) // 2
                if ls[i][1] == elem or ls[j][1] == elem:
                    return ls[i][0] if ls[i][1] == elem else ls[j][0]
                else:
                    if i == mid:
                        return None
                    if ls[mid][1] < elem:
                        i = mid
                    else:
                        j = mid

        nums = sorted(enumerate(nums), key=lambda x: x[1])

        nums_amt = len(nums)
        cur_index = None
        snd_index = None

        for _ in range(nums_amt):
            cur_index, cur = nums.pop()

            snd = target - cur
            snd_index = bin_search(snd, nums)
            if snd_index is not None:
                break

        return [snd_index, cur_index]
