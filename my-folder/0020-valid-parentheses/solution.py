class Solution(object):
    def isValid(self, s):
        pairs = {"[":"]", "{":"}", "(":")"}
        stack = ''
        for i in range (len(s)):
            stack += s[i]
            if (len(stack) > 1):
                if (stack[len(stack)-1] == pairs.get(stack[len(stack)-2])):
                    stack = stack[:-2]
        if (len(stack) == 0):
            return True
        else:
            return False
        
