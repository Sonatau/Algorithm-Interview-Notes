<!-- Tag: 数组 -->

### 数值的整数次方

**题目描述**

```tex
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

 

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
```

**C++**

第一次写的: return myPow(x, n/2) * myPow(x, n - n/2); 因为每次都还是以x为基数去乘，速度特别慢，

0.00001 2147483647的时候就超时了。

```c++
class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0) return 1;
        if(n == 1) return x;
        if(n == -1) return 1 / x;
        
        return (n & 1) ? x * myPow(x, n - 1) : myPow(x * x, n / 2);
      
    }
};
```

