<!-- Tag: 二叉树 -->

### 从上到下打印二叉树

**题目描述**

```tex
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
返回：

[3,9,20,15,7]
```

**C++**

层次遍历

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
    // 层次遍历
    vector<int> levelOrder(TreeNode* root) {
        queue<TreeNode*> que;
        vector<int> ans;
        if(!root) return ans;
        que.push(root);
        while(!que.empty()) {
            int len = que.size();
            for(int i = 0; i < len; i++) {
                TreeNode *cur = que.front();
                que.pop();
                ans.push_back(cur->val);
                if(cur->left) que.push(cur->left);
                if(cur->right) que.push(cur->right);
                
            }
        }

        return ans;
    }
};
```