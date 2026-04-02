# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # Node found
        if root.val == key:
            # Handle 0 children and 1 child cases
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Handle 2 children case
            else:
                # Find the max on the left subtree
                root.val = self.find_the_max(root.left)
                # Delete that max node from the left subtree AND reassign the pointer
                root.left = self.deleteNode(root.left, root.val)
                return root

        # Search right subtree AND reassign pointer
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # Search left subtree AND reassign pointer
        else:
            root.left = self.deleteNode(root.left, key)
            return root
        
    def find_the_max(self, root):
        if root.right is None:
            return root.val
        else:
            return self.find_the_max(root.right)