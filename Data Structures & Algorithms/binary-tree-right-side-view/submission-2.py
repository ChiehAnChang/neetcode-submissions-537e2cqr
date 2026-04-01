# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        if not root:
            return []

        q = deque()
        q.append((root, 0))

        prev = (None, -1)
        res = []
        while q:

            node, level = q.popleft()
            if level > prev[1] and prev[1] != -1:
                res.append(prev[0].val)
            prev = (node, level)
            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))

        res.append(prev[0].val)
        return res

