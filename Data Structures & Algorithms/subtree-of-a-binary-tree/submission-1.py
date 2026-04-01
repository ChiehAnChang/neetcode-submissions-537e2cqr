class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, it can't contain a subRoot (unless subRoot is also None)
        if not root: 
            return False
        
        # 1. Check if the trees are identical starting here
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. BUG FIX: Recursively call isSubtree (not isSameTree) 
        # to search deeper levels of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val: # Changed .value to .val
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)