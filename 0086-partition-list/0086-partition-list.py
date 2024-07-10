# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1=ListNode(-1)
        dummy2=ListNode(-1)
        h1=dummy1
        h2=dummy2
        while(head!=None):
           
            if (head.val<x):
                h1.next=head
                h1=h1.next
            if (head.val>=x):
                h2.next=head
                h2=h2.next
            head=head.next
        h1.next=dummy2.next
        h2.next=None
        return dummy1.next