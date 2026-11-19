# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1=headA
        c2=headB
        seen=set()
        while c1!=None:
            seen.add(c1)
            c1=c1.next
        while c2!=None:
            if c2 in seen:
                return c2
            c2=c2.next
        return None