class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for i in range(len(nums)-1):
            tempnums = nums[:i] + nums[i+1 :]
            if (target-nums[i]) in tempnums:
                if ((i not in output) and (nums.index(target-nums[i]) not in output)):
                    output.append(i)
                    temp = nums[i]
                    nums[i] = 'a'
                    output.append(nums.index(target-temp))
                    nums[i] = temp
        return(output)
        
