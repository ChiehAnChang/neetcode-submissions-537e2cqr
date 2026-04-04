# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.left is None and root.right is None and root.val == target:
            return None
        else:
            right = self.removeLeafNodes(root.right, target)
            left = self.removeLeafNodes(root.left, target)
            if right is None and left is None and root.val == target:
                return None
            else:
                root.left, root.right = left, right
                return root