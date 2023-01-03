# https://leetcode.com/problems/linked-list-cycle/description/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        cur = head
        while cur is not None:
            if cur in nodes:
                return True
            nodes.add(cur)
            cur = cur.next
        return False
