# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or head.next is None:
            return head

        else:

            curr = head
            temp = curr.next

            new_head = self.reverseList(curr.next)

            temp.next = curr

            curr.next = None

            return new_head