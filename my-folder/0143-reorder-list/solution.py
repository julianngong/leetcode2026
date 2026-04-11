# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderListFirstAttempt(self, head: Optional[ListNode]) -> None:
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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        --- CRITICAL NOTE FOR NEXT TIME ---
        
        1. THE "SEVERING" REQUIREMENT (The Missing slow.next = None):
           If you don't detach the first half from the second half, you create 
           a 'Cycle' or Infinite Loop. 
           
           THE ISSUE: When you reverse the second half, those nodes now point 
           backwards. If the tail of your first half still points to the 
           original start of the second half, the merge phase will eventually 
           link a node to a previous node in the sequence, creating a circle 
           that the computer will follow forever until the memory or time 
           limit expires.
           
        2. DITCHING THE DUMMY:
           You don't actually need a dummy node to find the middle. Using 
           'slow, fast = head, head.next' is more efficient. 
           
        3. WHY IT WORKS FOR SINGLE NODES (N=1):
           If the list has only one node, 'fast' (head.next) is None. The 
           'while fast and fast.next' loop never runs. 'halfstart' becomes 
           None, 'slow.next' remains None, and the merge loop 'while second' 
           never starts. The code stays robust without extra 'if' checks.
        """
        if not head or not head.next:
            return

        # 1. Find the middle (No dummy needed)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. SEVER THE CONNECTION
        # This is the "string cutting" that prevents the infinite loop.
        curr = slow.next
        slow.next = None 
        
        # 3. Reverse the second half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 4. Merge the two halves
        curr1, curr2 = head, prev
        while curr2: # curr2 is always shorter or equal to curr1
            temp1, temp2 = curr1.next, curr2.next
            
            curr1.next = curr2
            curr2.next = temp1
            
            curr1 = temp1
            curr2 = temp2
