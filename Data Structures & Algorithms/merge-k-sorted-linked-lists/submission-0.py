import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        minHeap = []
        
        # 1. Initialize Heap
        # We add 'i' (index) to the tuple to act as a tie-breaker.
        # If values are equal, Python compares 'i' instead of the ListNode object.
        for i, each_ll in enumerate(lists):
            if each_ll:
                heapq.heappush(minHeap, (each_ll.val, i, each_ll))
        
        while minHeap:
            # 2. Fix heappop syntax (pass minHeap) and unpack the index 'i'
            val, i, node = heapq.heappop(minHeap)
            
            # 3. Link the node
            curr.next = node
            # 4. CRITICAL: Move the curr pointer forward!
            curr = curr.next 
            
            if node.next:
                # Push the next node from the same list
                heapq.heappush(minHeap, (node.next.val, i, node.next))
                
        return dummy.next