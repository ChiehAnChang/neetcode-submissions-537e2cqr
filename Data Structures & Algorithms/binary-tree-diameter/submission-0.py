# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This will hold the maximum diameter we find at any node
        self.max_diameter = 0
        
        # Helper function to compute the height of the tree
        def dfs_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # 1. Post-order traversal: calculate height of left and right subtrees
            left_height = dfs_height(node.left)
            right_height = dfs_height(node.right)
            
            # 2. Update the global max diameter if the path through this node is larger
            # (Path length = left_height + right_height)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # 3. Return the height of this node to its parent
            return max(left_height, right_height) + 1
            
        dfs_height(root)
        
        return self.max_diameter