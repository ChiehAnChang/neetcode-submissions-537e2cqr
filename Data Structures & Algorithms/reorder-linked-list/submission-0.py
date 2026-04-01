# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. Count nodes (This part was correct)
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next

        # 2. Split list (Logic correct, but fixed the reverse call)
        reverse_start = head
        reverse_conut = 0
        prev = None
        while reverse_conut != ((count - 1) // 2 + 1):
            prev = reverse_start 
            reverse_conut += 1
            reverse_start = reverse_start.next
            
        prev.next = None

        # BUG FIX 1: Pass 'reverse_start' (the 2nd half), NOT 'head'
        reverse_start = self.reverse(reverse_start)

        # We don't need to return anything, just modify in place
        self.merge(head, reverse_start)

    def reverse(self, head):
        curr = head
        prev = None

        while curr is not None:
            temp = curr.next
            curr.next = prev
            
            # BUG FIX 2: Correctly advance pointers
            prev = curr  # Move prev to current
            curr = temp  # Move curr to next (temp)

        return prev

    def merge(self, head1, head2):
        curr_1 = head1
        curr_2 = head2

        placeholder = ListNode(0, None)
        res = placeholder

        while curr_1 is not None and curr_2 is not None:
            # BUG FIX 3: Save the next pointers BEFORE changing links
            temp_1 = curr_1.next
            temp_2 = curr_2.next

            res.next = curr_1
            res = res.next
            
            res.next = curr_2
            res = res.next

            # Restore pointers from temp variables
            curr_1 = temp_1
            curr_2 = temp_2

        if curr_1 is not None:
            res.next = curr_1
        
        return placeholder.next