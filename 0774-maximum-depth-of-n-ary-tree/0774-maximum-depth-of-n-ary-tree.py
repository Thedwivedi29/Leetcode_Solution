"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node',m=0) -> int:
        if(root==None):
            return 0
        for i in root.children:
          h1=self.maxDepth(i)
          m=max(h1,m)
        return m+1