# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return []
            else:
                left, right = dfs(root.left), dfs(root.right)
                return left + [root.val] + right
            
        lst = dfs(root)
        pre = None
        for each_num in lst:
            if pre is None:
                pre = each_num
            else:
                if pre >= each_num:
                    return False
                else:
                    pre = each_num
        return True