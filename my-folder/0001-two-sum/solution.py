class Solution:
    def twoSumFail(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,1
        numlen = len(nums)
        while i<numlen:
            total = nums[i] + nums[j]
            if total == target:
                return [i,j]
            else:
                if i < j-1 or j == numlen - 1:
                    i += 1
                else:
                    j += 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        firstNumIndex = 0
        for i, val in enumerate(nums):
            remainder = target - val
            if remainder in seenMap:
                return([i, seenMap[remainder]])
            else:
                seenMap[val] = i


'''
they mention if its o(n^2) and space o(1) then its likely it can be changed to o(n) time and space
'''
