# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
# Approach 1: Saving pointers in hashmap and then matching pointers
#         hashmap = {}
#         while headA or headB:
#             if headA:
#                 if headA not in hashmap:
#                     hashmap[headA] = headA.val
#                     headA = headA.next
#                 else:
#                     return headA
#             if headB:
#                 if headB not in hashmap:
#                     hashmap[headB] = headB.val
#                     headB = headB.next
#                 else:
#                     return headB
#         return None
        def length_linked_list(head):
            ptr, count = head, 0
            while ptr:
                ptr = ptr.next
                count += 1
            return count
        
        lenA, lenB = length_linked_list(headA), length_linked_list(headB)
        skip = abs(lenA - lenB)
        ptrA, ptrB = headA, headB

        while skip>0:
            ptrA = ptrA.next if lenA > lenB else ptrA
            ptrB = ptrB.next if lenA < lenB else ptrB
            skip -= 1
        if ptrA == ptrB:
            return ptrA
        while ptrA and ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
            if ptrA == ptrB:
                break
        return ptrA
            
            
        