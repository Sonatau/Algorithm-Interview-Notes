<!-- Tag: 二叉树 -->

### 二叉树中和为某一值的路径

**题目描述**

```tex
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

示例1:
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

示例2:
root = [1,2,3], targetSum = 5
输出：[]

示例 3:
输入：root = [1,2], targetSum = 0
输出：[]
```

**C++**

```c++
class Solution {
public:
    vector<vector<int>> ans;
    vector<vector<int>> pathSum(TreeNode* root, int target) {
        vector<int> cur;
        dfs(root, target, cur);
        return ans;
    }

    // root必须是叶子结点
    void dfs(TreeNode* root, int target, vector<int> &cur) {
        if(!root) return;
        if(target == root->val && !root->left && !root->right) {
            cur.push_back(root->val);
            ans.push_back(cur);
            cur.pop_back();
            return;
        }
        
        cur.push_back(root->val);
        if(root->left) dfs(root->left, target - root->val, cur);
        if(root->right) dfs(root->right, target - root->val, cur);
        cur.pop_back();

        return;
    }
};
```