class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // An empty tree is already inverted.
        if (root == nullptr) {
            return nullptr;
        }

        // Swap the left and right child pointers.
        swap(root->left, root->right);

        // Invert both subtrees.
        invertTree(root->left);
        invertTree(root->right);

        return root;
    }
};