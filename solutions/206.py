# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # 3 pointers approach
      if head is None or head.next is None: return head
      cur, prev = head.next, head
      while cur != None:
          next_cur = cur.next
          cur.next = prev
          prev = cur
          cur = next_cur
      head.next = None
      return prev

      # Stack approach
      nodes = []
      cur = head
      new_head = None
      while cur != None:
          nodes.append(cur)
          cur = cur.next
      if nodes:
          new_head = nodes[-1]
      while nodes:
          node = nodes.pop()
          node.next = nodes[-1] if nodes else None
      return new_head
