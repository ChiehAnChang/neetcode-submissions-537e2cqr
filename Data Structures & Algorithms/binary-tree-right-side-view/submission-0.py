# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            q = deque([(root, 0)])        
            res = []
            while q:
                new_node, level = q.popleft()
                left_component = new_node.left, level + 1
                right_component = new_node.right, level + 1

                if left_component[0]:
                    q.append(left_component)

                if right_component[0]:
                    q.append(right_component)

                if len(res) != level + 1:
                    res.append([new_node.val])
                else:
                    res[level].append(new_node.val)
            return res
        
        res = levelOrder(root)
        return [each_level_cont[-1] for each_level_cont in res]