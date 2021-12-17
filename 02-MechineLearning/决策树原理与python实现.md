## 生成步骤

1. 特征选择
2. 决策树的生成
3. 剪枝

## 特征选择

某件事的不确定性越大，需要了解的信息就越多；在统计中，用熵度量随机变量的不确定性；

**熵越大，随机变量的不确定就越大**

### **信息熵**

若一个随机变量Y的取值为$Y = {c_1, c_2...}$，概率分布为$P(Y = c_i) = p_i, i =1,2,..k$

那么随机变量Y的熵定义为
$$
H(Y) = -\sum_{i=1}^k p_ilog(p_i)
$$
举个例子：

$$
Entropy(t) = -\frac{1}{6}log_2(\frac{1}{6})-\frac{5}{6}log_2\frac{5}{6} = 0.65
$$

### 信息增益

随机变量Y的熵H(Y)与Y的条件熵H(Y｜X)之差就是信息增益
$$
g(Y, X) = H(Y) - H(Y|X)
$$
**信息增益依赖于特征，不同特征往往具有不同的信息增益。信息增益大的特征具有更强的分类能力。**

### 信息增益比

使用信息增益的缺点是，倾向于选择类别取之较多的特征
$$
Ratio(Y, X) = \frac{g(Y, X)}{H(X)}
$$

### 基尼系数

用于度量数据集的不纯度，指数越小，表明样本只属于同类的概率越高，即样本的纯度越高。

如下公式，Pk表示D中属于第k类的样本子集的概率，k为类别，N为类别的总数。

<img src="https://tva1.sinaimg.cn/large/007S8ZIlly1gicssxx6poj30r803a74k.jpg" style="height:50px" />
$$
p_k = \frac{|C_k|}{|D|}
$$

## 决策树生成

决策树的生成方法有三种：ID3、C4.5，CART树

### ID3算法

#### 缺点

1. 不能处理连续值
2. 容易过拟合
3. 偏向于优先选取取值种类较多的特征

#### 分裂停止条件

停止条件有以下三种：

- 当前集合的样本都属于同一类时，节点分裂停止
- 特征维度已经全部用完
- 每个特征的提纯效果都不太好，小于阈值

### C4.5

#### 解决方案

1. 将连续值离散化后，找出类别标签有变化的地方，取其中的值作为二分类划分的阈值，小于为一类，大于为一类
2. 过拟合问题时因为决策树的生成过程中分支太细导致的，引入**正则化系数**控制节点的个数
3. 用信息增益比来替代信息增益

#### 缺点

1. 和ID3一样，每个特征仅使用一次，使得特征信息的利用率较低
2. 简单的离散化，使得信息丢失（类别的划分太随意

### CART树

#### 特点

1. 可以处理分类和回归的问题：分类的时候用基尼系数衡量，回归可以使用均方误差。回归时，叶子结点的值用所有子集的均值表示。
2. 二叉树对每个特征或特征的取值进行划分。分类时切分子集，计算基尼指数或平方误差。回归时选择相邻两个值的中值作为划分点。

#### 分类树和回归树的区别

- **特征选择的标准不同**

    - 分类：某个特征的某个划分点的基尼指数

    - 回归：选择某个特征的某个取值进行划分，使得均方误差和最小（小中小）
        $$
        \sum_{x_i\in D_1}(y_i - c_1)^2 + \sum_{x_i\in D_2}(y_i - c_2)^2
        $$

- **输出结果处理方式不同**

    - 分类：选择样本类别占多数者对应的类别标签作为该叶子结点的类别标签
    - 回归：选择子集中所有样本的均值或者中位数作为输出值



## 剪枝

后剪枝比较常用，就是先构造好一棵树，比较剪掉某个子树与不剪时的损失函数；

选择结构损失，将叶子结点的个数作为损失函数的正则项考虑进去。

比如对于一颗以$T_i$为根结点的子树，其结构损失为：
$$
L(\alpha,T_i) = L(T_i) + \alpha|T_i|
$$
如果把它作为单结点，将树枝全部减去，则有
$$
L(\alpha,i) = L(i) + \alpha * 1
$$
当两式相等时，把树枝全部减去的结点更少，效果更优，有：
$$
\alpha = \frac{L(i) - L(T_i)}{|T_i| - 1}
$$

#### 剪枝步骤

集合M存储的是自下而上的剪枝阈值

第三步从M中选择了最大的ak，自上而下进行判断，只要有比ak更小的a则剪枝，这说明不需要这么多结点即可达到与Tk（大）一样的效果，存入最优子树集合。

最后从最优子树集合中选出最优子树。

![](https://tva1.sinaimg.cn/large/008i3skNly1gxh43ehhqlj316y0pajw4.jpg)



## 代码实践

### ID3的构造过程

```python
# coding:utf-8
"""
@Author  : sonata
@time    : 17/12/2021 17:11
@File    : DecisionTree.py
@Software: PyCharm
@Role    : 
"""
import numpy as np
from math import log


def create_dataset():
    """ 定义数据集 """
    dataset = [[0, 0, 0, 0, 'N'],
               [0, 0, 0, 1, 'N'],
               [1, 0, 0, 0, 'Y'],
               [2, 1, 0, 0, 'Y'],
               [2, 2, 1, 0, 'Y'],
               [2, 2, 1, 1, 'N'],
               [1, 2, 1, 1, 'Y']]
    labels = ['outlook', 'temperature', 'humidity', 'windy']
    return dataset, labels


def calculate_shannon_ent(dataset):
    """计算熵"""
    num_entries = len(dataset)
    label_counts = {}
    for i in dataset:
        current_label = i[-1]
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
        label_counts[current_label] += 1  # 每一类各多少个， {'Y': 4, 'N': 3}
    shannon_ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        shannon_ent -= prob * log(prob, 2)
    return shannon_ent


def split_dataset(dataset, axis, value):
    """把选做特征的列除去"""
    ret_dataset = []
    for example in dataset:
        if example[axis] == value:
            reduce_example = example[:axis]
            reduce_example.extend(example[axis+1:])
            ret_dataset.append(reduce_example)

    return ret_dataset


def choose_best_feature(dataset):
    num_feature = len(dataset[0]) - 1
    base_entropy = calculate_shannon_ent(dataset)
    best_info_gain_ration = 0.0
    best_feature = -1
    for i in range(num_feature):
        feature_list = [example[i] for example in dataset]
        unique_val = set(feature_list)
        new_entropy = 0.0
        split_info = 0.0
        for value in unique_val:
            sub_dataset = split_dataset(dataset, i, value)
            prob = len(sub_dataset) / float(len(dataset))
            new_entropy += prob * calculate_shannon_ent(sub_dataset)
            split_info += -prob * log(prob, 2)

        info_gain = base_entropy - new_entropy  # 以该特征作为分类的信息增益
        if split_info == 0:
            continue
        info_gain_ratio = info_gain / base_entropy  # 以该特征作为分类的信息增益比
        if info_gain_ratio > best_info_gain_ration:
            best_info_gain_ration = info_gain_ratio
            best_feature = i

    return best_feature


def majority_cnt(class_list):
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0
        class_count[vote] += 1
    sorted_class_count = sorted(class_count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    return sorted_class_count[0][0]


def create_tree(dataset, labels):
    class_list = [example[-1] for example in dataset]

    # class_list中所有元素都相等时，类别完全相同，停止划分
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    # 只有一个类别的时候 直接统计最大样本的类别数
    if len(dataset[0]) == 1:
        return majority_cnt(class_list)

    best_feat = choose_best_feature(dataset)
    best_feat_label = labels[best_feat]

    myTree = {best_feat_label: {}}
    del(labels[best_feat])

    feat_value = [example[best_feat] for example in dataset]
    unique_value = set(feat_value)
    for value in unique_value:
        sub_label = labels[:]
        myTree[best_feat_label][value] = create_tree(split_dataset(dataset, best_feat, value), sub_label)

    return myTree


dataset, labels = create_dataset()
label_tmp = labels[:]
decision_tree = create_tree(dataset, label_tmp)
print(decision_tree)

```

输出如下：

```python
{'outlook': {0: 'N', 1: 'Y', 2: {'windy': {0: 'Y', 1: 'N'}}}}
```

