### 降维的意义

高维数据存在很多冗余数据和噪声，希望在尽量保证信息量不丢失的情况下对数据进行降维，从而提升特征表达能力，降低训练复杂度。

### 信噪比

信号具有较大的方差，噪声具有较小的方差。信噪比越大表示数据的是质量越好。因此可以认为，数据在方差大的维度上的信息保存较好。

### 中心化的意义

使得投影后的均值为0，计算方差的时候可以省去此项。

### 求解方法

**1. 均值标准化**

获取每个维度的均值，设 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_j) 为第 ![[公式]](https://www.zhihu.com/equation?tex=j) 个维度的均值，则

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_j%3D%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7Dx_%7Bj%7D%5E%7B%28i%29%7D%5Ctag%7B1%7D+)

再对原始的数据进行替换，

![[公式]](https://www.zhihu.com/equation?tex=x_%7Bj%7D%3Dx_%7Bj%7D-%5Cmu_j+%5Ctag%7B2%7D+)

**2.求解协方差矩阵**

经过均值标准化之后的数据的协方差矩阵为

![[公式]](https://www.zhihu.com/equation?tex=%5CSigma%3DX%5ETX%5Ctag%7B3%7D+)

**3.获取特征向量**

一般来说， ![[公式]](https://www.zhihu.com/equation?tex=%5CSigma) 会有 ![[公式]](https://www.zhihu.com/equation?tex=n) 个特征值，对应 ![[公式]](https://www.zhihu.com/equation?tex=n) 个特征向量，如果需要将原始数据从 ![[公式]](https://www.zhihu.com/equation?tex=n) 维降低到 ![[公式]](https://www.zhihu.com/equation?tex=k) 维，则只需要选取特征值最大的 ![[公式]](https://www.zhihu.com/equation?tex=k) 个特征值对应的特征向量即可，