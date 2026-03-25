class Solution:
    # =========================================================================
    # My Thought Process / Notes:
    # This solution works similarly to Two Sum: you pin one number down and try 
    # to find the sum of the others, which reduces the time complexity from 
    # O(n^3) to O(n^2). 
    #
    # The main idea is that you iterate through the array, setting 'i' as the 
    # first number. Then, for the second number 'j', you only have to iterate 
    # through the remaining elements and check if the negative of their sum 
    # (the target) exists in the hash map. 
    #
    # We don't want any duplicate triplets, and order does not matter. To easily 
    # handle removing duplicates for permutations, think about SORTING. Sorting 
    # allows us to check if a number is a duplicate simply by comparing it to the 
    # previous number. We can just keep incrementing (skipping) until we hit a 
    # new number to ensure we won't process a duplicate again.
    #
    # When choosing an 'i', we need to make sure to decrease its count in the 
    # dictionary so we can't use that exact physical element again. 
    #
    # The special thing this time, though, is that for the second number ('j'), 
    # we CAN use those numbers again for a completely different iteration of 'i'. 
    # So, even though we decrease their counts during the inner loop, we need to 
    # make sure to increase them back again after the inner loop finishes. 
    #
    # Future note: For summing problems, really keep this Two Sum dictionary 
    # pattern in mind!
    # =========================================================================

    def threeSumHashMap(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums = sorted(nums)
        counts = {}

        # (Fun Python trick for the future: you can replace this whole loop 
        # with just `counts = collections.Counter(nums)`)
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
                
        for i in range(len(nums)):
            counts[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, len(nums)):
                counts[nums[j]] -= 1
                
                # NOTE: The 'j - 1 > i' algebra ensures we are at least two 
                # steps ahead of 'i' so we don't accidentally skip valid neighbors.
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                    
                target = -(nums[j] + nums[i])
                
                if target in counts and counts[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i+1, len(nums)):
                counts[nums[j]] += 1
                
        return res
    
    # =========================================================================
    # My Thought Process / Notes:
    # 
    # THE BIG TAKEAWAY: The absolute importance of SORTING. 
    # Sorting does two massive things for us here:
    # 1. Duplicate Handling: It groups duplicates together, letting us skip 
    #    them just by checking if a number is the same as the one next to it.
    # 2. Pointer Math: It gives us a predictable way to adjust our sum. If the 
    #    sum is too big, we move the right pointer left (smaller). If it's too 
    #    small, we move the left pointer right (bigger).
    #
    # THE LOGIC:
    # 1. We iterate through the array, "pinning" the first number. We skip it 
    #    if it's the same as the previous number so we don't start duplicate 
    #    triplets.
    # 2. With the first number pinned, we use two pointers (bp and ep) starting 
    #    at the edges of the remaining list, working inward in O(N) time to 
    #    find the remaining two numbers that complete the sum.
    # 3. When we find a match, we MUST skip duplicates for the left pointer (bp) 
    #    so we don't accidentally log the exact same combination again.
    #
    # THE MATH TRICK: 
    # Notice we don't write a loop to skip duplicates for the right pointer (ep)!
    # Because we force the left pointer to a strictly new/different number, the 
    # total sum will instantly change. On the very next loop, the math will 
    # force the right pointer to move anyway because the sum will be off. 
    # =========================================================================

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # NOTE: Always sort first for Two Pointer array problems!
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums)):
            
            # NOTE: 'if i' prevents checking nums[-1] on the first iteration.
            # Skip this pinned number if we just checked it.
            if i and nums[i] == nums[i-1]:
                continue
                
            bp = i + 1
            ep = len(nums) - 1
            
            while bp < ep:
                threesum = nums[i] + nums[bp] + nums[ep]
                if threesum > 0:
                    ep -= 1
                elif threesum < 0:
                    bp += 1
                else:
                    res.append([nums[i], nums[bp], nums[ep]])
                    bp += 1
                    ep -= 1
                    while nums[bp] == nums[bp - 1] and bp < ep:
                        bp += 1
                        
        return res

            
