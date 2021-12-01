# coding:utf-8
"""
@Author  : sonata
@time    : 01/12/2021 14:57
@File    : BatchNormalization.py
@Software: PyCharm
@Role    : 
"""
from numpy.core.fromnumeric import shape
import torch
import torch.nn as nn
import numpy as np


class BN:
    def __init__(self, momentum, eps, num_features):
        """
        初始化参数值
        :param momentum: 追踪样本整体均值和方差的动量
        :param eps: 防止数值计算错误
        :param num_features: 特征数量
        """

        self._mean = 0
        self._std = 1
        self._momentum = momentum
        self._eps = eps  # 防止计算无效
        self._num_features = num_features
        # 对应learnable参数beta和gamma，采用pytorch文档中的初始化值
        self._beta = np.zeros(shape=(num_features, ))
        self._gamma = np.ones(shape=(num_features, ))

    def batch_norm(self, x):
        for i in range(self._num_features):
            x_c = x[:, i]
            x_mean = x_c.mean()
            x_std_1 = x_c.std()
            x_std_2 = x_c.std(ddof=1)

            self._mean = (1 - self._momentum) * x_mean + \
                self._momentum * self._mean
            self._std = (1 - self._momentum) * x_std_2 ** 2 + \
                self._momentum * self._std

            x_hat = (x_c - x_mean) / np.sqrt(x_std_1 ** 2 + self._eps)
            x[:, i] = x_hat
            y = self._gamma[i] * x_hat + self._beta[i]  # 恢复数据表达

        print(x)


def bn_process(x, mean, var):
    b, c, w, h = x.shape
    # 对每个通道进行BN
    for i in range(c):
        x_c = x[:, i]
        mean_c = x_c.mean()
        std_1 = x_c.std()  # 总体方差
        std_2 = x_c.std(ddof=1)  # 样本方差（无偏估计

        x[:, i] = (x[:, i] - mean_c) / np.sqrt(std_1 ** 2 + 1e-5)

        mean[i] = mean[i] * 0.9 + mean_c * 0.1
        var[i] = var[i] * 0.9 + (std_2 ** 2) * 0.1  # 使用样本方差进行更行

    print(x)


x = torch.randn(2, 3, 2, 2)  # 元素个数等于channel深度
calculate_mean = [0.0, 0.0, 0.0]
calculate_var = [1.0, 1.0, 1.0]

bn_process(x.numpy().copy(), calculate_mean, calculate_var)

bn = nn.BatchNorm2d(3, eps=1e-5)  # 3 = num_features
output = bn(x)
print(output)  # output 与 x的输出值相同

bn2 = BN(momentum=0.1, eps=1e-5, num_features=3)
bn2._beta = bn.bias.detach().numpy()
bn2._gamma = bn.weight.detach().numpy()
bn2.batch_norm(x.numpy().copy())
