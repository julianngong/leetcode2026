# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    # ==========================================
    # LOWEST COMMON ANCESTOR IN A BST
    # ==========================================
    # THE CORE IDEA: The Lowest Common Ancestor (LCA) is simply the lowest node 
    # where the paths to `p` and `q` diverge (split).
    #
    # 1. THE SPLIT CASE: If we are going down the tree and see that `p` and `q` 
    #    belong in separate branches (one is > curr, the other is < curr), the 
    #    current node is the junction that joins them. We return the current node.
    # 
    # 2. THE EQUALS CASE: If the current node's value is exactly equal to `p` or `q`, 
    #    then no matter where the other node is further down the tree, the current 
    #    node MUST be the parent/ancestor. We return the current node.
    #
    # 3. THE TRAVERSAL: Because this is a Binary Search Tree (BST), if both values 
    #    are strictly greater than the current node, we know they are both located 
    #    down the right branch. If both are strictly less, they are down the left. 
    #    We just update our pointer (`curr = curr.right` or `curr = curr.left`) 
    #    and repeat the check.
    #
    # 4. THE `ELSE` CATCH-ALL: In the optimized solution, the `else` statement is 
    #    brilliant because it catches everything else. If the values aren't *both* #    greater, and aren't *both* less, it means they either split, or one of them 
    #    equals the current node. In either scenario, we just return `curr`.
    #
    # 5. POINTER VS. STACK: We do NOT need a queue or stack here! Because we know 
    #    exactly which side they are on, we only ever follow a single, predictable 
    #    path down the tree. We don't need a data structure to remember multiple 
    #    paths; a single pointer is enough to trace down to the answer.
    
    def lowestCommonAncestorFirstWithHints(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = deque([root])
        while stack:
            curr = stack.popleft()
            if curr == None:
                continue
            if curr.val == p.val:
                return p
            if curr.val == q.val:
                return q
            if (p.val > curr.val and q.val < curr.val) or (p.val < curr.val and q.val > curr.val):
                return curr
            if p.val > curr.val:
                stack.append(curr.right)
            else:
                stack.append(curr.left)
        return root
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
