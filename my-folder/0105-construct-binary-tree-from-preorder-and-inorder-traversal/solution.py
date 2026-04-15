# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTreeEasy(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        APPROACH:
        This solution builds the tree by relying on the core characteristics of Preorder 
        (Root -> Left -> Right) and Inorder (Left -> Root -> Right) traversals.

        1. Identify the Root: 
           In a preorder traversal, the first element is always the root of the tree.
        
        2. Find Subtree Sizes: 
           By finding the root's index in the inorder traversal (`in_index`), we know 
           exactly how many elements belong to the left branch. Because inorder is 
           [Left... Root... Right], the index of the root is exactly equal to the 
           TOTAL NUMBER of nodes in the left subtree.
        
        3. Build Left Subtree (The "One-Off" Offset Logic):
           - Inorder slice: Everything up to, but not including, the root (`[:in_index]`).
           - Preorder slice: We must skip the first element (the root, at index 0). Then, 
             we need to grab exactly `in_index` amount of elements. Therefore, we start at 
             index 1, and go up to index `in_index + 1`. This offset by 1 is entirely 
             because the root sits at the very front of the preorder array.
             Slice: `[1 : in_index + 1]`
        
        4. Build Right Subtree:
           - Inorder slice: Everything after the root (`[in_index + 1:]`).
           - Preorder slice: The right subtree elements start exactly where the left 
             subtree elements ended. So we pick up starting at `in_index + 1` and take 
             the rest of the array.
             Slice: `[in_index + 1 : ]`

        5. Return the Node: 
           Attach the left and right children and return the root up the recursive chain.

        DRAWBACKS (Why we optimize later):
        While conceptually great, doing list slicing (`preorder[...]`) in Python creates 
        a brand-new list in memory each time. This makes it expensive in both memory and 
        time. The ideal next step is to pass index pointers instead of slicing.
        """
        if not preorder or not inorder:
            return None
        
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        rootNode = TreeNode(preorder[0])
        in_index = inorder_map[rootNode.val]
        
        rootNode.left = self.buildTree(preorder[1 : in_index + 1], inorder[:in_index])
        rootNode.right = self.buildTree(preorder[in_index + 1 :], inorder[in_index + 1 :])
        
        return rootNode

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # 1. THE SPATIAL MAP (Where things go)
        # The inorder array tells us the boundaries. By finding the root here, 
        # we know exactly how many nodes belong to the left and right subtrees.
        # We use a hash map to turn the O(N) search into an instant O(1) lookup.
        indices = {val: idx for idx, val in enumerate(inorder)}

        # 2. THE CHRONOLOGICAL CONVEYOR BELT (What to build next)
        # The preorder array tells us the exact order nodes are built: [Root -> Left -> Right].
        # THE BACKTRACK MAGIC: Because this is a class instance variable (`self.`), 
        # it ignores the recursion backtracking. Even when the recursive functions bounce 
        # up and down the tree, this pointer ONLY ever moves forward.
        self.pre_idx = 0
        
        # 3. THE RECURSIVE HELPER
        # 'l' and 'r' are our imaginary fences in the inorder map.
        def dfs(l, r):
            
            # BASE CASE: The fences crossed.
            # No elements are left in this boundary to build a tree with.
            if l > r:
                return None

            # GRAB THE ROOT
            # We grab the current item off the conveyor belt and immediately move 
            # the belt forward by 1. 
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # FIND THE SPLIT 
            # Ask the map: "Where is this root?" Everything to its left goes 
            # to the left child, everything to its right goes to the right child.
            mid = indices[root_val]
            
            # BUILD THE LEFT CHILD
            # We pass in new fences. The left fence stays ('l'), the right moves ('mid - 1').
            root.left = dfs(l, mid - 1)
            
            # THE BLACK BOX TIMING (Why the right child works without index math)
            # Python executes sequentially. The line below CANNOT run until the 
            # entire left side above is 100% finished building. 
            # During that time, the left side acts as a "black box," eating exactly 
            # the right amount of nodes off the conveyor belt and ticking `self.pre_idx` 
            # forward. By the time the code finally reaches this line, `self.pre_idx` 
            # is mathematically guaranteed to be sitting on the exact correct root 
            # for the right subtree!
            
            # BUILD THE RIGHT CHILD
            # The left fence moves ('mid + 1'), the right fence stays ('r').
            root.right = dfs(mid + 1, r)
            
            # Return the fully built subtree back up the recursive stack
            return root

        # 4. KICKSTART THE RECURSION
        # Start with the fences surrounding the entire inorder array map.
        return dfs(0, len(inorder) - 1)
