/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    vector<int> bstList (TreeNode * root){
        vector <int> res;
        if (root == nullptr){
            return res;
        }

        vector<int> left = bstList(root -> left);
        vector<int> right = bstList(root -> right);

        for (const int each_n : left){
            res.push_back(each_n);
        }
        
        res.push_back(root->val);

        for (const int each_n : right){
            res.push_back(each_n);
        }

        return  res;
    }
public:
    int kthSmallest(TreeNode* root, int k) {


        
        vector <int> lstBst = bstList(root);

        return lstBst[k-1];
    }
};
