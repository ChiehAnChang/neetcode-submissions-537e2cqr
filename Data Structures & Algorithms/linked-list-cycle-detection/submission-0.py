# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        checklist = set()
        curr = head

        while curr is not None:
            if curr in checklist:
                return True
            else:
                checklist.add(curr)
                curr = curr.next
        return False