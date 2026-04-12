# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    
    # ==========================================
    # 1. INITIAL ATTEMPT (TUPLES & LEVEL TRACKING)
    # ==========================================
    # THE IDEA: Because BFS natively processes a tree level-by-level and never 
    # goes backward, attaching a level counter to each node in a tuple 
    # `(curr_level, curr)` is a totally valid way to know which level we are on.
    #
    # THE DOWNSIDE: It requires a lot of manual management. You have to juggle 
    # a global `level` tracker, a `temp` array, and carefully check when the 
    # level number changes to know when to push the array to the final result.
    def levelOrderTry1(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0
        stack = deque([(level,root)])
        temp = []
        
        while stack:
            curr_level, curr = stack.popleft()
            if curr == None:
                continue
            if curr.left:
                stack.append((curr_level + 1, curr.left))
            if curr.right:
                stack.append((curr_level + 1, curr.right))
                
            if level != curr_level:
                level += 1
                res.append(temp)
                temp = [curr.val]
            else:
                temp.append(curr.val)
                
        if temp:
            res.append(temp)
        return res


    # ==========================================
    # 2. THE OPTIMAL "SNAPSHOT" TRICK
    # ==========================================
    # THE CORE REALIZATION: We don't need to manually track the level numbers at all!
    #
    # THE LOGIC BREAKDOWN:
    # 1. The Snapshot: At the start of the `while` loop, the queue holds EXACTLY 
    #    the nodes for the current level. We take a snapshot of how many there are: 
    #    `lenqueue = len(queue)`.
    #
    # 2. The Bounded For-Loop: We run a `for` loop exactly `lenqueue` times. This 
    #    guarantees we only iterate through the things in the current level.
    #
    # 3. Safe Appending: Inside this loop, we pop the current nodes and append 
    #    their left and right children to the back of the queue. Because our `for` 
    #    loop is strictly bounded by the original `lenqueue`, it will NOT accidentally 
    #    process these newly added children.
    #
    # 4. Clean Grouping: Once the `for` loop finishes, the `level` array is 
    #    perfectly complete. We just append it to `res` and the `while` loop starts 
    #    over for the next level.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        
        while queue:
            lenqueue = len(queue)
            level = []
            
            # Process exactly the nodes on the current level
            for i in range(lenqueue):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    # Append children for the next level
                    queue.append(curr.left)
                    queue.append(curr.right)
                    
            if level:
                res.append(level)
                
        return res
