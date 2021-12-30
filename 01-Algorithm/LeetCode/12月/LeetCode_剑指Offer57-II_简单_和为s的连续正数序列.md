<!-- Tag: 数组 -->

### 和为s的连续正数序列

**题目描述**

```tex
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 
示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5
```

**C++**

滑动窗口的简单题

```c++
class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> ans;
        int l = 1, r = 2, sum = l + r;
        if(target < sum) return ans;
        while(l < r) {
            if(sum <= target) {
                if(sum == target) {
                    vector<int> cur;
                    for(int i = l; i <= r; i++) cur.push_back(i);
                    ans.push_back(cur);
                }
                r ++;
                sum += r;
            } else {
                sum -= l;
                l++;
            }
        }
        return ans;
    }
};
```