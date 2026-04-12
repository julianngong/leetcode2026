# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

"""
HOW THIS ALGORITHM WORKS:

1. WHY A HEAP:
Using a heap makes this question actually very easy. Remember, a min-heap gives you the 
smallest element of a collection very quickly. This wasn't needed when we only merged 
2 lists (because we could just compare the two heads directly). But when merging multiple 
lists and constantly having to find the minimum of multiple items, always think about 
using a heap!

2. THE WRAPPER CLASS:
Ideally, we would just pass the nodes directly into the heap. However, Python doesn't know 
how to handle comparing two ListNode objects by default. To get around this, we create a 
NodeWrapper object. It is initialized with a node, and defines a magic method `def __lt__(self, other):`. 
This tells Python how to compare a wrapper against an 'other' wrapper to see which is less. 
We define "less" by looking at which underlying node value (`self.node.val < other.node.val`) is smaller.

3. EARLY EXIT:
We make a quick early exit: if the input array of lists is entirely empty, we just return None.

4. THE DUMMY (FAKE) NODE:
Because we are building a new list, we don't know which node will be the absolute first. 
To avoid writing messy `if/else` logic just to handle the very first node, we do the "blank 
node" trick (`res = ListNode()`). This gives us a safe starting pointer. We set `curr = res`. 
As we attach things to `curr.next` and move `curr` down the line, `res` stays safely at the 
very beginning. At the end, we just return `res.next` to skip the fake dummy node.

5. INITIALIZING THE HEAP:
We define `minHeap` as an empty list. Since each of the K input lists is already sorted, 
we iterate through them and push the *head* (the very first node) of each list into the 
heap, making sure to wrap it in our NodeWrapper.

6. THE LOOP & ADVANCING:
We repeat this process until the heap is empty: we pop the wrapper from the heap, which 
gives us the absolute smallest node currently available across all lists. We set `curr.next` 
to this popped node, and then move `curr` down to point to this new addition.

7. REPLENISHING THE HEAP:
Finally, if the node we just added to our merged list has a connecting `next` node in its 
original list, that `next` node is now the new "front" of that specific list. Therefore, 
it must be added to the heap to compete against the fronts of the other lists.

---
ADDITIONAL TIPS TO LOOK OUT FOR:
* Time Complexity: O(N log K), where N is the total number of nodes across all lists, and 
  K is the number of linked lists. Finding the minimum takes O(log K) time.
* Space Complexity: O(K) because the heap never holds more than K elements at a single time 
  (just the front of each list).
* Magic Methods: `__lt__` stands for "less than". By defining it, you are officially operator 
  overloading the `<` symbol for your custom class in Python.
"""

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class SortableNode:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val
    
    def __gt__(self, other):
        return self.node.val > other.node.val

class Solution:    
    def mergeKListsHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Early exit for empty list
        if len(lists) == 0:
            return None
        
        # Create dummy node to easily build the new list
        res = ListNode()
        curr = res
        minHeap = []
        
        # Populate the heap with the head of each linked list
        for l in lists:
            if l is not None:
                heapq.heappush(minHeap, NodeWrapper(l))
        
        # Continuously pop the smallest and push the next available node
        while minHeap:
            node_wrapper = heapq.heappop(minHeap)
            curr.next = node_wrapper.node
            curr = curr.next

            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))
                
        # Return the head of the new list, skipping the dummy node
        return res.next

    """
    HOW THIS ALGORITHM WORKS:

    1. THE DIVIDE AND CONQUER STRATEGY:
    In this solution, we use the "Divide and Conquer" idea. We sequentially go through our 
    array of linked lists and pair them up (List 0 with List 1, List 2 with List 3, etc.). 
    We merge each pair together to create a new, smaller array of longer lists. We repeat 
    this entire pairing and merging process until there is only exactly 1 list left, which 
    we then return.

    2. THE HELPER FUNCTION:
    To execute this, we rely heavily on the standard "Merge Two Sorted Lists" algorithm, 
    which we define as a helper function (`mergeList`). This function takes two individual 
    linked lists and weaves them together in sorted order.

    3. HANDLING AN ODD NUMBER OF LISTS:
    When grouping our lists into pairs (l1 and l2), there is a high chance we will have an 
    odd number of lists at some point. If we try to grab `l2` and the index is out of bounds, 
    we simply set `l2` to `None`. Our helper function handles this perfectly: merging a valid 
    list with `None` just immediately returns the valid list without breaking anything.

    ---
    ADDITIONAL TIPS & COMPLEXITY TO LOOK OUT FOR:

    * Time Complexity: O(N log K)
    - N is the total number of nodes across ALL lists.
    - K is the number of linked lists.
    - Why? In a single pass of pairing up all lists, you touch every single node once 
        (O(N) work). Because you are halving the number of lists in each pass (from 8 to 4 
        to 2 to 1), you only have to do this full pass log(K) times. 

    * Space Complexity: O(K)
    - Your `mergedLists` temporary array stores the new heads of the merged lists. In the 
        first pass, it stores K/2 items. So, the extra memory scales with the number of lists.

    * The Step Function Trick: 
    - Using `range(0, len(lists), 2)` is the secret sauce here. The `, 2` at the end makes 
        the loop jump by 2 steps at a time. This guarantees that `i` is always the left item 
        of a pair, and `i + 1` is always the right item, preventing you from merging the same 
        lists twice.

    * Inline If/Else (Ternary Operator): 
    - `lists[i+1] if (i+1) < len(lists) else None` is a very Pythonic way to handle the 
        IndexError. It reads exactly like English and saves you from having to write a 4-line 
        if/else block just to assign a variable.
    """

    def mergeKListsDivideAndConquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Early exit for empty input
        if not lists or len(lists) == 0:
            return None
        
        # Keep merging pairs of lists until only 1 giant list remains
        while len(lists) > 1:
            mergedLists = [] # Temp array to hold the results of this current pass
            
            # Jump by 2 every iteration to grab pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Safely grab the second list, or set to None if we have an odd number
                l2 = lists[i+1] if (i+1) < len(lists) else None
                
                # Merge the pair and add the result to our temp array
                mergedLists.append(self.mergeList(l1, l2))
                
            # Overwrite the original lists array with our newly merged halved array
            lists = mergedLists
            
        # Return the final remaining merged list
        return lists[0]
    
    def mergeList(self, l1, l2):
        # Standard "Merge Two Sorted Lists" implementation
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        # Attach whatever is left over from either list
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
            
        return dummy.next  

    def mergeKListsHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, SortableNode(node))
        curr = dummy
        while heap:
            smallest = heapq.heappop(heap)
            curr.next = smallest.node
            curr = curr.next
            if smallest.node.next:
                heapq.heappush(heap, SortableNode(smallest.node.next))
        return dummy.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            newlist = []
            for i in range(len(lists)//2):
                front = dummy = ListNode()
                l1, l2 = lists[i*2], lists[i*2 + 1]
                while l1 and l2:
                    if l1.val < l2.val:
                        dummy.next = l1
                        l1 = l1.next
                    else:
                        dummy.next = l2
                        l2 = l2.next
                    dummy = dummy.next
                if l1:
                    dummy.next = l1
                if l2:
                    dummy.next = l2
                newlist.append(front.next)
            if len(lists) % 2 != 0:
                newlist.append(lists[-1])
            lists = newlist
        return lists[0]
  
