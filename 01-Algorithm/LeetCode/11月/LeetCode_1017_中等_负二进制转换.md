<!-- Tag: 位运算 -->

### 负二进制转换

**题目描述**

```tex
给出数字 N，返回由若干 "0" 和 "1"组成的字符串，该字符串为 N 的负二进制（base -2）表示。
除非字符串就是 "0"，否则返回的字符串中不能含有前导零。

示例 1：
  输入：2
  输出："110"
  解释：(-2) ^ 2 + (-2) ^ 1 = 2

示例 2：
  输入：3
  输出："111"
  解释：(-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

示例 3：
  输入：4
  输出："100"
  解释：(-2) ^ 2 = 4


提示：
	0 <= N <= 10^9
```

**C++**

轻轻敲醒沉睡的心灵... 呜呜呜闫总好厉害 我啥也不会

推导过程如下：

![](https://tva1.sinaimg.cn/large/008i3skNly1gwnref1i3kj31l00o00ut.jpg)

```c++
class Solution {
public:
    string baseNeg2(int n) {
        if(!n) return "0";
        string res;
        while(n) {
            int r = n & 1; // n模-2 !!注意这个要用位运算 因为r应该是非负数 如果%的话得到的结果是负数
            res += to_string(r);
            n = (n - r) / -2;
        }
        // 翻转字符串结果
        reverse(res.begin(), res.end());
        return res;
    }
};
```

