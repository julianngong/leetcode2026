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
    # 1. ORIGINAL ATTEMPT (FIXED)
    # ==========================================
    # THE ISSUE: Trying to check if left/right children are None *before* appending 
    # them makes the code messy and crash-prone.
    # 
    # THE FIX: Allow None values to be added to the queues! 
    # - Handle the None checks at the very start of the while loop instead.
    # - PRO TIP: Instead of keeping two separate queues in sync, it is much easier 
    #   to use a single queue of tuples: `queue.append((p_node, q_node))`.
    def isSameTreeFirst(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pstack = deque([p])
        qstack = deque([q])
        res = True
        
        while len(pstack) > 0 and (len(pstack) == len(qstack)):
            currp = pstack.popleft()
            currq = qstack.popleft()
            
            # Handle nulls immediately at the start of the loop
            if currp == None and currq == None:
                continue
            if currp == None or currq == None:
                res = False
                break
            if currp.val != currq.val:
                res = False
                break
                
            # Safe look-aheads for left children
            if (currp.left == None and currq.left == None ) or (currp.left != None and currq.left != None and currp.left.val == currq.left.val):
                pstack.append(currp.left)
                qstack.append(currq.left)
            else:
                res = False
                break
                
            # Safe look-aheads for right children
            if (currp.right == None and currq.right == None ) or (currp.right != None and currq.right != None and currp.right.val == currq.right.val):
                pstack.append(currp.right)
                qstack.append(currq.right)
            else:
                res = False
                break
                
        return res


    # ==========================================
    # 2. THE ITERATION TRICK (BFS)
    # ==========================================
    # THE STRATEGY: Use a single queue of tuples and let `continue` be a shield.
    # 
    # - STEP 1: If both nodes are None, they are identical! We don't add anything 
    #   to the stack, and `continue` safely stops the rest of the loop and grabs 
    #   the next pair.
    # - STEP 2: Because of `continue`, if we reach the `elif`, we KNOW they aren't 
    #   both None. Therefore, if even one is None (or values don't match), it's a 
    #   guaranteed mismatch -> return False.
    def isSameTreeIteration(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque([(p,q)])
        
        while stack:
            currp, currq = stack.popleft()
            
            if currp == None and currq == None:
                continue
            elif currp == None or currq == None or currp.val != currq.val:
                return False
            
            # Blindly append children; the top of the loop will sort out the Nones
            stack.append((currp.left, currq.left))
            stack.append((currp.right, currq.right))
            
        return True
    
    
    # ==========================================
    # 3. THE RECURSION RULE (DFS)
    # ==========================================
    # THE STRATEGY: Always figure out the base cases at the bottom of the tree first.
    # 
    # - Base Case 1: We hit the bottom and both are None. They match! -> return True.
    # - Base Case 2: One is None and the other isn't, or values differ. Mismatch! -> return False.
    # 
    # If we pass the base cases, they are the same so far. We just return whether 
    # the left branches AND the right branches match, trusting the recursion to 
    # bubble the final answer back up to the top.
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None or p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
