<!-- Tag: 深度优先搜索 -->

### 机器人的运动范围

**题目描述**

```tex
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3

示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

```

**C++**

```c++
class Solution {
public:
    // 全排列 坐标最多为两位数
    int sum = 0;
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