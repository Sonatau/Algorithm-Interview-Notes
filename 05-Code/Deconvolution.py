# coding:utf-8
"""
@Author  : sonata
@time    : 16/12/2021 16:07
@File    : Deconvolution.py
@Software: PyCharm
@Role    : 
"""
import torch
import torch.nn as nn

batch_size = 1
in_channel = 1
height = 4
width = 4
data_shape = (batch_size, in_channel, height, width)
conv_input = torch.ones(data_shape)

out_channel = 1
kernel_size = 4  # 3
weight_shape = (in_channel, out_channel, kernel_size, kernel_size)
conv_weight = torch.ones(weight_shape)

conv_trans = nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=kernel_size, stride=2, padding=1)
conv_trans.weight = torch.nn.Parameter(conv_weight)

y = conv_trans.forward(conv_input)
print(y)