# The way this works is for each index we calculate its multiples of everything else by looking at the multiples of all things to the left of it multiplied by the multiples of all things to the right. In first attempt we go through and multiply each element to the running multipliction todal up to that point and each time we do a new multiplication we add it to the list. similarly with all the elements multiplied from the right then we pair them up at the end and multiply them together. the second way we do it is starting with the result being one (as for the first elelment we multiple everyhting to the right and as there is nothing to the left we are essentially timsing by 1) we fill in the multiples from the left as we did before. then we start from the back and in the same list multiply each one by the running multiplicaitno total from the right until we reach the end

class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        result = []
        multiplesbeforeindex = []
        multiplesafterindex = []
        currentbefore = 1
        currentafter = 1
        for i in range(len(nums)):
            currentbefore = currentbefore*nums[i]
            multiplesbeforeindex.append(currentbefore)
            currentafter = currentafter*nums[len(nums)-1-i]
            multiplesafterindex = [currentafter] + multiplesafterindex
        for i in range(len(nums)):
            if i == 0:
                result.append(multiplesafterindex[1])
            elif i == len(nums)-1:
                result.append(multiplesbeforeindex[i-1])
            else:
                result.append(multiplesbeforeindex[i-1]*multiplesafterindex[i+1])
        return(result)
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        currentbefore = 1
        currentafter = 1
        for i in range(len(nums)):
            result+=[currentbefore]
            currentbefore = currentbefore*nums[i]
        for i in range(len(nums)-1,-1,-1):
            result[i]*=currentafter
            currentafter = currentafter*nums[i]
        return(result)
