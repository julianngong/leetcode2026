class Solution:
    def longestConsecutiveTry1(self, nums: List[int]) -> int:
        starting_nums = []
        setmap = set(nums)
        maxlen = 0
        for num in setmap:
            if num-1 not in setmap:
                currentlen = 1
                nextnum = num + 1
                while nextnum in setmap:
                    currentlen+=1
                    nextnum += 1
                if currentlen > maxlen:
                    maxlen = currentlen
        return maxlen

    # Completed but had to use neetcode hints.
    # things to note, if you need to check if something is in the list at all, convert the list to a set because then we can check if something is in the set with o(1). also iterating through the set vs the list means if there are loads of duplicates it makes it more efficient as doesnt have to check 1 over and over again. the idea here is we know it must be a start of a subsequence if the previous number is not in the list. then at this point keep checking if each one is in the list until its not then this is the substring. keep count of this max.

    def longestConsecutiveTry2(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        count = 1
        for i, num in enumerate(nums):
            if num-1 not in nums_set:
                comparison_num = num + 1
                while comparison_num in nums_set:
                    comparison_num+=1
                res = max(comparison_num - num, res) 
        return res
    
    # completed but still needed neetcode hints. benefit this time is that i remembered to make nums_set to not do duplicated and allowing o(1) for checking if something is in a collection then checking if something is in the list directly. especcially as we dont need to bother checking duplicates.
    # big thing i keep forgetting again is what makes something the start of a consecutive sequence and that is when the previous number is not in the list. once this is found then i can start counting up and seeing if in the set.  

    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in numset:
            if num-1 not in numset:
                count = 1
                while num + 1 in numset:
                    count += 1
                    num += 1
                res = max(count, res)
        return res
    # completed this time no hints just good stuff
