# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        --- UNDERSTANDING THE MEMORY MECHANICS ---
        
        1. Splitting the List (Variables vs. Objects):
           When we do `halfstart = slow.next`, `halfstart` points to the physical 
           box location after `slow`. It does NOT mean `halfstart` becomes None 
           when we run `slow.next = None`. We are just cutting the connection 
           from the previous box (`slow`), but whatever physical box was at 
           `slow.next` is still safely in memory with `halfstart` attached to it.
           
        2. The Golden Rule of Pointers (No dots vs. Dots):
           - Assigning variables (no dots, e.g., `temp1 = first.next`): You are 
             looking at the physical box that `first.next` is pointing to, and 
             copying that box's location over to `temp1`. You are NOT linking 
             `temp1` to the `first` variable itself.
           - Cutting strings (with dots, e.g., `first.next = second`): You are 
             changing the actual string/pointer attached to `first`. This does 
             NOT affect `temp1`, because `temp1` is safely attached to the physical 
             box that was there before you cut the string.
        """

        # 1. Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Split the list into two distinct halves
        halfstart = slow.next 
        slow.next = None 
        
        # 3. Reverse the second half 
        curr = halfstart
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 4. Merge the two halves alternatingly
        first, second = head, prev
        while second:
            # Save the upcoming nodes before we overwrite the current pointers
            temp1, temp2 = first.next, second.next

            # Change the pointers (cut the strings and re-tie them)
            first.next = second
            second.next = temp1
            
            # Move our pointer variables forward down the list
            first = temp1
            second = temp2
