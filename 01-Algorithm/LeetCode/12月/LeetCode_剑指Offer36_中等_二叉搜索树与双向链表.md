<!-- Tag: 二叉树 -->

### 二叉搜索树与双向链表

**题目描述**

```tex
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
```

**C++**

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
public:
    queue<Node*> st;
    Node* treeToDoublyList(Node* root) {
        if(!root) return NULL;

        preOrder(root);
        Node* pre = st.front();

        while(st.size() >= 2) {
            Node* tmp1 = st.front();
            st.pop();
            Node* tmp2 = st.front();
            tmp1->right = tmp2;
            tmp2->left = tmp1;
        }
        Node* tmp1 = st.front();
        pre->left = tmp1;
        tmp1->right = pre;

        return pre;
    }

    void preOrder(Node* root) {
        if(root->left) preOrder(root->left);
        st.push(root);
        if(root->right) preOrder(root->right);
    }
};
```