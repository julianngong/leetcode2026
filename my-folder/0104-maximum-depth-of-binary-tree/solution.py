# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxd = 1
        # Why 1 and not 0? 
        # If this is a leaf node, it has no children. The 'if' statements below will not execute. 
        # Starting at 1 guarantees that a single node correctly counts itself and returns a depth of 1.
        if root.left:
            maxd = max(self.maxDepth(root.left) + 1, maxd)
        if root.right:
            maxd = max(self.maxDepth(root.right) + 1, maxd)
        return maxd
        
        
