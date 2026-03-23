from typing import List

class Solution:
    # =========================================================================
    # APPROACH 1: Two Distinct Lists (Prefix and Postfix)
    # =========================================================================
    # The core idea: For any number, the "product except self" is just:
    # (Product of everything to its LEFT) * (Product of everything to its RIGHT).
    #
    # We can do a forward pass to build a 'prefixes' list, and a backward pass 
    # to build a 'postfixes' list. We use a default of 1 for the edges (since 
    # there is nothing to the left of the first element, or right of the last).
    #
    # VISUAL EXAMPLE: nums = [1, 2, 3, 4]
    # nums:      [ 1,  2,  3,  4 ]
    # prefixes:  [ 1,  1,  2,  6 ]  <-- running product from the left
    # postfixes: [ 24, 12, 4,  1 ]  <-- running product from the right
    # result:    [ 24, 12, 8,  6 ]  <-- multiplying them together vertically!
    #
    # Note on Python optimization: Doing `postfixes = [nums[j-1]] + postfixes` 
    # creates a brand new list in memory every loop, which is slow. It's much 
    # faster to use `.append()` and then `.reverse()` the list afterward.
    # =========================================================================
    
    def productExceptSelfNotBest(self, nums: List[int]) -> List[int]:
        res = []
        prefixes = [1]
        postfixes = [1]
        
        # Build prefixes (Left side products)
        for i, num in enumerate(nums):
            if i == 0:
                prefixes.append(num)
            else:
                prefixes.append(prefixes[-1] * num)
                
        # Build postfixes (Right side products)
        for j in range(len(nums), 0, -1):
            if j == len(nums):
                postfixes = [nums[j-1]] + postfixes
            else:
                postfixes = [postfixes[0] * nums[j-1]] + postfixes
                
        # Multiply left and right together
        for k in range(len(nums)):
            res.append(prefixes[k] * postfixes[k+1])
            
        return res
    

    # =========================================================================
    # APPROACH 2: The Optimal One-List Solution (O(1) extra space)
    # =========================================================================
    # We can go one step further and save space by only using our final 'res' list.
    # 
    # 1. Forward pass: Fill 'res' with the prefix products (front to back).
    # 2. Backward pass: Instead of a full postfix list, we just keep a running 
    #    'postfix' variable. We multiply it directly into 'res' on the way back, 
    #    updating the postfix variable as we go down.
    #
    # VISUAL EXAMPLE: nums = [1, 2, 3, 4]
    # 
    # PASS 1 (Forward): 
    # Start res = [1, 1, 1, 1], running prefix = 1
    # End of Pass 1: res = [1, 1, 2, 6] (These are the left-side products)
    #
    # PASS 2 (Backward):
    # Start running postfix = 1
    # i=3: res[3] = 6 * 1  = 6   | new running postfix = 1 * 4 = 4
    # i=2: res[2] = 2 * 4  = 8   | new running postfix = 4 * 3 = 12
    # i=1: res[1] = 1 * 12 = 12  | new running postfix = 12 * 2 = 24
    # i=0: res[0] = 1 * 24 = 24  | new running postfix = 24 * 1 = 24
    # 
    # Final res: [24, 12, 8, 6]
    # =========================================================================

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # 1. Calculate prefixes and store in res
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # 2. Calculate postfixes on the fly and multiply into res
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
            
        return res
