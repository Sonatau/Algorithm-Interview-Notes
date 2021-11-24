<!-- Tag: 动态规划 -->

### 最大子矩阵

**题目描述**

```tex
给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。

返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

示例：

输入：
[
   [-1,0],
   [0,-1]
]
输出：[0,1,0,1]
解释：输入中标粗的元素即为输出所表示的矩阵

说明：

	1 <= matrix.length, matrix[0].length <= 200

```

**C++**

（华为 and 猿辅导 

最大子数组的二维升级版。技术点：`前缀和+最大子数组`

下面是思路：

- i,j双指针遍历所有可能的的两个“行对”，即子矩阵的上下两条边，这决定了矩阵的高
- 将i-j之间的每一列（求出每一列的累计的和）看成一维数组中的一项，在其中求最大子数组，即求出符合的子矩阵的宽

祝你好运！

```c++
class Solution {
public:
    vector<int> getMaxMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int best = matrix[0][0];
        vector<int> res(4, 0);

        // 列的前缀和
        int dp[m + 1][n + 1];
        for(int i = 1; i < m + 1; i++) {
            for(int j = 0; j < n; j++) dp[i][j] = dp[i-1][j] + matrix[i-1][j];
        }

        for(int i = 0; i < m; i++) {
            for(int j = i; j < m; j++) {
                // 对于某一列而言 行之间的差值
                int cur[n];
                for(int k = 0; k < n; k++) cur[k] = dp[j + 1][k] - dp[i][k];

                int start = 0;
                int sum = cur[0];
                for(int k = 1; k < n; k++) {
                    if(sum > 0) sum += cur[k];
                    else {
                        sum = cur[k];
                        start = k;
                    }
                    if(sum > best) {
                        best = sum;
                        res = {i, start, j, k};
                    }
                }
            }
        }

        return res;
    }
};
```