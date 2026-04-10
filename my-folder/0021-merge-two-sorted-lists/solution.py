# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    This isn't too hard, just need to solidify the understanding. Rather than writing messy edge-case 
    logic to try and figure out which node should be the absolute start of the newly merged list, we 
    just make a blank "dummy" node to begin populating the rest of the nodes off of. 
    
    The line `dummy = node = ListNode()` makes both `dummy` and `node` point to the exact same empty 
    node in memory. We make two variables because we need to return the front of the linked list at the 
    very end. We can use `node` as our "builder" pointer, changing it and moving it forward, while `dummy` 
    stays firmly planted at the start. At the end, we just return `dummy.next` which holds the real 
    start of the full linked list.
    
    Because they start pointing to the same memory, when we attach our first node to `node.next`, 
    it's also attaching to `dummy.next`. 
    
    So, we keep repeating the loop while both `list1` and `list2` are not None (aka neither has reached 
    the end of its list). We check their values: if list1's value is smaller, we don't need an inner loop 
    to keep looking, we just set `node.next` to list1, and then iterate list1 up so it's pointing to its 
    next bit. We do the exact same for list2 if the inequality goes the other way. 
    
    A cool trick to note here is that even though setting `node.next = list1` technically attaches the 
    ENTIRE rest of list1 to our builder, it's totally fine because the very next time the while loop runs, 
    we will just overwrite that pointer with the next correct smallest node anyway!
    
    After the conditional, we must make sure to move our `node` builder up (`node = node.next`) so that we 
    are standing on the new addition, ready to look for the next one.
    
    The line at the very end just says: once the loop breaks, one list is empty and the other isn't. 
    Since the remaining list is already sorted, just use whatever chunk is remaining and attach it all at once 
    using `list1 or list2`.
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            # Step the builder forward!
            node = node.next
            
        # Attach the leftovers
        node.next = list1 or list2
        
        # Return the actual start of the list, ignoring the blank dummy node
        return dummy.next
        
    def mergeTwoListsTry2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        curr = dummy_node
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy_node.next
