<!-- Tag: 数组 -->

### 将数组分成和相等的三个部分

**问题描述**

```txt
给你一个整数数组 arr，只有可以将其划分为三个和相等的 非空 部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i + 1 < j 且满足 (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1]) 就可以将数组三等分。

示例 1：
  输入：arr = [0,2,1,-6,6,-7,9,1,2,0,1]
  输出：true
  解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

示例 2：
  输入：arr = [0,2,1,-6,6,7,9,-1,2,0,1]
  输出：false

示例 3：
  输入：arr = [3,3,6,5,-2,2,5,1,-9,4]
  输出：true
  解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


提示：
  3 <= arr.length <= 5 * 104
  -104 <= arr[i] <= 104
```

**C++**

1. 数组之和可以被3除尽，`sum = sum / 3`
2. 将数组分为A、B、C三个部分，每个部分的和相同
3. 若A、B的和均为sum，只需要保证不是遍历到了最后一位即可。（防止`[1,-1,1-,1]`的情况）

```c++
class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        if(arr.size() < 3) return false;
        long long sum = 0, temp = 0, times = 0;
        sum = accumulate(arr.begin(), arr.end(), 0); // 数组求和
      
        if(sum % 3) return false;
        else {
            sum = sum / 3;
            for(int i = 0; i < arr.size(); i++) {
                temp += arr[i];
                if(temp == sum) {
                    temp = 0;
                    if(++times == 2 && i != arr.size() - 1) return true;
                }
            }
        }
        return false;
    }
};
```

