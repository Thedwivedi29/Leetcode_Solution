"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        level_start = root

        while level_start:
            current = level_start
            while current:
                if current.left:
                    current.left.next = current.right
                if current.next and current.right:
                    current.right.next = current.next.left
                current = current.next

            level_start = level_start.left

        return root