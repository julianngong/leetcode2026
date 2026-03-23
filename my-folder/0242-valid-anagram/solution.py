from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCount = defaultdict(int)
        for sletter in s:
            letterCount[sletter] += 1
        for tletter in t:
            letterCount[tletter] -= 1
            if letterCount[tletter] < 0:
                return False
        if set(letterCount.values()) == {0}:
            return True
        return False

# Good solution, can't see anything wrong with it and a good early break case for when it goes negative. Can do it in one pass tho using enumerate. unemerate through s or t as they have to have the same length to be correct then decrement each one and do the same checking you did.
'''
for i,_ in enumerate(s):
            cnt[s[i]]+=1
            cnt[t[i]]-=1
'''
        
