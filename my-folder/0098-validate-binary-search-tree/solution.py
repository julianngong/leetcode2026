# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional

class Solution:
    
    # ==========================================
    # ATTEMPT 1: MANUAL LOOK-AHEADS
    # ==========================================
    def isValidBSTFirst(self, root: Optional[TreeNode]) -> bool:
        q = deque([(-float("inf"), float("inf"), root)])
        while q:
            minval, maxval, curr = q.popleft()
            if curr == None:
                continue
            if (curr.right and curr.right.val <= curr.val) or (curr.left and curr.left.val >= curr.val) or (curr.val >= maxval) or (curr.val <= minval):
                return False
            q.append((curr.val, maxval, curr.right))
            q.append((minval, curr.val, curr.left))
        return True
    
    # ==========================================
    # ATTEMPT 2: THE RANGE "SQUEEZE" LOGIC
    # ==========================================
    # Good question. I completed it after the hint (as seen above) but it needed 
    # some simplifying of the logic, and I didn't fully understand the min/max value 
    # stuff at first. 
    #
    # Basically, the vital thing to note for a Binary Search Tree is that everything 
    # on the right-hand side of a node must be BIGGER than that node, and everything 
    # on the left-hand side must be SMALLER. For example, every single value in the 
    # entire right half of the tree has to be bigger than the root.
    # 
    # Because of this deep structural rule, we must track individual "valid ranges" 
    # as we go, rather than just checking if the immediate left and right children 
    # are valid compared to their direct parent. 
    #
    # 1. At the start, the root node can be anything, so its valid range is 
    #    (-infinity to +infinity).
    #
    # 2. As you go down the LEFT branch, the new node must be bigger than the current 
    #    minimum (which might still be -infinity), but strictly smaller than the 
    #    current node. So, the parent's value becomes the new maximum (the ceiling).
    #
    # 3. This leads to a huge simplification: we ONLY need to check if the current 
    #    node fits inside its inherited range. We do NOT need to worry about checking 
    #    the children ahead of time. The children will get checked automatically 
    #    when they are popped from the queue with their newly updated ranges.
    #
    # 4. Now, if we go down the RIGHT-hand side, we update the new minimum (the floor) 
    #    to be the parent's value, while keeping whatever the maximum already was.
    #
    # Because this range-passing happens continuously as we traverse the queue, the 
    # rules from the very top of the tree are preserved all the way down. This means 
    # a node deep in the left subtree will still rightfully fail if it is larger than 
    # the root node. This process slowly shrinks and "squeezes" the valid ranges 
    # inward until we either validate the whole tree or catch a node out of bounds.
    #
    # THE AHA MOMENT (Why not just check the immediate children?):
    # If you only check the immediate children against the parent, the node has amnesia. 
    # It knows who its dad is, but it completely forgets its grandpa. The minval/maxval 
    # trick gives the node perfect memory of its entire family line.
    #
    # Example: Grandpa=10, Dad=5 (Left of Grandpa), Child=12 (Right of Dad)
    # - Amnesia Method: If we only check curr.right.val <= curr.val, we look at Dad (5) 
    #   and Child (12). "Is 12 > 5?" YES. It wrongly says it's valid. (Bug, because 12 is 
    #   on the left side of 10!)
    # - Perfect Memory Method: Grandpa (10) goes left -> sets the ceiling: maxval = 10. 
    #   Dad (5) goes right -> sets the floor: minval = 5, BUT passes down the ceiling of 
    #   10 from the Grandpa! At the Child (12), we pop the queue and ask: "Is 12 between 
    #   5 and 10?" NO. The code catches the bug!
    #
    # WAIT, DOESN'T MAXVAL EVENTUALLY GET OVERWRITTEN?
    # Yes! If you take multiple LEFT turns in a row, the ceiling gets overwritten. But 
    # overwriting isn't amnesia; it is tightening the squeeze. 
    # If Grandpa says "Must be < 100", and Dad says "Actually, must be < 80", overwriting 
    # 100 with 80 is perfectly safe. If a node obeys the stricter rule (< 80), it 
    # automatically obeys the older rule (< 100). The limits only get overwritten by 
    # stricter constraints!
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(float("-inf"), float("inf"), root)])
        
        while q:
            minval, maxval, curr = q.popleft()
            
            if curr == None:
                continue
                
            # The only check we need: Does the node fit in its inherited box?
            if curr.val <= minval or curr.val >= maxval:
                return False
                
            # Going Left: Update the maximum (ceiling) to the parent's value
            q.append((minval, curr.val, curr.left))
            
            # Going Right: Update the minimum (floor) to the parent's value
            q.append((curr.val, maxval, curr.right))
            
        return True
