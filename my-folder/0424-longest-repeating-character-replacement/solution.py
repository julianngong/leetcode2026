from collections import defaultdict

class Solution:
    # This one is quite hard. Basically, it's a sliding window where you iterate through 
    # to find the longest window that meets our requirements. 
    # 
    # The Requirement: For a replacement to be valid, we look at the total size of the window 
    # and subtract the count of the most frequent character in that window. If the remaining 
    # characters (which are the ones we need to replace) are <= k, the window is valid.
    # If the remaining characters > k, the window is invalid, so we shrink it from the left 
    # (moving 'l' forward and decrementing counts) until it becomes valid again.
    #
    # THE GENIUS OF 'maxf': 
    # 'maxf' represents the HISTORICAL maximum frequency of a single character we've ever 
    # seen in ANY window so far. Why don't we recalculate it when the window shrinks? 
    # Because we only care about finding the *longest possible* window. To beat our current 
    # high score (res), we MUST find a new window with an even higher character frequency. 
    # If our window shrinks, we don't care if the current window's actual max frequency goes 
    # down, because a lower frequency can't possibly help us beat our record 'res' anyway!
    # We just keep 'maxf' as our high-water mark. This avoids scanning the whole dictionary,
    # making the code a true O(N) instead of O(26N).
    def characterReplacementIdeal(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        
        # I'm noticing for a lot of sliding window problems, you don't need a messy 
        # while loop that goes on forever for the right pointer. Just use a for loop 
        # to drive it! It processes one new character safely per loop.
        for r in range(len(s)): 
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            
            # If (total window size) - (historical max frequency) > replacements allowed
            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res
    
    
    # Same logic as above, but this is the more intuitive, brute-force version. 
    # It explicitly calculates the exact max character count for the live window 
    # every single time. It's much easier to wrap your head around, but slower.
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        letter_window_count = defaultdict(int)
        max_window = 0
        
        # 1. Let r drive the window safely to prevent IndexErrors
        for r in range(len(s)):
            letter_window_count[s[r]] += 1
            
            # 2. Get the actual max frequency of the current live window
            # The only issue is this takes 26 operations each time (scanning the whole alphabet),
            # so this whole thing becomes O(26N) instead of O(N).
            max_count = max(letter_window_count.values()) 
            window = r - l + 1
            
            # 3. If the window is invalid, shrink it from the left until it is valid
            while window - max_count > k:
                letter_window_count[s[l]] -= 1
                l += 1
                window = r - l + 1
                
                # We have to recalculate the max_count every time we shrink the window here
                max_count = max(letter_window_count.values())
            
            # 4. By this point, the window is guaranteed to be valid
            max_window = max(max_window, window)
            
        return max_window
    
    def characterReplacementTry2(self, s: str, k: int) -> int:
        res = 0
        l = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            maxcount = max(counts.values())
            numchars = r-l+1 
            if numchars - maxcount <= k:
                res = max(res, r-l+1)
            else:
                while numchars - maxcount > k:
                    counts[s[l]] -= 1
                    l += 1
                    maxcount = max(counts.values())
                    numchars = r-l+1 
        return res

    """
    MY REFLECTION & OPTIMIZATION NOTES:
    
    1. Try 2 Mistake: I calculated `maxcount` and `numchars` *before* adjusting counts. They used the same `l` and `r` that triggered the loop, so they never changed!
    
    2. The O(26*N) Inefficiency: Calling `max(counts.values())` scans all 26 letters every single time we move the pointers.
    
    3. The O(N) Trick (`maxf`): Just track the historical max frequency instead (`maxf = max(maxf, counts[s[r]])`). 
    
    4. Why it works: When we shrink the window, we don't lower `maxf` even if the actual max drops. Why? We only care about finding a *larger* result, which mathematically requires beating our historical `maxf` anyway. A "stale", high `maxf` just safely bottlenecks the window size until we find a character that actually beats it!
    """

    def characterReplacementSol(self, s: str, k: int) -> int:
        res = 0
        l = 0
        counts = defaultdict(int)
        maxf = 0
        
        for r in range(len(s)):
            counts[s[r]] += 1
            maxf = max(maxf, counts[s[r]]) # Only check against historical max
            numchars = r-l+1 
            
            if numchars - maxf <= k:
                res = max(res, r-l+1)
            else:
                while numchars - maxf > k:
                    counts[s[l]] -= 1
                    l += 1
                    numchars = r-l+1 
                    
        return res
    
    def characterReplacement(self, s: str, k: int) -> int:
        windowcount = defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            windowcount[s[r]] += 1
            maxf = max(windowcount[s[r]], maxf)
            while (r-l+1) - maxf > k:
                windowcount[s[l]] -= 1
                l = l+1
            res = max(res, r-l+1)
        return res
