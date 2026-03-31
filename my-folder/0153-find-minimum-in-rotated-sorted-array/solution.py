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
    def findMin(self, nums: List[int]) -> int:
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
    

