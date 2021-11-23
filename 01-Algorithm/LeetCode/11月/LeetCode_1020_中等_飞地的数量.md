<!-- Tag: 深度优先搜索 -->

### 飞地的数量

**题目描述**

```tex
给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。

移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。

返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。

示例 1：

  输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
  输出：3
  解释： 
  有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

示例 2：

  输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
  输出：0
  解释：
  所有 1 都在边界上或可以到达边界。

提示：

  1 <= A.length <= 500
  1 <= A[i].length <= 500
  0 <= A[i][j] <= 1
  所有行的大小都相同

```

**C++**
1. 从边界遍历
```c++
class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {
        // 上下两行
        for(int j = 0; j < grid[0].size(); j++) {
            if(grid[0][j] == 1) dfs(0, j, grid);
            if(grid[grid.size() - 1][j] == 1) dfs(grid.size() - 1, j, grid);
        }
        // 左右两列
        for(int j = 0; j < grid.size(); j++) {
            if(grid[j][0] == 1) dfs(j, 0, grid);
            if(grid[j][grid[0].size() - 1] == 1) dfs(j, grid[0].size() - 1, grid);
        }
        int sum = 0;
        for(int i = 0; i < grid.size(); i++) {
            sum += accumulate(grid[i].begin(), grid[i].end(), 0);
        }
        return sum;
    }

    void dfs(int x, int y, vector<vector<int>>& grid) {
        grid[x][y] = 0;
        int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
        for(int i = 0; i < 4; i++) {
            int a = dx[i] + x, b = dy[i] + y; // 下一个位置的坐标
            if(a >= 0 && a < grid.size() && b >= 0 && b < grid[0].size() && grid[a][b] == 1) dfs(a, b, grid);
        }
    }
};
```