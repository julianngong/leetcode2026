"""
Notes: Search in Rotated Sorted Array

General Rule of Thumb: If a problem mentions an array is "sorted in ascending order" 
and asks you to find something in O(log n) time, always think Binary Search.

The Strategy: I did this basically myself after watching the video explanation. It's 
labeled as a hard question, but it's really just a case-by-case logic puzzle. The biggest 
takeaway: You don't need to worry about finding the exact pivot point first. Just set 
up standard binary search pointers (l and r) and keep repeating while they haven't crossed. 
When you find the midpoint (mp), all you need to focus on is figuring out which half of 
the array is "normal" (strictly sorted), because due to the rotation, at least one half 
will always be perfectly sorted.

Case 1: The Left Side is Sorted (nums[l] < nums[mp])
If this is true, the pivot point is not in the left half. We check if our target belongs 
in this perfectly sorted left chunk. Because of the rotation, we can't just check if the 
target is less than mp. We also have to check if it's smaller than the very first number 
(nums[l]). If it's smaller than nums[l] OR bigger than nums[mp], it absolutely cannot be 
in the left half, so we shift our search to the right side.

Case 2: The Right Side is Sorted (pivot is in the left)
If the left side isn't sorted, that means the pivot point is in the left half, making 
the right side perfectly sorted. We apply the exact same logic: check if the target 
falls within the bounds of this sorted right chunk. If it does, search right. If not, 
search left.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mp = (r + l) // 2
            if nums[mp] == target:
                return mp
                
            # CASE 1: The Left half is perfectly sorted
            elif nums[l] < nums[mp]:
                if target == nums[l]:
                    return l
                
                # If target is outside the bounds of this sorted left chunk, it must be in the right half.
                elif target < nums[l] or target > nums[mp]:
                    l = mp + 1
                # Otherwise, it's safely inside this left half.
                else:
                    r = mp - 1
                    
            # CASE 2: The Right half is perfectly sorted (pivot is in the left)
            else:
                if target == nums[r]:
                    return r
                
                # If target is outside the bounds of this sorted right chunk, it must be in the left half.
                elif target > nums[r] or target < nums[mp]:
                    r = mp - 1
                # Otherwise, it's safely inside this right half.
                else:
                    l = mp + 1
                    
        return -1
