<!-- Tag: 链表 -->

### 两个链表的第一个公共节点

**题目描述**

```tex
输入两个链表，找出它们的第一个公共节点。
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *p = headA, *q = headB;
        int lenA = 0, lenB = 0;
        while(p) {
            lenA ++;
            p = p->next;
        }
        while(q) {
            lenB++;
            q = q->next;
        }
        int sub = abs(lenA - lenB);
        p = headA, q = headB;
        if(lenA > lenB) {
            while(sub) { 
                p = p->next;
                sub--;
            }
        } else {
            while(sub) { 
                q = q->next;
                sub--;
            }
        }
        while(p!=q) {
            p = p->next;
            q = q->next;
        }
        return p;
    }
};
```