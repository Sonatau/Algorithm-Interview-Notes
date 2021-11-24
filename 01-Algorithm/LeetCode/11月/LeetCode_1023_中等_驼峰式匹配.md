<!-- Tag: 字符串 -->

### 驼峰式匹配

**题目描述**

```tex
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。


示例 1：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".

示例 2：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".

示例 3：

输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输入：[false,true,false,false,false]
解释： 
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
 
提示：

  1 <= queries.length <= 100
  1 <= queries[i].length <= 100
  1 <= pattern.length <= 100
  所有字符串都仅由大写和小写英文字母组成。

```

**C++**

```c++
class Solution {
public:
    // 对于每个单词 先判断当前位置是否为小写字母 不是则直接置为false
    // 如果是小写字母 pattern中的元素按顺序出现即可
    vector<bool> camelMatch(vector<string>& queries, string pattern) {
        vector<bool> res;
        for(int i = 0; i < queries.size(); i++) {
            int idx = 0, j = 0; // pattern指针
            string cur = queries[i];
            while(j < cur.size()) {
                if(idx == pattern.size()) {
                    if(j == cur.size()) res.push_back(true);
                    else {
                        if(cur[j] - 'a' < 0) res.push_back(false);
                        else j++;
                    }
                } else {
                    if(cur[j] == pattern[idx]) idx++;
                    else {
                        if(cur[j] - 'a' < 0)
                    }
                }
            }
        }
        return res;
    }
};
```