# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = node = ListNode(0);
        while ((l1.next != None) or (l2.next != None)):
            temp = l1.val + l2.val + carry
            carry = 0
            if (temp > 9):
                temp = temp - 10
                carry = carry + 1
            if (l1.next == None):
                l1.val = 0
            else: 
                l1 = l1.next
            if (l2.next == None):
                l2.val = 0
            else:
                l2 = l2.next
            node.next = ListNode(temp)
            node = node.next
        temp = l1.val + l2.val + carry
        if (temp > 9):
                temp = temp - 10
                node.next = ListNode(temp)
                node = node.next
                node.next = ListNode(1)
        else:
            node.next = ListNode(temp)
        return(root.next)
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
