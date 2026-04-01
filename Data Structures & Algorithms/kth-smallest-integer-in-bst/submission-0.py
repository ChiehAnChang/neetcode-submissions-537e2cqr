# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def _print_BST(root):
            if not root:
                return []
            else:
                return _print_BST(root.left) + [root.val] + _print_BST(root.right)

        return _print_BST(root)[k - 1]