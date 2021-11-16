<!-- Tag: 动态规划 -->

### 最佳观光组合

**题目描述**

```wiki
给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。
一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。
返回一对观光景点能取得的最高分。

示例 1：
  输入：values = [8,1,5,2,6]
  输出：11
  解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

示例 2：
  输入：values = [1,2]
  输出：2
  
提示：
  2 <= values.length <= 5 * 104
  1 <= values[i] <= 1000
```

**C++**

1. 暴力了一下直接超时:(
2. 使用贪心算法。将问题分解为 A[i] + i 和 A[j] - j，其中 i < j。在一次遍历 j 的时候只需要不断保存并且更新 A[i] + i 的值即可求出最大值。

```c++
class Solution {
public:
    // 遍历长度
    int maxScoreSightseeingPair(vector<int>& values) {
        int maxScore = INT_MIN, left = values[0];
        for(int i = 1; i < values.size(); i++) {
            maxScore = max(maxScore, left + values[i] - i); // 更新最大值
            left = max(left, values[i] + i); // 更新左侧的最大值
        }
        return maxScore;
    }
};
```