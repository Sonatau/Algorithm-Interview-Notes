<!-- Tag: 二叉树 -->

### 对称的二叉树

**题目描述**

```tex
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false

```

**C++**

递归

```c++
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(!root)
            return true;
        return subSym(root->left,root->right);
    }
    bool subSym(TreeNode* A, TreeNode* B){
        if(!A && !B) return true;
        if(!A || !B) return false;
        return A->val == B->val && subSym(A->left,B->right) && subSym(A->right,B->left);
    }
};
```