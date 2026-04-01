# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        from collections import deque  # Fixed: lowercase 'd'

        q = deque()
        q.append((-float("inf"), root))

        goodNote = 0

        while q:  

            prev_max, curr = q.popleft()

            if curr.val >= prev_max:  
                goodNote += 1
                prev_max = curr.val

            if curr.left is not None:
                q.append((prev_max, curr.left))

            if curr.right is not None:
                q.append((prev_max, curr.right))

        return goodNote