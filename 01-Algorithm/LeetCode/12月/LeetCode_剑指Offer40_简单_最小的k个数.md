<!-- Tag: 堆 -->

### 最小的k个数

**题目描述**

```tex
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
```

**C++**

```c++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        vector<int> res;
        if (k == 0) return res;
        priority_queue<int, vector<int>> heap; // 用大根堆维护维护前k小的数 堆顶元素是k个数中最大的

        for (int i = 0; i < arr.size(); i++) {
            if (heap.empty() || heap.size() < k) heap.push(arr[i]);
            else {
                if (heap.top() > arr[i]) {
                    heap.pop();
                    heap.push(arr[i]);
                }
            }
        }
        while (!heap.empty()) {
            res.push_back(heap.top());
            heap.pop();

        }

        return res;
    }
};
```