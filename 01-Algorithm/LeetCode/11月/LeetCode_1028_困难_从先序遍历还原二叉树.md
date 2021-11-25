<!-- Tag: 二叉树 -->

### 从先序遍历还原二叉树

**题目描述**

```tex
我们从二叉树的根节点 root 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 S，还原树并返回其根节点 root。

输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
```

**C++**

```c++
class Solution {
public:
    TreeNode* helper(string const& S, int& position, int depth){
        if(position == S.size())
            return NULL;
        int tmp = position, cnt = 0, val = 0;
        while(S[tmp] == '-'){
            ++cnt;
            ++tmp;
        }
        if(cnt == depth){
            while(tmp < S.size() && S[tmp] != '-'){
                val = val * 10 + (S[tmp++] - '0');
            }
            TreeNode* root = new TreeNode(val);
            position = tmp;
            root->left = helper(S, position,depth + 1);
            root->right = helper(S, position, depth + 1);
            return root;
        }
        return NULL;
    }
    TreeNode* recoverFromPreorder(string S) {
        int position = 0;
        return helper(S, position, 0);
    }
};
```