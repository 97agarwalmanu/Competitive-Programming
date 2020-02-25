# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_value = 0
        cur = head
        while cur:
            decimal_value = decimal_value*2 + cur.val
            cur = cur.next
        return(decimal_value)