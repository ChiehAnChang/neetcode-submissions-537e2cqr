# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def _goodNode(root, cur_max):
            if not root:
                return 0
            else:
                cur_max = max(root.val, cur_max)
                child_good_node_left = _goodNode(root.left, cur_max)
                child_good_node_right = _goodNode(root.right, cur_max)
                if not(cur_max > root.val):
                    return 1 + child_good_node_left + child_good_node_right
                else:
                    return child_good_node_left + child_good_node_right
        return _goodNode(root, root.val)