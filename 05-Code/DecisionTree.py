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


