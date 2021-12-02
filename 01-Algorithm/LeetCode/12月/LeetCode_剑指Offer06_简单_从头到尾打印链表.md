<!-- Tag: 链表 -->

#### 从尾到头打印链表

**题目描述**

```tex
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
  输入：head = [1,3,2]
  输出：[2,3,1]
 
限制：
	0 <= 链表长度 <= 10000
```

**C++**

先遍历一遍得到长度，再反向填充

```c++
class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        int idx = -1;
        ListNode *p = head, *q = head;
        while(p) {
            idx++;
            p = p->next;
        }
        vector<int> res(idx + 1, 1);
        while(q) {
            res[idx--] = q->val;
            q = q->next;
        }
        return res;
    }
};
```