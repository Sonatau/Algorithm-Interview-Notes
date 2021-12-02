<!-- Tag: 链表 -->

#### 反转链表

**题目描述**

```tex
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
  输入: 1->2->3->4->5->NULL
  输出: 5->4->3->2->1->NULL
 

限制：
	0 <= 节点个数 <= 5000
```

**C++**

把当前遍历到的节点接在ans后面。

```c++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head) return NULL;
        ListNode *ans = new ListNode(0);
        ans->next = head;
        // 一个指针维护当前遍历到的节点 另一个指针维护它的上一个节点
        ListNode *p = head, *q = head->next;
        while(q) {
            p->next = q->next;
            q->next = ans->next;
            ans->next = q;
            q = p->next;

        }
        return ans->next;
    }
};
```