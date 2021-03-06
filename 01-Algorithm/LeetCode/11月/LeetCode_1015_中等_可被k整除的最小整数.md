<!-- Tag: 数学 -->

### 可被k整除的最小整数

**题目描述**

```wiki
给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。返回 N 的长度。如果不存在这样的 N，就返回 -1。

示例 1：
  输入：1
  输出：1
  解释：最小的答案是 N = 1，其长度为 1。

示例 2：
  输入：2
  输出：-1
  解释：不存在可被 2 整除的正整数 N 。

示例 3：
  输入：3
  输出：3
  解释：最小的答案是 N = 111，其长度为 3。
 
提示：
  1 <= K <= 10^5
```

**C++**

```txt
(x个1) 11...11 = (10^x - 1) / 9

(10^x - 1) / 9 能被k整除时，
等价：(10^x - 1)能被9k整除
等价：10^x%9k = 1
等价：10^x - 9k*t = 1，即存在一个t使得两者差值为1

设存在d为10^x 与 9k的最小公约数，则10^x 与 9k的差值必定也可以被d整除
由于10^x与9已经互质了，因此只要判断10^x与k是否互质即可
等价：判断k能否被2和5整除
```



1. 只要不满足 K%2 == 0 || K%5 == 0，就必然有解。 2和5可以一眼看出肯定除不尽，但不懂其他情况一定有解的数学证明。

```c++
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        // to_string
        if(k % 2 == 0 || k % 5 == 0) return -1;
        long long num = 1, len = 1;
        while (num % k) {
            num %= k;
            num = num * 10 + 1;
            len++;
        }
        return len;
    }
};
```