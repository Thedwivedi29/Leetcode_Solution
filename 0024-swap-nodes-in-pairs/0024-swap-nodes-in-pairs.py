# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        p=dummy
        f=dummy
        s=dummy
        if not head or not head.next:
            return head
        else:
             while head and head.next:
                f=head
                s=head.next
                p.next=s
                f.next=s.next
                s.next=f
                head=f.next
                p=f
        return dummy.next
