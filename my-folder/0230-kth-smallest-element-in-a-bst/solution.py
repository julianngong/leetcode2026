# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import heapq
from typing import Optional

class Solution:
    
    # ==========================================
    # ATTEMPT 1: THE GENERALIZED HEAP APPROACH
    # ==========================================
    # This works for ANY tree or array, but it takes O(N log k) time because 
    # we have to maintain a max-heap of size k while visiting every node.
    def kthSmallestTry1(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque([root])
        heap = []
        while stack:
            curr = stack.pop()
            if curr == None:
                continue
            heapq.heappush(heap, -curr.val)
            if len(heap) > k:
                heapq.heappop(heap)
            stack.append(curr.right)
            stack.append(curr.left)
        return -heapq.heappop(heap)
    
    # ==========================================
    # ATTEMPT 2: IN-ORDER TRAVERSAL (THE BST CHEAT CODE)
    # ==========================================
    # 1. DFS OVER BFS: This is a bit tricky. We want to use a stack and DFS because 
    #    in a Binary Search Tree, the smallest values are as deep to the left as possible.
    #    A stack lets us plunge deep quickly, unlike a queue (BFS).
    #
    # 2. DEFERRING THE VISIT: The big difference here compared to normal DFS is that 
    #    we don't just pop the element and "visit" (process) it right away. Instead, 
    #    we just traverse down, adding the nodes to our "trail" (the stack). We want to 
    #    get to the absolute smallest element, so we say: go all the way to the left 
    #    as far as mathematically possible.
    #
    # 3. POPPING & DECREMENTING: Once we hit a dead end (null), we pop the stack to 
    #    actually "visit" the node. Because we went all the way left, this will ALWAYS 
    #    be the smallest available element. We decrease `k` (our counter for how many 
    #    smallest elements we've visited). If `k == 0`, we found our answer!
    #
    # 4. MOVING RIGHT: If we need to find the next biggest number, we move our pointer 
    #    to the right child (`curr = curr.right`) and repeat the whole process. If there 
    #    is no right child, the inner loop skips, and we just pop the next thing off 
    #    the stack (which is the parent, naturally the next biggest number).
    #
    # 5. IN-ORDER VS PRE-ORDER: This specific pattern is called In-Order Traversal. 
    #    Normally (Pre-Order), you visit the current node first, then traverse left, 
    #    then right. In-Order is different: we traverse Left first. Once you can't anymore, 
    #    you visit the Root, and THEN traverse Right. As you hit a new right, it's like a 
    #    new state, so you traverse all the way left again.
    #
    # 6. THE BST CHEAT CODE: Doing an In-Order traversal on a Binary Search Tree ALWAYS 
    #    goes through the elements in perfectly sorted ascending order. Because of this, 
    #    the Heap approach (which is O(N log k)) is actually slower than just traversing 
    #    in-order and counting to k!
    #
    # ==========================================
    # THE AHA! MOMENT: The Critical 'OR' (`while stack or curr:`)
    # ==========================================
    # Why can't we just use `while stack:`? Because without `or curr`, the code 
    # completely breaks in two specific scenarios:
    # 
    # Scenario 1 (The Ignition): At the very beginning, the stack is empty. If we only 
    # checked `while stack:`, the loop would never start! `or curr` forces it to start.
    #
    # Scenario 2 (The Right-Branch Empty Stack): Imagine a root (10) with only a right 
    # child (20). 
    #   - We try to dive left. No left child! Push 10 to stack: stack=[10], curr=None.
    #   - We pop 10 to visit it. curr=10, stack=[]  <-- THE STACK IS NOW EMPTY!
    #   - We move to the right child. curr=20, stack=[]
    #   *CRITICAL MOMENT:* The loop checks its condition. If we only had `while stack:`, 
    #   the code would see the empty stack, stop completely, and miss the 20! 
    #   Because we use `or curr`, Python sees that curr=20, keeps the loop alive, 
    #   and safely loops back around to process the right branch.
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque([])
        curr = root
        
        while stack or curr:
            # Go as deep left as possible to find the smallest elements
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop and visit the node
            curr = stack.pop()
            k -= 1
            
            # If we've hit the kth smallest, return it
            if k == 0:
                return curr.val
                
            # Move to the right child to find the next slightly larger elements
            curr = curr.right
