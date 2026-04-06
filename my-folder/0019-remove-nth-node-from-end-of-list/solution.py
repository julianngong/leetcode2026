# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEndFirstTry(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenlist = 0
        curr = head
        while curr:
            lenlist += 1
            curr = curr.next
        
        curr = head
        prev = None
        for i in range(lenlist - n):
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next
            return head
        else:
            # If prev is None, it means we wanted to remove the very first node, so the loop never ran.
            # We want to pass back head.next to make sure it skips this first node. 
            # If the list only had 1 item to begin with, head.next will correctly just be None anyway.
            return head.next 


    """
    With this code it's nice and smart. The idea is using two pointers to find the Nth from the end:
    1. Start two pointers with a gap of 'n' between them.
    2. Keep going down the list until the right pointer falls off the end.
    3. Because of the exact gap we created, when the right one finishes, the left one is in the perfect position!
    
    BUT note: The left pointer needs to end up one spot BEFORE the node we want to delete, so we can access `prev.next`. 
    If we just increased the gap, it wouldn't work for edge cases (like if there are only 2 elements and n=2). 
    
    So, we make a Dummy Node. We start the left pointer on the Dummy, and the right pointer on the Head. 
    This perfectly offsets our left pointer by 1 behind the real list. It also helps us later: we can just 
    return dummy.next, which allows the first element to be deleted without breaking everything.
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode = ListNode()
        dummynode.next = head
        lp = dummynode
        rp = head
        
        # Create the exact gap of 'n'
        for i in range(n):
            rp = rp.next

        # Slide the window down the list
        while rp:
            lp = lp.next
            rp = rp.next

        # Cut the string to remove the node
        lp.next = lp.next.next
        
        # Note: We MUST return dummynode.next and not head! 
        # There's always a chance the actual `head` node was the one we just deleted. 
        # Rather than adding annoying if/else logic for when the head is deleted, we just rely on the dummy node.
        # dummynode.next will ALWAYS point to the correct start of the list, even if the original head was destroyed.
        return dummynode.next
