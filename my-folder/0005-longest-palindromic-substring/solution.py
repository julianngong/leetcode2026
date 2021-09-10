class Solution(object):
    def longestPalindrome(self, s):
        currentmax = ''
        for i in range (len(s)):
            j = 1
            tempmax = s[i]
            while ((i-j>=0) and (i+j < len(s))):
                if (s[i-j] == s[i+j]):
                    tempmax = s[i-j] + tempmax + s[i+j]
                    j += 1
                else:
                    j = len(s)
            if (len(tempmax) > len(currentmax)):
                currentmax = tempmax
            if (i+1<len(s)):
                if (s[i] == s[i+1]):
                    j = 1
                    tempmax = s[i] + s[i+1]
                    while ((i-j>=0) and (i+1+j< len(s))):
                        if (s[i-j] == s[i+1+j]):
                            tempmax = s[i-j] + tempmax + s[i+1+j]
                            j += 1
                        else:
                            j = len(s)
                    if (len(tempmax) > len(currentmax)):
                        currentmax = tempmax
        return(currentmax)
                   
                   
                   
                
        
        
