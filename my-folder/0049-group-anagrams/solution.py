class Solution:
    def groupAnagramsFirstTry(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in sorted_dict:
                sorted_dict[sorted_string].append(string)
            else:
                sorted_dict[sorted_string] = [string]
        return list(sorted_dict.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet_dict = {}
        for string in strs:
            alphlist = [0] * 26
            for char in string:
                alphlist[ord(char) - ord("a")] += 1
            if tuple(alphlist) in alphabet_dict:
                alphabet_dict[tuple(alphlist)].append(string)
            else:
                alphabet_dict[tuple(alphlist)] = [string]
        return list(alphabet_dict.values())

# did it yourself. Big thing to note is this idea that when doign things for anagrams and having to count letters. get yourself a list of 26 letters initialised as 0 then go through and count the counts of them and then compare that tuple or string. note: make sure to use .append() for adding strings to list of strings and not += as that makes the string basically a list of chars then appends that to the list.

        
