from collections import Counter

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

    """
    Notes: 3Sum (Dictionary/Counter Approach)

    General Rule of Thumb: Whenever a problem asks you to find unique combinations 
    and specifically says "avoid duplicates," your first instinct should be to sort 
    the array. Sorting groups duplicates together, making them easy to skip.

    The Strategy: 
    I nearly did this right on the first try for the dictionary approach. The idea 
    is to fix the first two numbers (nums[i] and nums[j]) and use a Counter to instantly 
    look up if the required third number (target = -twosum) exists.

    Handling Duplicates:
    Because the list is sorted, we can easily avoid duplicate triplets. If our current `i` 
    or `j` is the exact same number as the previous `i` or `j`, we just skip it using `continue`. 

    Managing the Counter (The tricky part):
    1. We decrement `seen[nums[i]]` and `seen[nums[j]]` as we iterate so we don't accidentally 
    reuse the exact same element to form our target.
    2. After checking all possible `j`'s for a specific `i`, we have to restore the counts 
    for the `j` loop so the next `i` can use those numbers.
    3. Crucial note: You DON'T need to increment/restore `seen[nums[i]]`. Once we finish an `i` 
    loop, we are completely done using that specific number as a starting point, so we just 
    leave it decremented and move on.
    """

    def threeSumTry2(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # Sort first to easily skip duplicates later
        seen = Counter(nums)
        res = []
        
        for i in range(len(nums) - 1):
            # Remove nums[i] from available pool
            seen[nums[i]] -= 1
            
            # Skip duplicate 'i' values to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, len(nums)):
                # Remove nums[j] from available pool
                seen[nums[j]] -= 1
                
                # Skip duplicate 'j' values (make sure we don't check j against i)
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                    
                twosum = nums[i] + nums[j]
                target = -twosum
                
                # If the required 3rd number is still available in our pool, we found a match
                if seen[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            # Restore the pool for the next 'i' iteration
            # Note: We ONLY restore the 'j' values. We do NOT restore seen[nums[i]] 
            # because we are permanently done searching with this 'i'.
            for j in range(i + 1, len(nums)):
                seen[nums[j]] += 1
                
        return res
    """
    # 2. Why MUST I skip duplicates for `sp`?
    Once we find a valid triplet that equals 0, we increment `sp` and decrement `ep`. 
    But if the *new* `sp` is the exact same number as the old `sp`, the two-pointer logic 
    will eventually just find the exact same triplet again. To guarantee unique combos, 
    we have to keep pushing `sp` forward until it sits on a brand-new number.

    3. Why DON'T I need a `while` loop to skip duplicates for `ep`?
    Because the math naturally takes care of it for us! If we force `sp` to move to a 
    *new, unique* number, the required value to reach 0 completely changes. If `ep` happens 
    to be sitting on a duplicate of its previous value, the sum will simply be too big 
    or too small, and the normal `elif total > 0` or `elif total < 0` logic will naturally 
    push `ep` along on the next iteration. Skipping duplicates on just *one* of the two 
    pointers (usually the left one) is enough to break the cycle.
    """
    def threeSumTry2Pointer(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            sp = i+1
            ep = len(nums)-1
            while sp < ep:
                total = nums[i] + nums[sp] + nums[ep]
                if total > 0:
                    ep -= 1
                elif total < 0:
                    sp += 1
                else:
                    res.append([nums[i], nums[sp], nums[ep]])
                    ep -= 1
                    sp += 1
                    while nums[sp] == nums[sp-1] and sp < ep:
                        sp += 1
        return res

    """
    MY THOUGHT PROCESS & NOTES:

    1. First thing: I remembered the need for sorting! 
       This is the key to the whole problem because we need to easily skip duplicates.
       - Bonus realization here: Because it's sorted, if the first pointer `a` lands on a 
         number > 0, every number after it is also strictly positive. You can never add 
         positive numbers together to get 0, so we can just `break` and finish early!

    2. Next up, avoiding duplicate starting numbers (`a`): 
       We are allowed to use the same number twice in a single answer, but we don't want 
       to evaluate the exact same starting number twice for different answers. So, I look 
       behind: if `i > 0` and it matches the previous value, I `continue` and skip it to 
       make sure there is no double counting.

    3. Now inside the loop (The Sliding Window): 
       I remembered this is a two-pointer problem, not another for-loop! I set `j` to 
       the start (`i + 1`) and `k` to the end. I calculate the sum: if it's too big 
       (> 0), I move `k` inwards. If it's too small (< 0), I move `j` inwards.

    4. The tricky part (When sum == 0): 
       The hard thing to remember is what to do when we actually find a match. We add 
       it to our results, but then we want to move BOTH pointers. 
       - Why? We definitely want to move `j` inwards to find new combinations. But if 
         we move to a completely new `j`, the total sum changes. That means whatever 
         our current `k` is will NEVER be the right `k` to make the sum work again. 
         Since that `k` is now completely useless to us, we can safely move it inwards 
         too (`k -= 1`).

    5. The final clean-up: 
       After moving `j` on a match, I have a quick `while` loop that ensures `j` actually 
       moved to a brand new number and didn't just step onto a duplicate of itself.
    """

    def threeSumTry3(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # 1. Early exit if 'a' is positive
            if a > 0:
                break
            
            # 2. Skip duplicate starting numbers
            if i > 0 and a == nums[i - 1]:
                continue
            
            # 3. Setup sliding window
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                threesum = a + nums[j] + nums[k]
                
                if threesum > 0:
                    k -= 1
                elif threesum < 0:
                    j += 1
                else:
                    # 4. Match found! Move both pointers.
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    # 5. Ensure the new 'j' isn't a duplicate
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                        
        return res
