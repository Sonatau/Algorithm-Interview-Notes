<!-- Tag: 二叉树 -->

### 二叉搜索树的第k大节点

**题目描述**

```tex
给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

```

**C++**

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
    vector<int> ans;
    int kthLargest(TreeNode* root, int &k) {
        if (!root) return 0;
        int result = kthLargest(root->right, k);  // 右侧有多少个节点
        --k;
        if (!k) return root->val;
        return k < 0 ? result : kthLargest(root->left, k);  // 左
    }
};
```

或者下面这个比较容易懂，重新写的：

```c++
class Solution {
public:
    int count = 0, ans = 0;
    int kthLargest(TreeNode* root, int k) {
        zhongxu(root, k);
        return ans;
    }

    int zhongxu(TreeNode* root, int k) {
        if(root->right) zhongxu(root->right, k);
        if(k == ++count) ans = root->val;
        if(root->left) zhongxu(root->left, k);
        return 0;
    }
};
```

