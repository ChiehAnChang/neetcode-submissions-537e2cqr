/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right)
 *         : val(x), left(left), right(right) {}
 * };
 */

class Solution {

private:

    int numBig(TreeNode* root, int num) {
        if (root == nullptr) {
            return 0;
        }

        int res;

        if (root->val >= num) {
            res = 1
                + numBig(root->left, root->val)
                + numBig(root->right, root->val);
        } else {
            res = numBig(root->left, num)
                + numBig(root->right, num);
        }

        return res;
    }

public:

    int goodNodes(TreeNode* root) {
        return numBig(root, INT_MIN);
    }
};