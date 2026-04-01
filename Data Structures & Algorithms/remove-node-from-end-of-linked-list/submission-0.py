# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # check the number of the node in the linked list

        length = 0

        curr = head

        while curr is not None:
            length += 1
            curr = curr.next

        if length - n == 0:
            return head.next

        else:

            curr = head
            prev = None
            count = 0

            while count != (length - n):
                prev, curr = curr, curr.next
                count += 1

            prev.next = curr.next
            curr.next = None
            return head
            