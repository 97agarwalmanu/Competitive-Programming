# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        output = ListNode(-1)
        ptr = output
        while l1 != None or l2 != None:
            ptr.next = ListNode(-1)
            ptr = ptr.next
            a = 0
            b = 0
            if l1 != None:
                a = l1.val
                l1 = l1.next
                
            if l2 != None:
                b = l2.val
                l2 = l2.next
            ptr.val = (a + b + carry) % 10
            carry = (a + b + carry) // 10
        if carry > 0:
             ptr.next = ListNode(carry)
        return output.next
        