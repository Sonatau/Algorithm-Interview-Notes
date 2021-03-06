<!-- Tag: 数组 -->

### 调整数组顺序使奇数位于偶数前面

**题目描述**

```tex
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。


示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 
提示：

0 <= nums.length <= 50000
0 <= nums[i] <= 10000

```

**C++**

```c++
class Solution {
public:
    vector<int> exchange(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while(left <= right) {
            while(nums[left] % 2 == 0 && left <= right) {
                int tmp = nums[right];
                nums[right--] = nums[left];
                nums[left] = tmp;
            }
            left++;
        }
        return nums;
    }
};
```