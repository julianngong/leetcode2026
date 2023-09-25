class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        ssort = ''.join(sorted(s))
        tsort = ''.join(sorted(t))
        if ssort == tsort:
            return(True)
        else:
            return(False)

    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        print(count)
        for letter in s:
            count[letter] += 1
        for letter in t:
            count[letter] -= 1
        for num in count.values():
            if num !=0:
                return(False)
        return(True)

# Default dict is best to use instead of dict as it handles when you dont already have the key value pair there. if you dont have a key set and you request to access a key it will make a new key there and default its value to 0 if the int parameter is given. if the list parameter is given it will default it to an empty list

        
