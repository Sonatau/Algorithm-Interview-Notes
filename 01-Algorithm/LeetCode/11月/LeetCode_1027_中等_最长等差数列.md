<!-- Tag: 动态规划 -->

### 最长等差数列

**题目描述**

```tex
给定一个整数数组 A，返回 A 中最长等差子序列的长度。

回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k] 其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1。并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。

示例 1：

  输入：[3,6,9,12]
  输出：4
  解释： 
  整个数组是公差为 3 的等差数列。
  
示例 2：

  输入：[9,4,7,2,10]
  输出：3
  解释：
  最长的等差子序列是 [4,7,10]。
  
示例 3：

  输入：[20,1,15,3,10,5,8]
  输出：4
  解释：
  最长的等差子序列是 [20,15,10,5]。
 

提示：

  2 <= A.length <= 2000
  0 <= A[i] <= 10000
```

**C++**

1. 开一个大数组保存所有可能存在的差值
2. 双重遍历，以i为结尾，sum为差值的元素有几个（刚开始看到这种题目总是会以为是开一维数组就够了

```c++
class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        if(nums.size() <= 2) return nums.size();
        int res = 0;
        vector<vector<int>> dp(nums.size(),vector<int>(20001,1));

        for(int i = 1; i < nums.size(); i++) {
            for(int j = 0; j < i; j++) {
                // 以i为结尾 sum为差值
                int sum = nums[i] - nums[j] + 10000; // 差值
                dp[i][sum] = 2;
                if(dp[j][sum] > 0) dp[i][sum] = max(dp[i][sum], dp[j][sum] + 1);

                res = max(res, dp[i][sum]);
            }
        }
        return res;
    }
};
```


