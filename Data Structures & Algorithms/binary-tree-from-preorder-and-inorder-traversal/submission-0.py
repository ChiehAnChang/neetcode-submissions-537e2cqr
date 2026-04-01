# class TreeNode:
#      def __init__(self, val=0, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        else:

            root_val = preorder[0]
            root = TreeNode(root_val)
            index_root = inorder.index(root_val) 
            left_length = index_root

            # This is the O(N^2) "logic bug" due to repeated slicing/copying
            left_pre = preorder[1: 1+index_root]
            right_pre = preorder[1+index_root:]

            left_subtree = self.buildTree(left_pre, inorder[:left_length])
            right_subtree = self.buildTree(right_pre, inorder[left_length + 1:])

            root.left, root.right =left_subtree,  right_subtree
            return root