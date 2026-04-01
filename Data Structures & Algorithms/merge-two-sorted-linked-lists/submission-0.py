# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        curr_1 = list1
        curr_2 = list2
        
        placeholder = ListNode(val = None, next = None)
        
        res = placeholder

        while curr_1 is not None and curr_2 is not None:
            if curr_1.val >= curr_2.val:
                res.next, curr_2 = curr_2, curr_2.next
            else:
                res.next, curr_1 = curr_1, curr_1.next
            res = res.next

        if curr_1 is None:
            res.next = curr_2
        else:
            res.next = curr_1
        return placeholder.next