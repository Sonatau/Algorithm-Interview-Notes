<!-- Tag: 栈 -->

### 用两个栈实现队列

**题目描述**

```tex
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示：

  1 <= values <= 10000
  最多会对 appendTail、deleteHead 进行 10000 次调用

```

**C++**

```c++
class CQueue {
public:
    stack<int> st1;  // s1作为输入栈
    stack<int> st2;  // s2作为输出栈
    // 初始化两个栈
    CQueue() {
    }
    
    // 入队
    void appendTail(int value) {
        st1.push(value);
    }
    
    int deleteHead() {
        if (!st2.empty()) {
            int temp = st2.top();
            st2.pop();
            return temp;
        } else {
            if (!st1.empty()) {
                while (!st1.empty()) {
                    st2.push(st1.top());
                    st1.pop();
                }
                int temp = st2.top();
                st2.pop();
                return temp;
            } else return -1;
        }
    }
};
```
