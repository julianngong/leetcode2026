from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for string in strs:
            if len(string)!=0:
                sortedstring = ''.join(sorted(string))
            else:
                sortedstring = string
            dd[sortedstring].append(string)
        return list(dd.values())
            
