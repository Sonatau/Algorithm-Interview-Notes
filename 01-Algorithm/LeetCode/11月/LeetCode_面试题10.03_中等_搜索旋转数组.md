<!-- Tag: 查找 -->

### 搜索旋转数组

**题目描述**

```tex
搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

示例1:

 输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
 输出: 8（元素5在该数组中的索引）

示例2:

 输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
 输出：-1 （没有找到）
 
提示:

arr 长度范围在[1, 1000000]之间

```

**C++**

```c++
class Solution {
public:
    // rotate操作 也就是从首位选择一些元素移到最后
    // 优先考虑左边
    int search(vector<int>& arr, int target) {
        if(arr.size() == 1) return arr[0] == target ? 0 : -1;
        int left = 0, right = arr.size() - 1;
        while(arr[0] == arr[right]) right--; // 这个很重要！（但我也不知道为什么

        // 其中有一边是有序的
        while(left < right) {
            int mid = (left + right) >> 1;
            // 假设左边有序 尽可能先查询左边 因为索引小
            if(arr[left] <= arr[mid]) {
                // 有序且在区间内 缩小搜索范围
                if(arr[left] <= target && target <= arr[mid]) right = mid;
                // 左侧有序但不在区间内 则需要查询右边
                else left = mid + 1;
            }
            // 假设右侧有序 
            else if(arr[mid] <= arr[right]) {
                // 有序且target在区间内 在缩小搜索范围
                if(arr[mid] <= target && target <= arr[right]) left = mid;
                // 有序但不在区间范围 则需要查询左边
                else right = mid - 1;
            }
        }
        
        return arr[left] == target ? left : -1;
    }
};
```