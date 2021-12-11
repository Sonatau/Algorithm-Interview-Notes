<!-- Tag: 查找 -->

### 第一个只出现一次的字符

**题目描述**

```tex
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:
输入：s = "abaccdeff"
输出：'b'

示例 2:
输入：s = "" 
输出：' '
 

限制：
0 <= s 的长度 <= 50000

```

**C++**

我以为还有更简便的方法，没想到都差不多～～

```c++
class Solution {
public:
    char firstUniqChar(string s) {
        unordered_map<char, int> st;
        for(int i = 0; i < s.size(); i++) st[s[i]] ++;
        for(int i = 0; i < s.size(); i++) {
            if(st[s[i]] == 1) return s[i];
        }
        return ' ';
    }
};
```