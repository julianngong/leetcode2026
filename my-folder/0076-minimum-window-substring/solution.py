from collections import Counter

class Solution:
    def minWindowfirstattempt(self, s: str, t: str) -> str:
        count_t = Counter(t)
        res = ""
        l = 0
        for r in range(len(s)):
            substring = s[l:r+1]
            count_substring = Counter(substring)
            if (s[r] in count_t) and (count_t[s[r]] > 0):
                count_t[s[r]] -= 1
            if (set(count_t.values()) == {0}):
                if res == "":
                    res = substring
                elif (len(substring) < len(res)):
                    res = substring
                while set(count_t.values()) == {0} and l < r:
                    substring = s[l:r+1]
                    count_substring = Counter(substring)
                    if (s[l] in count_t) and (count_substring[s[l]] == 0):
                        count_t[s[l]] += 1
                    l += 1
        return res
    
    '''
    All in all, there was a good thought process here to start. I correctly remembered that with a 
    sliding window, you basically make a for loop for the right pointer and adjust the left pointer 
    as you need to. I also had the right idea to hold the left pointer until the window becomes valid, 
    and once it is, increment it only until the window becomes invalid again (rather than blindly 
    pushing it all the way to the right pointer). 
    
    The big thing to note here for the optimized approach is keeping `countT` strictly read-only and 
    comparing it to a separate `window` dictionary, rather than constantly modifying the target counts. 
    Also, to avoid having to re-count or loop through everything inside the sliding window on every 
    single step, we just use `have` and `need` counters. `need` represents the total number of unique 
    characters required by t. `have` increases only when our current window has the exact count 
    required for one of those unique letters.
    
    So the way it actually flows: you work your right pointer up, and as you hit a new letter, add it 
    to the window dictionary. Then, check if this new letter is one that T actually needs, and if its 
    current count in the window is now exactly the same as the target count for T. If it is, add 1 to 
    the `have` counter since we fully satisfied that letter's requirement. Next, we check if `have` and 
    `need` are equal. If they are, we have a valid window! We check if this valid window is shorter than 
    our current best. If it is, we save the left and right indices (which saves a ton of space and memory 
    compared to actually slicing and storing the string every time) and update our best length. After 
    saving, we try to shrink the window by dropping the leftmost letter from the window count. We check 
    if dropping it caused us to not have enough of that letter anymore, and if so, we decrease `have`. 
    Then we move the left pointer up. Lastly, when the whole loop is done, we just check if we actually 
    found anything—if resLen is still infinity, we didn't find anything so we send back "", otherwise 
    we slice the string using our saved indices and send back the shortest substring.
    '''
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = Counter(t), Counter()
        have, need = 0, len(countT) 
        res, resLen = [-1, -1], float("infinity") 
        
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
                
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                    
                l += 1
                
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

    def minWindowTry2(self, s: str, t: str) -> str:
        t_count = Counter(t)
        window_count = Counter()
        l = 0
        need = len(t_count)
        have = 0
        res = ""
        for r in range(len(s)):
            window_count[s[r]] += 1
            if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
                have += 1
            while have == need:
                if res == "":
                    res = s[l:r+1]
                elif r-l+1 < len(res):
                    res = s[l:r+1]
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        return res

# you did this first time mate so so so so good. only other thing to note is you are still using slicing a list here in a loop which we know makes brand new one each time. for efficienct just store a list of 2 which represents left and right pointer and be storing that then only return the slice at the end once we have the solution.

