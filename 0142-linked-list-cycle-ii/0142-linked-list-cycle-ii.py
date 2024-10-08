# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=head
        p2=head
        i=0
        while p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                p1=head
                while p1!=p2:
                    p1=p1.next
                    p2=p2.next
                return p1
            
        # if p1==None or p1.next==None:
        #     return ("no cycle")
        