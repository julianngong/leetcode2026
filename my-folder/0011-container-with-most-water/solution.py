from typing import List

class Solution:
    # =========================================================================
    # My Thought Process / Notes:
    #
    # WHY NO DICTIONARY? 
    # Hash maps are for finding exact target matches (like Two Sum). Here, we 
    # are maximizing an equation (Area = Width * Height), not looking for a 
    # specific number, so a dictionary doesn't help us.
    #
    # THE "BOTTLENECK" THEORY (Why Two Pointers works in O(N) time):
    # To find the max area, we start with the absolute maximum WIDTH by placing 
    # pointers at the far left and far right. 
    #
    # Every time we move a pointer inward, we lose width. The ONLY way to make 
    # up for that lost width is to find a taller height. 
    # 
    # The water level is always restricted by the SHORTER line (the min). 
    # If we keep the shorter line and move the taller line inward, the height 
    # can NEVER increase, but the width shrinks. The area is guaranteed to get 
    # smaller. Therefore, we MUST always throw away the shorter line and move 
    # that pointer inward, hoping to find a taller line to compensate for the 
    # shrinking width.
    # =========================================================================

    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        maxarea = 0
        
        while lp < rp:
            # The water level is bottlenecked by the shorter of the two lines
            h = min(height[lp], height[rp])
            length = rp - lp
            area = length * h
            
            # Update max area if we found a bigger container
            if area > maxarea:
                maxarea = area
                
            # THE CRUCIAL LOGIC:
            # Always abandon the shorter line. Keeping it guarantees a smaller 
            # area on the next loop because the width is shrinking.
            if height[lp] <= height[rp]:
                lp += 1
            else:
                rp -= 1
                
        return maxarea
