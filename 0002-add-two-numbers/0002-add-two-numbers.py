# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        carry = 0  
        result = ListNode(0)
        result_current = result  
        while h1 or h2 or carry:
           
            total_sum = carry

            if h1:
                total_sum += h1.val
                h1 = h1.next
            if h2:
                total_sum += h2.val
                h2 = h2.next

            carry = total_sum // 10

            result_current.next = ListNode(total_sum % 10)

            result_current = result_current.next

        return result.next
