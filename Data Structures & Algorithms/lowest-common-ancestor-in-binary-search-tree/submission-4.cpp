class Solution {
public:
    TreeNode* lowestCommonAncestor(
        TreeNode* root,
        TreeNode* p,
        TreeNode* q
    ) {
        if (root == nullptr) {
            return nullptr;
        }

        // Both target nodes are in the left subtree.
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }

        // Both target nodes are in the right subtree.
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }

        // The nodes are on different sides, or root equals p or q.
        return root;
    }
};