<!-- Tag: 动态规划 -->

### 礼物的最大价值

**题目描述**

```tex
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？


示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
```

**C++**

超时了了了了了

```c++
class Solution {
public:
    // 每个格子都可能从上或者左边来
    int maxValue(vector<vector<int>>& grid) {
        if(!grid.size() || !grid[0].size()) return 0;
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        dp[0][0] = grid[0][0];
        dfs(grid, 0, 0, dp);
        return dp[m - 1][n - 1];
    }

    void dfs(vector<vector<int>>& grid, int x, int y, vector<vector<int>>& dp) {
        int dx[2] = {0, 1}, dy[2] = {1, 0};
        for(int i = 0; i < 2; i++) {
            int a = x + dx[i], b = y + dy[i];
            if(a >= 0 && a < grid.size() && b >= 0 && b < grid[0].size()) {
                dp[a][b] = max(grid[a][b] + dp[x][y], dp[a][b]);
                if(dp[a][b] == grid[a][b] + dp[x][y]) dfs(grid, a, b, dp);  // 剪枝
            }
        }
    }
};
```

换一个真dp

```c++
class Solution {
public:
    // 每个格子都可能从上或者左边来
    int maxValue(vector<vector<int>>& grid) {
        if(!grid.size() || !grid[0].size()) return 0;
        int m = grid.size(), n = grid[0].size();

        for(int i = 1; i < m; i++) grid[i][0] = grid[i-1][0] + grid[i][0];
        for(int i = 1; i < n; i++) grid[0][i] = grid[0][i-1] + grid[0][i];

        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                grid[i][j] = grid[i][j] + max(grid[i-1][j], grid[i][j-1]);
            }
        }

        return grid[m-1][n-1];
    }
};
```

