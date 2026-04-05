# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]   # [without_root, with_root]

            left_res = dfs(root.left)
            right_res = dfs(root.right)

            
            without_root = max(left_res) + max(right_res)
            
            with_root = root.val + left_res[0] + right_res[0]

            return [without_root, with_root]

        return max(dfs(root))