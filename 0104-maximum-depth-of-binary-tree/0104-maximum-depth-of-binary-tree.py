# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        h1=self.maxDepth(root.left)
        h2=self.maxDepth(root.right)
        m=max(h1,h2)+1
        return m 