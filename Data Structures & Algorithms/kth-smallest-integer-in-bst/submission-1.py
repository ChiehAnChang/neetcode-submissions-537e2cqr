# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        lst = self.printPreOrder(root)
        return lst[k - 1]


    def printPreOrder(self, root):
        if not root:
            return []
        else:
            left, right = self.printPreOrder(root.left), self.printPreOrder(root.right)
            return left + [root.val] + right
        