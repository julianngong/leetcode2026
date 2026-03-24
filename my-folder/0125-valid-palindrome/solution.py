class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        min_pointer = 0
        max_pointer = len(s) - 1
        while min_pointer < max_pointer:
            if not s[min_pointer].isalnum():
                min_pointer += 1
            elif not s[max_pointer].isalnum():
                max_pointer -= 1
            elif s[min_pointer] == s[max_pointer]:
                min_pointer += 1
                max_pointer -= 1
            else:
                return False
        return True

# good but thing to note, alpha numeric includes numbers so they are also valid. the .isalnum() function checks if your thing is alphanumeric for you automatically without having to use any asci comparrisons with ord.
# if not allowed to use it can use this code to make sure that its alphanumeric
# def alphaNum(self, c):
# return (ord('A') <= ord(c) <= ord('Z') or
#         ord('a') <= ord(c) <= ord('z') or
#         ord('0') <= ord(c) <= ord('9'))
# another option is goign through one string and making a new string appending things in the old string into the new string in reverse skipping obciously non alphanumeric then comparing if they are the same.

