# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        out = ListNode(-1)
        ptr = out
        while l1 and l2:
            temp = 0
            if l1.val <= l2.val:
                temp = l1.val
                l1 = l1.next
            else:
                temp = l2.val
                l2 = l2.next
            ptr.next = ListNode(temp)
            ptr = ptr.next
        ptr.next = l1 or l2
        return out.next
        