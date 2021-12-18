<!-- Tag: 二叉树 -->

### 从上到下打印二叉树

**题目描述**

```tex
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
返回：

[
  [3],
  [20,9],
  [15,7]
]
```

**C++**

层次遍历

```c++
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> que;
        vector<vector<int>> ans;
        stack<int> st;
        bool reverse = false;

        if(!root) return ans;
        que.push(root);
        while(!que.empty()) {
            vector<int> tmp;
            int len = que.size();
            for(int i = 0; i < len; i++) {
                TreeNode *cur = que.front();
                que.pop();
                if(reverse) st.push(cur->val);
                if(!reverse) tmp.push_back(cur->val);

                if(cur->left) que.push(cur->left);
                if(cur->right) que.push(cur->right);
            }

            while(!st.empty()) {
                tmp.push_back(st.top());
                st.pop();
            }
            reverse = !reverse;
            ans.push_back(tmp);
        }

        return ans;
    }
};
```