# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev  # Return the new head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start_prev = None
        start = None
        end = None
        end_next = None
        curr = head
        i = 1
        while curr is not None and i <= right:
            if i < left:
                start_prev = curr
            if i == left:
                start = curr
            if i == right:
                end = curr
                end_next = curr.next
            curr = curr.next
            i += 1
        end.next = None
        new_head = self.reverse(start)  # Use the new_head
        if start_prev is not None:
            start_prev.next = new_head
        else:
            head = new_head 
        start.next = end_next
        return head