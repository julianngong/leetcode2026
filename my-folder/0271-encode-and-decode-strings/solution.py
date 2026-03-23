class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        tagged = [str(len(x)) + "#" + x for x in strs]
        return "".join(tagged)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        numstartindex = 0
        hashtagindex = 0
        res = []
        while numstartindex < len(s):
            if s[hashtagindex] != "#":
                hashtagindex += 1
            else:
                wordlen = int(s[numstartindex:hashtagindex])
                word = s[hashtagindex + 1:hashtagindex + 1 + wordlen]
                res.append(word)
                numstartindex = hashtagindex + 1 + wordlen
                hashtagindex = numstartindex
        return(res)

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
