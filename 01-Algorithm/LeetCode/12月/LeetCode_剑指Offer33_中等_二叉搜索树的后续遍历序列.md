<!-- Tag: 二叉树 -->

### 二叉搜索树的后续遍历序列

**题目描述**

```tex
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
 
示例 1：

输入: [1,6,3,2,5]
输出: false

示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：
数组长度 <= 1000
```

**C++**

```c++
class Solution {
public:
    // 根结点永远在数组的最后
    bool verifyPostorder(vector<int>& postorder) {
        int left = 0, right = postorder.size() - 1;
        return  verify(postorder,left, right);
    }
		// 分治 + 递归
    bool verify(vector<int>& postorder, int left, int right) {
        if(left >= right) return true;
        int mid_n = postorder[right];
        int i = left, tag = 0;
        while(postorder[i] < mid_n) i++;
        tag = i;
        while(postorder[i] > mid_n) i++;
        if(i != right) return false;
        else return verify(postorder, left, tag-1) && verify(postorder, tag, right-1);
    }
};
```