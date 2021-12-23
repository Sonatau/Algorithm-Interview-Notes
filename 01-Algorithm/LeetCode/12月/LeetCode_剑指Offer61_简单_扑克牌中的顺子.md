<!-- Tag: 数组 -->

### 扑克牌中的顺子

**题目描述**

```tex
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True
 
示例 2:

输入: [0,0,1,2,5]
输出: True
```

**C++**

```c++
class Solution {
public:
    bool isStraight(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int zero_num = 0;
        int idx = 0;
        while(idx < nums.size() && nums[idx] == 0) {
            zero_num++;
            idx++;
        }
        if(idx == nums.size()) return true;

        int last = nums[idx++];
        while(idx < nums.size()) {
            if(nums[idx] == last) return false; // 避免重复
            if(nums[idx] - 1 == last) {
                last += 1;
                idx++;
            } else {
              	// 够不够补足
                if(nums[idx] - last - 1 > zero_num) return false;
                else {
                    zero_num -= (nums[idx] - last - 1);
                    last = nums[idx];
                    idx++;
                }
            }
        }

        return true;
    }
};
```