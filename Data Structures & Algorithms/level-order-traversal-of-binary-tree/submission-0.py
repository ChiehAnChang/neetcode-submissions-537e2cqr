# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        # Store (node, level_index)
        q.append((root, 0))
        
        res = []
        
        while q: # Pythonic way to check not empty
            new_node, level = q.popleft()
            
            # 3. FIX: Append .val, not the node object
            if len(res) == level:
                res.append([new_node.val])
            else:
                res[level].append(new_node.val)

            # 1. FIX: Use new_node, not root
            # 2. FIX: Check if children exist before appending
            if new_node.left:
                q.append((new_node.left, level + 1))
            if new_node.right:
                q.append((new_node.right, level + 1))

        return res