class Solution:
    # ==========================================
    # ATTEMPT 1: The "Divide & Conquer" Trap
    # ==========================================
    # What went wrong here? 
    # 1. THE SLICING TRAP: As you noted, doing nums[mp+1:] doesn't just look at the list, 
    #    it creates a brand new physical copy of that half of the list in memory. 
    #    This instantly kills our O(1) space requirement and turns it into O(N).
    # 2. THE DOUBLE RECURSION TRAP: Look at the return statement. If we don't immediately 
    #    find the valley, we return min(search(left), search(right)). Binary search is 
    #    supposed to THROW AWAY half the array. By searching both halves, we degrade our 
    #    time complexity to O(N). We are just doing a really complicated linear scan!
    # 3. EDGE CASE NIGHTMARE: Trying to look at mp-1 and mp+1 forces us to write messy 
    #    code to prevent IndexErrors, especially when the array shrinks to size 1 or 2.
    def findMinFirst(self, nums: List[int]) -> int:
        if nums == []:
            return 99999999
        mp = int(len(nums)/2)
        preceding = nums[mp-1]
        proceding = nums[0] if mp == len(nums)-1 else nums[mp+1]
        if nums[mp] <= preceding and nums[mp] <= proceding:
            return nums[mp]
        return min(self.findMinFirst(nums[mp+1:]), self.findMinFirst(nums[:mp]))
    

    # ==========================================
    # ATTEMPT 2: The Optimal Pointer Approach
    # ==========================================
    # Such a hard question, but here is the trick: The rotated array only goes in one direction. 
    # We are looking for the "inflection point" (the cliff where numbers drop from high to low).
    def findMinOptimal(self, nums: List[int]) -> int:
        # We assume the smallest value is the first number to start, but this will update.
        res = nums[0]
        
        # Start pointers on both ends of the list. We don't slice or copy! 
        l = 0
        r = len(nums) - 1
        
        # We loop while l <= r. Don't worry about index out-of-bounds edge cases! 
        # Even if l and r cross over each other, this while loop instantly catches 
        # them and stops the code before it crashes.
        while l <= r:
            
            # EARLY EXIT CHECK: If the left-most number is smaller than the right-most number, 
            # it means this specific window is PERFECTLY SORTED (no rotation here).
            # The algorithm is designed to find a cliff, so if there is no cliff, 
            # the minimum MUST just be the left-most number. Record it and break early!
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            # Find the middle pointer
            mp = (l + r) // 2
            
            # Always check if the current middle number is our new lowest seen so far. This is important because in the next bit we discard the middle as we look as splits on either side so we need to make sure we track this to see if it was the middle number as it might not be part of the completely sorted list segment
            res = min(res, nums[mp])
            
            # THE CORE LOGIC: Where is the inflection point?
            # If the middle number is bigger than or equal to the left-most number, 
            # that means the ENTIRE LEFT SIDE IS FULLY SORTED. 
            # remember its sorted and shuffled one direction so when this is done the rhs past the inflection contains all numbers all lower than the left. so if at the mp its bigger than the left most then the inflection cant be inside here as if it was this mp would be less.
            # Because it's fully sorted, the "cliff" (and the true minimum) cannot be there.
            if nums[mp] >= nums[l]:
                # Throw away the sorted left half by moving our left pointer past the middle
                l = mp + 1
                
            # Otherwise, the right side must be sorted, meaning the cliff is on the left side.
            else:
                # Throw away the sorted right half by moving our right pointer past the middle
                r = mp - 1
                
        return res
    
    # ---------------------------------------------------------
    # ATTEMPT 1 & 2: THE "LEFT SIDE" PITFALL
    # ---------------------------------------------------------
    def findMinfailed(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            print("l", l, "val", nums[l])
            print("r", r, "val", nums[r])
            print("mp", mid, "val", nums[mid])
            print(nums)
            
            if nums[l] <= nums[r]:
                return nums[l]
            if nums[l] < nums[mid]:
                l = mid+1
            else:
                r = mid-1
                
                
    # ---------------------------------------------------------
    # OPTIMAL SOLUTION
    # ---------------------------------------------------------
    """
    MY REFLECTION & ALGORITHM NOTES:

    1. The "Left Side" Pitfall:
    I made the classic mistake at first: checking the left side (`nums[l] < nums[mid]`). 
    The issue with looking at the left is ambiguity. Even if the left side is perfectly 
    sorted, the absolute minimum could be on the left OR the right. Relying on the left 
    forces you to write messy edge cases to figure out where you are.

    2. The "Right Side" Anchor:
    For finding a minimum, we must ONLY check the right side: `nums[mid] < nums[r]`. 
    The right side deterministically tells us exactly where the "cliff" (the drop-off) is.

    3. Why `r = mid` vs `l = mid + 1`:
    * If `nums[mid] < nums[r]`: The right side is a normal upward slope. The cliff isn't 
      over there. However, `mid` itself might literally be the minimum (the bottom of the 
      cliff), so we CANNOT throw it away. We keep it in our search space by setting `r = mid`.
    * If `nums[mid] > nums[r]`: The cliff is between `mid` and `r`. Because `mid` is strictly 
      larger than `r`, we know mathematically that `mid` CANNOT be the minimum. Since it's a 
      guaranteed loser, we safely step right over it by setting `l = mid + 1`.

    4. The Final Answer:
    Because of how we squeeze the bounds, the loop breaks exactly when `l` and `r` crash 
    into each other (`l == r`). That single surviving number is guaranteed to be the minimum.

    5. Finding a Target vs. Finding a Shape:
    Why does this differ from the standard "Search in Rotated Array" problem? 
    * When searching for a TARGET (a specific number), you need predictability. You use the 
      left side to find the "sorted" half, check if your target lives inside that sorted 
      range, and decide which way to go. 
    * When searching for a SHAPE (the minimum), you don't care about specific numbers or 
      bounds. You just need the right-hand anchor to definitively point you toward the cliff.
    """
    
    def findMindwda(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] < nums[r]:
                # Mid might be the minimum, so keep it!
                r = mid
            else:
                # Mid is definitely NOT the minimum, step over it!
                l = mid + 1
                
        # l and r have converged on the exact minimum
        return nums[l]

        
    # latest solution below
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mp = (l + r) // 2
            if nums[l] <= nums[mp]:
                l = mp + 1
            else:
                r = mp
        return nums[l]



    

