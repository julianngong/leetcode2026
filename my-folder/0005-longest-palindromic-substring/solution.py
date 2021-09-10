class Solution:
    def palindrome(self,s,l,r):
        templongest = '';
        while ((l>=0) and (r< len(s)) and (s[l] == s[r])):
            l -= 1
            r += 1
        return(s[l+1:r])
    
    def longestPalindrome(self, s):
        longest = ''
        for i in range(len(s)):
            longestodd = self.palindrome(s,i,i)
            longesteven = self.palindrome(s,i,i+1)
            longest = max([longest,longestodd,longesteven], key=len)
        return(longest)
        
