# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    # ==========================================
    # FUNCTION 1: THE SEARCHER (isSubtree)
    # ==========================================
    # THE GOAL: Traverse the main `root` tree. At every single node we visit, 
    # we stop and ask our helper function: "Does the subRoot start exactly here?"
    #
    # THE LOGIC BREAKDOWN:
    # 1. Base Case (Empty subRoot): An empty tree is technically a valid subtree 
    #    of ANY tree. So if subRoot is None, we automatically return True.
    #
    # 2. Base Case (Empty main root): If our main tree is empty (or we've searched 
    #    all the way down to a leaf's empty child) but our subRoot ISN'T empty, 
    #    it's impossible to find a match here. Return False.
    #
    # 3. The "Match" Check: We use our helper function `isSameTree`. If it returns 
    #    True, it means the entire tree from this exact node downwards matches 
    #    the subRoot exactly. We found it! Return True.
    #
    # 4. The "Keep Looking" Step: If `isSameTree` was False, we don't give up. 
    #    We branch out and keep searching down the tree. We use `OR` because 
    #    we only need to find the subRoot on the left side OR the right side. 
    #    If either branch eventually finds it, the `True` will bubble all the 
    #    way back up.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
            
        if root == None:
            return False
            
        if self.isSameTree(root, subRoot):
            return True
            
        # Keep searching down the tree! (This is why we call `isSubtree` here, not `isSameTree`)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    # ==========================================
    # FUNCTION 2: THE HELPER (isSameTree)
    # ==========================================
    # THE GOAL: Check if two trees are 100% identical starting from exactly 
    # where we are right now. (It does NOT search the rest of the tree like isSubtree does).
    #
    # THE LOGIC BREAKDOWN:
    # 1. If we reach the bottom of both trees at the exact same time (both are None), 
    #    they are identical. Return True.
    # 2. If only ONE is None, or if the values inside the nodes don't match, 
    #    the structural match is broken. Return False immediately.
    # 3. If we pass the checks above, the current nodes match! Now, check if the 
    #    left branches match AND the right branches match.
    def isSameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if t1 == None and t2 == None:
            return True
            
        if t1 == None or t2 == None or t1.val != t2.val:
            return False
        
        # We use `AND` here because for a tree to be exactly the same, 
        # the left side AND the right side must be perfect matches.
        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
