<!-- Tag: 位运算 -->

### 数组中数字出现的次数II

**题目描述**

```tex
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

 
示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1
 

限制：
1 <= nums.length <= 10000
1 <= nums[i] < 2^31

```

**C++**

统计每一列1的个数，是3的倍数，表明 贡献了该位的数字是3的整数； 反之，如果一个数字只出现了一次，那么其贡献过的相应位置的1的总个数绝对不可能是三的倍数。最后将该列模3得到1后，右移相应位，可以转变成2进制上的相应位置为1。

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int bit = 32, res = 0, count; // int型为32位整数
        for(int i = 0; i < bit; i ++) {
            count = 0;
            for(int j = 0; j < nums.size(); j ++) {
            count += ( nums[j] >> i ) & 1; // 上一次的移位本次是不会记录的 因此 每次都是移动i位
            }
            if(count % 3 == 1) res += (1 << i);
        }
        return res;
    }
};
```