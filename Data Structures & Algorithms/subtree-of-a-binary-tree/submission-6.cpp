/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode* left;
 *     TreeNode* right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(
 *         int x,
 *         TreeNode* left,
 *         TreeNode* right
 *     ) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Both nodes are empty.
        if (p == nullptr && q == nullptr) {
            return true;
        }

        // Only one node is empty.
        if (p == nullptr || q == nullptr) {
            return false;
        }

        return p->val == q->val &&
               isSameTree(p->left, q->left) &&
               isSameTree(p->right, q->right);
    }

public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // An empty subtree is considered a subtree.
        if (subRoot == nullptr) {
            return true;
        }

        // A non-empty subtree cannot exist inside an empty tree.
        if (root == nullptr) {
            return false;
        }

        // Check whether the subtree begins at the current node.
        if (isSameTree(root, subRoot)) {
            return true;
        }

        // Otherwise, search both child subtrees.
        return isSubtree(root->left, subRoot) ||
               isSubtree(root->right, subRoot);
    }
};