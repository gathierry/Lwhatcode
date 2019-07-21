/*
Given a binary search tree and a range [k1, k2], return all elements in the given range.

Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
*/
/*
二叉搜索树的中序遍历是递增的
*/

#include <iostream>
#include <vector>

using namespace std;

class TreeNode {
	public:
		int val;
		TreeNode *left, *right;
		TreeNode(int val) {
			this->val = val;
			this->left = this->right = NULL;
		}
};


class Solution {
public:
    /**
     * @param root: param root: The root of the binary search tree
     * @param k1: An integer
     * @param k2: An integer
     * @return: return: Return all keys that k1<=key<=k2 in ascending order
     */
    vector<int> searchRange(TreeNode *root, int k1, int k2) {
        // write your code here
		vector<int> lst;
		if (root) {
		    inOrder(root, lst, k1, k2);
		}
		return lst;
    }
	
	void inOrder(TreeNode *root, vector<int> &lst, int k1, int k2) {
	    if (root->left) {
		    inOrder(root->left, lst, k1, k2);
	    }
		if (root->val >= k1 && root->val <= k2) {
			lst.push_back(root->val);
		}
		if (root->right) {
		    inOrder(root->right, lst, k1, k2);
		}
	}
};