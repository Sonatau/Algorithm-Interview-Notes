<!-- Tag: 二叉树 -->

### 节点与其祖先之间的最大差值

**题目描述**

```tex
给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。

（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

输入：root = [8,3,10,1,6,null,14,null,null,4,7,13]
输出：7
  解释： 
  我们有大量的节点与其祖先的差值，其中一些如下：
  |8 - 3| = 5
  |3 - 7| = 4
  |8 - 1| = 7
  |10 - 13| = 3
  在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。

提示：

  树中的节点数在 2 到 5000 之间。
  0 <= Node.val <= 105
```

**C++**

辣鸡的力量！

```c++
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
public:
    int maxn = 0;
    int maxAncestorDiff(TreeNode* root) {
        dfs(root);
        return maxn;
    }

    vector<int> dfs(TreeNode* root) {
        if(!root) return {};
        vector<int> left = dfs(root->left);
        vector<int> right = dfs(root->right);
        // 左子树为空 返回节点与右子树的比较结果
        if(!left.size() && !right.size()) return {root->val, root->val};
        else if(!left.size()) {
            maxn = max(max(abs(root->val - right[0]), abs(root->val - right[1])), maxn);
            return {min(root->val, right[0]), max(root->val, right[1])};
        } else if(!right.size()) {
            maxn = max(max(abs(root->val - left[0]), abs(root->val - left[1])), maxn);
            return {min(root->val, left[0]), max(root->val, left[1])};
        } else {
            int maxn2 = max(max(abs(root->val - left[0]), abs(root->val - left[1])), maxn);
            int maxn1 = max(max(abs(root->val - right[0]), abs(root->val - right[1])), maxn);
            maxn = max(maxn1, maxn2);
            int min_1 = min(min(left[0], right[0]), root->val), max_2 = max(max(left[1], right[1]), root->val);
            return {min_1, max_2};
        }
    }
};
```

实际上的递归解法，对一个节点来说所谓最大差值，就是**祖先的最大值或者最小值和自己的val的差值**。
因此只需要知道所有祖先可能的最大值和最小值，在遍历时携带传递即可。

```c++
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        dfs(root, root->val, root->val);
        return result;
    }

private:
    int result = 0;
    void dfs(TreeNode* node, int up, int low) {
        if (node == nullptr) {
            return;
        }
        result = max(max(abs(node->val - up), abs(node->val - low)), result);
        up = max(node->val, up);
        low = min(node->val, low);
        dfs(node->left, up, low);
        dfs(node->right, up, low);
    }
};
```

