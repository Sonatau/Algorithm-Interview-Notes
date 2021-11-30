<!-- Tag: 二分查找 -->

### 青蛙跳台阶

**题目描述**

```tex
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1

示例 2：

输入：[2,2,2,0,1]
输出：0
```

**C++**

二分码死 下次再写不出直接跳楼

```c++
class Solution {
public:
    int minArray(vector<int>& numbers) {
        int l = 0, r = numbers.size() - 1;
        // 总有一边是顺序的
        while(l < r) {
            int mid = (l + r) >> 1;
            if(numbers[r] < numbers[mid]) l = mid + 1; // 在右
            else if(numbers[mid] < numbers[r]) r = mid; // 在左
            else r--;
        }
        return numbers[l];
    }
};
```