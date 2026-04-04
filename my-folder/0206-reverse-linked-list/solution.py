# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # must think for reversing linked list we need 3 things, the previous thing so we can reverse 
    # and point to it, the current one so we can assign to the previous and the next one which is 
    # basically the temporary to store the old next one before we reassign the current to the previous. 
    # we want to set previous at first to none as nothings there but we want this first term to 
    # eventually point to none as it will then be at the back and set the current to be the head. 
    # we repeat this until current is none and then once its none we return whats stored in the previous
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    '''
    this is a lot harder. basically think the end case is that we have a null or the next thing 
    after is a null so we go down until theres nothing at all or theres only 1 node. at this point 
    we return that node. now watch what we do with it. when returned its called newHead and we 
    never change it. thats because this is the end node and we want to keep this just in memory 
    so that we can use it as our result as we only end up passing a single head node and as this 
    is the last thing this is the new head node so must use this as the final return. 
    
    note these are all pointers so as we do head.next.next = head we are replacing the list. 
    this is saying take the current thing and the one to the next of it, point it to the current 
    head aka flipping it. we then clean up the forward pointer (head.next = None) and return newHead 
    again and as we are recursively going up this head keeps becoming the previous head of the 
    previous iteration so we are making sure all these point to the right thing backwards. 
    
    Now, as for where newHead actually gets linked to everything else since we never explicitly use it:
    Think about the very first time we step back up. If our list was 1 -> 2 -> 3, we just hit the 
    base case at node 3, so newHead = node 3. We are currently unpaused at head = node 2. 
    Look at the physical pointers right now: what is head.next? It's node 3! 
    
    Because newHead and head.next are looking at the exact same physical node in the computer's memory, 
    when we write `head.next.next = head`, we literally ARE linking newHead! We are reaching into 
    node 3 (by calling it head.next) and telling it to point back to node 2. We don't type the word 
    'newHead' to do this, but because they are the same object, the link is made. We have to use 
    `head.next.next` instead of `newHead.next` because as we keep walking up the list, we need to link 
    node 2 to node 1. If we used `newHead.next`, we would just be changing node 3's pointer over and 
    over again and leaving the rest of the list broken.
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead
