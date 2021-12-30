<!-- Tag: 数组 -->

### 圆圈中最后剩下的数字

**题目描述**

```tex
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 
示例 1：

输入: n = 5, m = 3
输出: 3

示例 2：

输入: n = 10, m = 17
输出: 2
 

限制：

1 <= n <= 10^5
1 <= m <= 10^6

```

**C++**

![](https://tva1.sinaimg.cn/large/008i3skNly1gxvo7j0z2tj316x0u0n05.jpg)

![](https://tva1.sinaimg.cn/large/008i3skNly1gxvo800r3vj319x0u0wl4.jpg)

```c++
class Solution {
public:
    int lastRemaining(int n, int m) {
        int index = 0; // 当只有一人的时候 胜利者下标肯定为0
        for(int i = 2; i <= n; i++){
            index = (index + m) % i; // 每多一人 胜利者下标相当于往右挪动了m位,再对当前人数取模求得新的胜利者下标
        }
        return index;
    }
};
```