# 1146. Snapshot Array
# https://leetcode.com/problems/snapshot-array/
class SnapshotArray:

    def __init__(self, length: int):
        self.data = [{0: 0} for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.data[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.data[index]:
            return self.data[index][snap_id]
        else:
            return self.data[index][max(k for k in self.data[index].keys() if k < snap_id)]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
