<!-- Tag: 深度优先搜索 -->

### 矩阵中的路径

**题目描述**

```tex
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
 

提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成

```

**C++**

```c++
class Solution {
public:
    int movingCount(int m, int n, int k) {
        if(k == 0) return 1;
        vector<vector<int>> visit(m, vector<int>(n, -1));
        return dfs(0, 0, m, n, k, visit);
    }
    
    int dfs(int i, int j, int m, int n, int k, vector<vector<int>> &visit) {
         if (i < 0 || i >= m || j < 0 || j >= n || (i/10 + i%10 + j/10 + j%10) > k || visit[i][j] != -1) {
            return 0;
        }
        visit[i][j] = 1;
        return dfs(i + 1, j, m, n, k, visit) + dfs(i - 1, j, m, n, k, visit) + dfs(i, j + 1, m, n, k, visit) + dfs(i, j - 1, m, n, k, visit) + 1;
    }
};
```