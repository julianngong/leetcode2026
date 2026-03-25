from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        close_to_open = {
            ")":"(",
            "}":"{",
            "]":"["
            }
        open_symbols = set(["(", "{", "["])
        for char in s:
            if char in open_symbols:
                stack.append(char)
            else:
                if len(stack) > 0:
                    popped = stack.pop()
                else:
                    return False
                if close_to_open[char] != popped:
                    return False
        return True if len(stack) == 0 else False
