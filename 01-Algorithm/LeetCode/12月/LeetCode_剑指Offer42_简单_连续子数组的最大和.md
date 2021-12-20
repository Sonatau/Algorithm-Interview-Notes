<!-- Tag: 动态规划 -->

### 连续子数组的最大和

**题目描述**

```tex
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。


示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100

```

**C++**

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = nums[0];
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i - 1] >= 0) nums[i] = nums[i] + nums[i - 1];
            max_sum = max(max_sum, nums[i]);
        }
        return max_sum;
    }
};
```