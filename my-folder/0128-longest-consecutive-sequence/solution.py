class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
