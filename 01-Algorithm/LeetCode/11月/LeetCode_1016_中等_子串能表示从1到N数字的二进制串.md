<!-- Tag: 哈希表 -->
<!-- Tag: 字符串 -->

### 子串能表示从1到N数字的二进制串

**题目描述**
```tex
给定一个二进制字符串 S（一个仅由若干 '0' 和 '1' 构成的字符串）和一个正整数 N，如果对于从 1 到 N 的每个整数 X，其二进制表示都是 S 的子串，就返回 true，否则返回 false。

示例 1：
  输入：S = "0110", N = 3
  输出：true
  
示例 2：
  输入：S = "0110", N = 4
  输出：false
  
提示：
  1 <= S.length <= 1000
  1 <= N <= 10^9

```

**C++**
1. 用哈希表存储字符串s中包含的所有数字
1. 最后判断哈希表的长度是否等于n即可

```c++
class Solution {
public:
    bool queryString(string s, int n) {
        unordered_set<int> sets;
        // l 起始位置
        for(int i = 0; i < s.size(); i++) {
            int x = 0;
            for(int j = i; j < s.size(); j++) {
                // x为当前长度和起始位置下表示的数值
                x = x * 2 + s[j] - '0';
                if(x > n) break;
                if(x) sets.insert(x);
            }
        }
        return sets.size() == n;
    }
};
```



