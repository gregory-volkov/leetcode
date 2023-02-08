# 430. Flatten a Multilevel Doubly Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        buffer = []
        prev = None
        cur = head
        while cur:
            if cur.child:
                if cur.next:
                    buffer.append(cur.next)
                cur.prev = prev
                prev = cur
                cur.next = cur.child
                cur = cur.child
            else:
                if cur.next:
                    cur.prev = prev
                    prev = cur
                else:
                    if buffer:
                        popped = buffer.pop()
                        cur.next = popped
                    cur.prev = prev
                    prev = cur
                cur = cur.next
            prev.child = None
        return head
