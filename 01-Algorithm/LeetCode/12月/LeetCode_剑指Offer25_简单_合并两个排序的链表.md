<!-- Tag: 链表 -->

### 合并两个排序的链表

**题目描述**

```tex
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

限制：

0 <= 链表长度 <= 1000
```

**C++**

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *res = new ListNode(INT_MIN);
        ListNode *p = l1, *q = l2, *r = res;
        while ( p && q) {
            if( p->val >= q->val) {
                r->next = q;
                q = q->next;
                r = r->next;
            } else {
                r->next = p;
                r = r->next;
                p = p->next;
            }
        }

        if (p) {
            r->next = p;
        }

        if (q) {
            r->next = q;
        }
        return res->next;
    }
};

```