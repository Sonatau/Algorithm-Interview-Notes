<!-- Tag: 数组 -->

### 整数的英语表示

**题目描述**

```tex
给定一个整数，打印该整数的英文描述。

示例 1:

  输入: 123
  输出: "One Hundred Twenty Three"
  
示例 2:

  输入: 12345
  输出: "Twelve Thousand Three Hundred Forty Five"
  
示例 3:

  输入: 1234567
  输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
  
  
示例 4:

  输入: 1234567891
  输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

**C++**

```c++
class Solution {
public:
    vector<string> singles = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    vector<string> teens = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    vector<string> tens = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    vector<string> thousands = {"", "Thousand", "Million", "Billion"};
    
    string numberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }
        string sb;
        for (int i = 3, unit = 1000000000; i >= 0; i--, unit /= 1000) {
            int curNum = num / unit;
            if (curNum != 0) {
                num -= curNum * unit;
                sb = sb + toEnglish(curNum) + thousands[i] + " ";
            }
        }
        while (sb.back() == ' ') {
            sb.pop_back();
        }
        return sb;
    }

    string toEnglish(int num) {
        string curr;
        int hundred = num / 100;
        num %= 100;
        if (hundred != 0) {
            curr = curr + singles[hundred] + " Hundred ";
        }
        int ten = num / 10;
        if (ten >= 2) {
            curr = curr + tens[ten] + " ";
            num %= 10;
        }
        if (num > 0 && num < 10) {
            curr = curr + singles[num] + " ";
        } else if (num >= 10) {
            curr = curr + teens[num - 10] + " ";
        }
        return curr;
    }
};
```