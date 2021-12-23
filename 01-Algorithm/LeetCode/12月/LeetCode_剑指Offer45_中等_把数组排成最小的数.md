<!-- Tag: 数组 -->

### 把数组排成最小的数

**题目描述**

```tex
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。


示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
 

提示:

0 < nums.length <= 100

```

**C++**

```c++
class Solution {
public:
    // 位数上 数字小且总长短的优先
    string minNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int a, int b) {
            string t1 = to_string(a), t2 = to_string(b);
            return t1 + t2 < t2 + t1;
        });
        string ans = "";
        for(int i = 0; i < nums.size(); i++) ans += to_string(nums[i]);
        return ans;
    }
};
```