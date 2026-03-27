"""
MY THOUGHT PROCESS:
I had the right idea originally, I just wasn't quite executing it. The core logic is just 
using a sliding window and constantly incrementing up the right-hand side. But note: when 
the right-hand side finds something inside what I've seen, I need to keep popping the 
left-hand side until it's no longer there so there are no longer duplicates, and then 
we can continue. also you always forget you can just ask for a specific thing to be removed from a set in o(1). cant use dictionary for this as it doesnt remove the key so you cant just count the keys. also rather than counting stuff in the set just subtract the indices

THINGS TO NOTE FOR NEXT TIME:
1. "No Duplicates" = Set: If they talk about duplicates not being allowed, always think 
   about using a set to track them.
2. The "For/While" Combo: For sliding windows, the cleanest structure is usually a for loop to relentlessly drive the right pointer forward, containing a while loop that only triggers to drag the left pointer forward when rules get broken.
3. The max() Trick: Rather than tracking the max with if-statements, just do a max() 
   of 2 things (current max vs. new window size). This variable will then always update 
   to the max. (Note: this is called keeping a "running maximum").
4. Window Size Math: Keep `r - l + 1` in mind to always get the exact length of the 
   current valid window!
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r-l+1)
        return res
