<!-- Tag: 数组 -->

### 顺时针打印矩阵

**题目描述**

```tex
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 
示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

```

**C++**

摁算

```c++
class Solution {
public:
    vector<int> ans;
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(!matrix.size() || !matrix[0].size()) return ans;
        int row = matrix.size(), col = matrix[0].size();
        order(matrix, 0, 0, row, col);
        return ans;
    }

    void order(vector<vector<int>>& matrix, int a, int b, int row, int col) {
        if(col <= 0 || row <= 0) return;
        for(int i = b; i < b + col; i++) ans.push_back(matrix[a][i]);
        for(int i = a + 1; i < a + row - 1; i++) ans.push_back(matrix[i][b + col - 1]);
        if (row > 1) for(int i = b + col - 1; i >= b; i--) ans.push_back(matrix[a + row - 1][i]);
        if (col > 1) for(int i = a + row - 2; i >= a + 1; i--) ans.push_back(matrix[i][b]);
        order(matrix, a+1, b+1, row-2, col-2);
    }
};
```