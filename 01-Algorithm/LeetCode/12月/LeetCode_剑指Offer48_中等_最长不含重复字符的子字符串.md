<!-- Tag: 动态规划 -->

### 最长不含重复字符的子字符串

**题目描述**

```tex
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

```

**C++**

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() == 0) return 0;
        unordered_map<char, int> hp;  // char and idx
        int len = s.size();
        int max_len = 1;
        vector<int> dp(len + 1, 1);
        hp[s[0]] = 0;
        for(int i = 1; i < len; i++) {
            dp[i] = 1 + dp[i - 1];
            if(hp.find(s[i]) != hp.end()) dp[i] = min(i - hp[s[i]], dp[i]);
            hp[s[i]] = i;
            max_len = max(dp[i], max_len);
        }
        return max_len;
    }
};
```