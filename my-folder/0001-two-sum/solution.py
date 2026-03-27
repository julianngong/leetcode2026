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
    they mention if its o(n^2) and space o(1) then its likely it can be changed to o(n) time and space. We will look at the remainder and see if the remainder has been previously seen in the history but the important thing is we need to keep track which numbers weve seen as we go through and which index its at.
    '''

    def twoSumSecondAttempt(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        res = []
        for i in range(len(nums)):
            num_to_index[nums[i]] = i
        for j in range(len(nums)):
            remainder = target - nums[j]
            if remainder in num_to_index and num_to_index[remainder] != j:
                res.append(min(j,num_to_index[remainder]))
                res.append(max(j,num_to_index[remainder]))
                return res

    '''
    This was second try and was good because you did the seen map. note we dont need to iterate once to populate and then iterate again. you can just populate in the same pass because although it wont be picked up at the start, by the time you're at the end the thing you need to add would be in the list
    '''
