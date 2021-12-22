<!-- Tag: 二叉树 -->

### 二叉树的深度

**题目描述**

```tex
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。


提示：

节点总数 <= 10000

```

**C++**

```c++
class Solution {
public:
    // int max_len = 0;
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        int left = 0, right = 0;
        if(root->left) left = maxDepth(root->left);
        if(root->right) right = maxDepth(root->right);

        return 1 + max(left, right);
    }
};
```
