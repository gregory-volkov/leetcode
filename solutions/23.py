###############
# My solution #
###############
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists_num = len(lists)
        max_el = 10**4
        cur_node, head = None, None
        cur_nodes = [node for node in lists if node is not None]
        
        while len(cur_nodes) > 0:
            min_i = None
            min_val = max_el
            for i, node in enumerate(cur_nodes):
                if node.val <= min_val:
                    min_i = i
                    min_val = node.val
            min_node = cur_nodes.pop(min_i)
            if min_node.next:
                cur_nodes.append(min_node.next)
            if cur_node is not None: cur_node.next = min_node
            if head is None: head = min_node
            cur_node = min_node
        return head


#############
# Reference #
#############
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next

        if not l1:
            point.next=l2
        else:
            point.next=l1

        return head.next
