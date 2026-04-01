from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(node, low=float("-inf"), high=float("inf")):
            if not node:
                return True
            
            # Use <= or >= here if your specific BST definition allows duplicates
            if not (low < node.val < high):
                return False
            
            # Recurse: 
            # Left side must be less than current val
            # Right side must be greater than current val
            return (checkBST(node.left, low, node.val) and 
                    checkBST(node.right, node.val, high))

        return checkBST(root)