class Solution(object):

    def lengthOfLongestSubstring(self, s):
        back, maxx = 0,0
        for front in range (len(s)):
            if (s[front] in s[back:front]):
                back = back + s[back:front].index(s[front]) + 1
            else:
                if (front-back+1>maxx):
                    maxx = front-back+1
        return maxx
            
        
            
            
            
