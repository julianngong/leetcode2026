class Solution:
    """
    MY REFLECTION & ALGORITHM NOTES:

    1. The Two-Element Trap (nums[l] <= nums[mp]):
       My initial mistake was using strictly `<` to check if the left side was sorted. 
       If the search space shrinks down to just 1 or 2 elements, 'l' and 'mp' end up 
       pointing to the exact same index. A single element is technically a perfectly 
       sorted array! By using '<=', we correctly tell the algorithm: "Even if the left 
       side is just a single number staring at itself, treat it as the sorted half."

    2. The While Loop Convergence (while l <= r):
       Unlike 'Find Minimum', searching for a specific target requires us to keep 
       searching until we verify the final number. If we just used '<', the loop would 
       break right before checking the last remaining element. Using '<=' ensures 'l' 
       and 'r' can meet at a single point, allowing 'mp' to land on it and check if 
       it's our target.

    3. The Core Logic (Target vs Shape):
       Because we are looking for a TARGET, we must find the perfectly sorted half first.
       - If the Left is sorted: Is our target mathematically inside it? 
         If yes, search left. If no, search right.
       - If the Right is sorted: Is our target mathematically inside it? 
         If yes, search right. If no, search left.
    """

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        
        while l <= r:
            mp = (l + r) // 2
            
            # Target found!
            if nums[mp] == target:
                res = mp
                break
            
            # Is the Left side the perfectly sorted half? (<= catches the 1-element edge case)
            if nums[l] <= nums[mp]:
                # Is the target hiding inside this sorted left half?
                if target >= nums[l] and target < nums[mp]:
                    r = mp - 1  # Search left
                else:
                    l = mp + 1  # Search right
            
            # Otherwise, the Right side MUST be the perfectly sorted half
            else:
                # Is the target hiding inside this sorted right half?
                if target > nums[mp] and target <= nums[r]:
                    l = mp + 1  # Search right
                else:
                    r = mp - 1  # Search left
                    
        return res
