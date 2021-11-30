<!-- Tag: 数组 -->

### 二维数组中的查找

**题目描述**

```tex
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：
  [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
  ]
  给定 target = 5，返回 true。

  给定 target = 20，返回 false。

限制：
  0 <= n <= 1000
  0 <= m <= 1000
```

**C++**

摁算... 像个傻叉

```c++
class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        if(!matrix.size() || !matrix[0].size()) return false;
        int n = matrix.size() - 1, m = matrix[0].size() - 1;
        while(n >= 0 && m >= 0 && matrix[n][m] >= target) {
            if(matrix[n][m] == target) return true;
            int left = matrix[n][0], top = matrix[0][m];
            if(left <= target) {
                for(int i = 0; i < m; i++) if(matrix[n][i] == target) return true;
            }
            if(top <= target) {
                for(int i = 0; i < n; i++) if(matrix[i][m] == target) return true;
            }
            n--; m--;
        }
        return false; 
    }
};
```

**官方解释**：从右上角看，这个矩阵其实就是一个二叉查找树

```c++
class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {         
         int n = matrix.size();
         //特殊情况，二位数组为空
         if(n == 0){
             return false;
         }
         int m = matrix[0].size();
         
         int i = 0;
         int j=m-1;
         while(i<n && j>=0 ){
            if(target == matrix[i][j]){
                return true;
            }
            else if(matrix[i][j] > target ){
                j--;
            }
            else{
                i++;
            }
         }
         return false;
    }
};
```

