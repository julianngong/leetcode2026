from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = defaultdict(bool)
        for num in nums:
            if uniques[num] == 1:
                return True
            uniques[num] = 1
        return False
    
    def containsDuplicateOptimal(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        
# Note: For things to do with duplicates try thinking about using the set to find the unique ones and then see if theres any comparisons which could be done with the number of elements in the set vs the original list.

# Note: Think about using a set here as its much more memory efficient so can just make an empty set then add the values to the empty set then see if its inside the set.
