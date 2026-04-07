class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_res = root.val
        
        def dfs(node):
            # 1. Declare nonlocal so we can modify the outer variable
            nonlocal global_res 
            
            if not node:
                return 0
            
            # 2. Fix the parenthesis typo here
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            
            global_res = max(global_res, node.val + leftMax + rightMax)
            
            return node.val + max(leftMax, rightMax)
            
        # 3. Actually call the function
        dfs(root) 
        
        return global_res