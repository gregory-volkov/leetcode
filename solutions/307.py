# 307. Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/description/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = self.build_tree(nums)

    def build_tree(self, a):
        # insert leaf nodes in tree
        n = len(a)
        tree = [0 for _ in range(2 * n + 1)]
        for i in range(n):
            tree[n + i] = a[i]

        # creating parent node by adding left and right child
        for i in range(n - 1, 0, -1):
            tree[i] = tree[2*i] + tree[2*i+1]

        return tree

    def update(self, index: int, val: int) -> None:
        # set value at position index
        n = len(self.nums)
        self.tree[index + n] = val
        index += n

        # after updating the child node,update parents
        i = index

        while i > 1:
            #update parent by adding new left and right child
            if i % 2:
                self.tree[i//2] = self.tree[i] + self.tree[i-1]
            else:
                self.tree[i // 2] = self.tree[i] + self.tree[i + 1]
            i =i//2


    def sumRange(self, left: int, right: int) -> int:
        right += 1
        n = len(self.nums)
        sum = 0

        #to find the sum in the range [l,r)
        l = left + n
        r = right + n

        while l < r:
            if (l % 2 == 1):
                sum += self.tree[l]
                l += 1
            if (r % 2 == 1):
                r -= 1
                sum += self.tree[r]
            l //= 2
            r //= 2
        return sum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
