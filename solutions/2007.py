# 2007. Find Original Array From Doubled Array
# https://leetcode.com/problems/find-original-array-from-doubled-array/


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = {}
        for num in changed:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
        ans = []
        for num in sorted(cnt.keys()):
            # print(num, cnt)
            if cnt[num] == 0:
                continue
            if num == 0:
                if cnt[num] % 2:
                    return []
                else:
                    ans.extend(num for _ in range(cnt[num] // 2))
                    continue
            doubled = num * 2
            if doubled not in cnt or cnt[num] > cnt[doubled]:
                return []
            cnt[doubled] -= cnt[num]
            ans.extend(num for _ in range(cnt[num]))
        return ans
