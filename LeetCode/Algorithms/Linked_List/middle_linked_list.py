# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast_pointer = head
        slow_pointer = head
        while fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if fast_pointer.next != None:
                fast_pointer = fast_pointer.next
        return slow_pointer
            
        