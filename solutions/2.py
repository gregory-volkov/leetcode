# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        acc = 0
        head = cur_node = ListNode(None)
        while l1 or l2 or acc:
            fst, snd = l1.val if l1 else 0, l2.val if l2 else 0
            temp_sum = fst + snd + acc
            cur_node.next = ListNode(temp_sum % 10)
            acc = (temp_sum) // 10
            cur_node = cur_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
