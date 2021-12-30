<!-- Tag: 数组 -->

### 数组中出现次数超过一半的数字

**题目描述**

```tex
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000
```

**C++**

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        //摩尔投票
        int count = 0;
        int card;
        for(auto num:nums){
            if(count == 0) card = num;
            count += (card == num)?1:-1;
        }
        return card;
    }
};
```