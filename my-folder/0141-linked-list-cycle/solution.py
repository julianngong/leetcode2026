# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# easy and done first time. note that you can add actual nodes to a set. its not only about if the value is the same but if the actual node is the same. it can be a complete different node but with the same value which is not a cycle. also note, try to duplicate the head variable so that if you ever need you can get back to the start of the list with a variable.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head != None:
            if head in seen:
                return True
            else:
                seen.add(head)
                head = head.next
        return False
        
