<!-- Tag: 二叉树 -->

### 重建二叉树

**题目描述**

```tex
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

示例 1:

  Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
  Output: [3,9,20,null,null,15,7]
  
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

限制：
	0 <= 节点个数 <= 5000
```

**C++**

这题还好 比较简单 分治搞一搞

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map<int, int> hp;
    TreeNode *root;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size() == 0) return NULL;
        for(int i = 0; i < inorder.size(); i++) hp[inorder[i]] = i;
        return makeNode(preorder, inorder, 0, preorder.size() - 1, 0);
    }

    TreeNode* makeNode(vector<int>& preorder, vector<int>& inorder, int left, int right, int idx) {
        TreeNode *cur = new TreeNode(preorder[idx]);
        if(left == right) return cur;

        int idx_in = hp[preorder[idx]];
        int left_len = idx_in - left, right_len = right - idx_in; // 左右子树的结点个数
        if(left_len) cur->left = makeNode(preorder, inorder, left, idx_in - 1, idx + 1);
        if(right_len) cur->right = makeNode(preorder, inorder, idx_in + 1, right, idx + left_len + 1);
        return cur;
    }
};
```


