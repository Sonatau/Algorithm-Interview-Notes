import numpy as np
from numpy.random import rand, seed, shuffle, normal
import matplotlib.pyplot as plt


# 模型准确率计算
def get_acc(y, y_hat):
    return sum(yi == yi_hat for yi, yi_hat in zip(y, y_hat)) / len(y)


# 查准率 TP / (TP + NP)
def get_precision(y, y_hat):
    true_positive = sum(yi and yi_hat for yi, yi_hat in zip(y, y_hat))
    predicted_positive = sum(y_hat)
    return true_positive / predicted_positive


# 查全率 TP / (TP + FN) = TPR
def get_recall(y, y_hat):
    true_positive = sum(yi and yi_hat for yi, yi_hat in zip(y, y_hat))
    actual_positive = sum(y)  # 真正的正例
    return true_positive / actual_positive


# 假正率：所有负例样本中被预测为正类的概率 FP / N = FP / (TN + FP)
def get_fpr(y, y_hat):
    false_positive = sum(yi == 0 and yi_hat == 1 for yi,
                         yi_hat in zip(y, y_hat))
    actual_negative = len(y) - sum(y)
    return false_positive / actual_negative


def get_roc(y, y_hat_prob):
    thresholds = sorted(set(y_hat_prob), reverse=True)  # 阈值选择
    ret = [[0, 0]]  # 第一次全部预测为负例 为原始点[0,0]

    # 大于阈值则为正例
    for threshold in thresholds:
        y_hat = [int(yi_hat_prob >= threshold) for yi_hat_prob in y_hat_prob]
        ret.append([get_recall(y, y_hat), get_fpr(y, y_hat)])

    return ret


def get_auc(y, y_hat_prob):
    roc = iter(get_roc(y, y_hat_prob))
    tpr_pre, fpr_pre = next(roc)
    auc = 0
    for tpr, fpr in roc:
        auc += (tpr + tpr_pre) * (fpr - fpr_pre) / 2  # 梯形求面积
        tpr_pre = tpr
        fpr_pre = fpr

    return auc


def power_positive(x):
    if x == 1:
        if rand() > 0.05:
            return rand() / 2 + 0.5
        else:
            return rand() / 2
    else:
        if rand() > 0.3:
            return rand() / 2
        else:
            return rand() / 2 + 0.5


seed(100)
y = np.array([0, 1] * 500)
shuffle(y)

seed(20)
y_pred = rand(1000)
points = np.array(get_roc(y, y_pred))
plt.plot(points[:, 1], points[:, 0])
plt.show()

y_pred = np.array([power_positive(yi) for yi in y])
points = np.array(get_roc(y, y_pred))
plt.plot(points[:, 1], points[:, 0])
plt.show()
