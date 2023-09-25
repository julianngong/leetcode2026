class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = False
        seen = dict({})
        i=0
        while result == False and i < len(nums):
            if nums[i] not in seen.keys():
                seen[nums[i]] = 1
            else:
                result = True
            i += 1
        return(result)

#The big difference here is using a dicitonary to check if something saved has been seen before as accessing something from list is O(n^2) while for a dictionary is O(n)
