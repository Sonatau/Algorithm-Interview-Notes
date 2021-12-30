<!-- Tag: 位运算 -->

### 数组中数字出现的次数

**题目描述**

```tex
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums.length <= 10000

```

**C++**

```c++
class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        int cur = 0;
        int nums1 = 0, nums2 = 0;
        for(int i = 0; i < nums.size(); i++) cur ^= nums[i];
        int i = 1;
        while((i & cur) == 0) i <<= 1;
        cout << i;
        for(int j = 0; j < nums.size(); j++) {
            if(i & nums[j]) nums1 ^= nums[j];
            else nums2 ^= nums[j];
        }
        return {nums1, nums2};
    }
};
```