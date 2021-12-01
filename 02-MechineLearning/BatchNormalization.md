### 背景

#### 炼丹困扰

在深度学习中，由于问题的复杂性，我们往往会使用较深层数的网络进行训练，需要去尝试不同的学习率、初始化参数方法（例如Xavier初始化）等方式来帮助我们的模型加速收敛。

深度神经网络之所以如此难训练，其中一个重要原因就是网络中层与层之间存在**高度的关联性与耦合性**。

![](https://tva1.sinaimg.cn/large/008i3skNly1gwy7jjormcj31400oudkb.jpg)

网络中层与层之间的关联性会导致如下的状况：随着训练的进行，网络中的参数也随着梯度下降在不停更新。

- 一方面，当底层网络中参数发生微弱变化时，由于每一层中的线性变换与非线性激活映射，这些微弱变化随着网络层数的加深而被放大（类似蝴蝶效应）；

- 另一方面，参数的变化导致每一层的输入分布会发生改变，进而上层的网络需要不停地去适应这些分布变化，使得我们的模型训练变得困难。这一现象叫做Internal Covariate Shift。

#### Internal Covariate Shift

一个较规范的定义：在深层网络训练的过程中，由于网络中参数变化而引起内部结点数据分布发生变化的这一过程被称作Internal Covariate Shift。

我们定义每一层的线性变换为 ![[公式]](https://www.zhihu.com/equation?tex=Z%5E%7B%5Bl%5D%7D%3DW%5E%7B%5Bl%5D%7D%5Ctimes+input%2Bb%5E%7B%5Bl%5D%7D)，其中 ![[公式]](https://www.zhihu.com/equation?tex=l+) 代表层数；非线性变换为 ![[公式]](https://www.zhihu.com/equation?tex=A%5E%7B%5Bl%5D%7D%3Dg%5E%7B%5Bl%5D%7D%28Z%5E%7B%5Bl%5D%7D%29) ，其中 ![[公式]](https://www.zhihu.com/equation?tex=g%5E%7B%5Bl%5D%7D%28%5Ccdot%29) 为第 ![[公式]](https://www.zhihu.com/equation?tex=l)层的激活函数。

随着梯度下降的进行，每一层的参数 ![[公式]](https://www.zhihu.com/equation?tex=W%5E%7B%5Bl%5D%7D) 与 ![[公式]](https://www.zhihu.com/equation?tex=b%5E%7B%5Bl%5D%7D) 都会被更新，那么 ![[公式]](https://www.zhihu.com/equation?tex=Z%5E%7B%5Bl%5D%7D) 的分布也就发生了改变，进而 ![[公式]](https://www.zhihu.com/equation?tex=A%5E%7B%5Bl%5D%7D) 也同样出现分布的改变。而 ![[公式]](https://www.zhihu.com/equation?tex=A%5E%7B%5Bl%5D%7D) 作为第 ![[公式]](https://www.zhihu.com/equation?tex=l%2B1) 层的输入，意味着 ![[公式]](https://www.zhihu.com/equation?tex=l%2B1) 层就需要去不停适应这种数据分布的变化。

#### Internal Covariate Shift带来的问题？

**（1）上层网络需要不停调整来适应输入数据分布的变化，导致网络学习速度的降低**

我们在上面提到了梯度下降的过程会让每一层的参数 ![[公式]](https://www.zhihu.com/equation?tex=W%5E%7B%5Bl%5D%7D) 和 ![[公式]](https://www.zhihu.com/equation?tex=b%5E%7B%5Bl%5D%7D) 发生变化，进而使得每一层的线性与非线性计算结果分布产生变化。后层网络就要不停地去适应这种分布变化，这个时候就会使得整个网络的学习速率过慢。

**（2）网络的训练过程容易陷入梯度饱和区，减缓网络收敛速度**

当我们在神经网络中采用饱和激活函数（saturated activation function）时，例如sigmoid，tanh激活函数，很容易使得模型训练陷入梯度饱和区（saturated regime）。

随着模型训练的进行，我们的参数 ![[公式]](https://www.zhihu.com/equation?tex=W%5E%7B%5Bl%5D%7D) 会逐渐更新并变大，此时 ![[公式]](https://www.zhihu.com/equation?tex=Z%5E%7B%5Bl%5D%7D%3DW%5E%7B%5Bl%5D%7DA%5E%7B%5Bl-1%5D%7D%2Bb%5E%7B%5Bl%5D%7D) 就会随之变大，并且 ![[公式]](https://www.zhihu.com/equation?tex=Z%5E%7B%5Bl%5D%7D) 还受到更底层网络参数 ![[公式]](https://www.zhihu.com/equation?tex=W%5E%7B%5B1%5D%7D%2CW%5E%7B%5B2%5D%7D%2C%5Ccdots%2CW%5E%7B%5Bl-1%5D%7D) 的影响，随着网络层数的加深， ![[公式]](https://www.zhihu.com/equation?tex=Z%5E%7B%5Bl%5D%7D) 很容易陷入梯度饱和区，此时梯度会变得很小甚至接近于0，参数的更新速度就会减慢，进而就会放慢网络的收敛速度。

对于激活函数梯度饱和问题，有两种解决思路：

第一种就是更为非饱和性激活函数，例如线性整流函数ReLU可以在一定程度上解决训练进入梯度饱和区的问题。另一种思路是，我们可以让激活函数的输入分布保持在一个稳定状态来尽可能避免它们陷入梯度饱和区，这也就是Normalization的思路。

### Batch Normalization

#### 思路

尝试单独对每个特征进行normalizaiton就可以了，让每个特征都有均值为0，方差为1的分布即可。在mini-batch的基础上进行计算。

#### 算法步骤

介绍算法思路沿袭前面BN提出的思路来讲。第一点，对每个特征进行独立的normalization。我们考虑一个batch的训练，传入m个训练样本，并关注网络中的某一层，忽略上标 ![[公式]](https://www.zhihu.com/equation?tex=l) 。

![[公式]](https://www.zhihu.com/equation?tex=Z%5Cin+%5Cmathbb%7BR%7D%5E%7Bd_l%5Ctimes+m%7D)

我们关注当前层的第 ![[公式]](https://www.zhihu.com/equation?tex=j) 个维度，也就是第 ![[公式]](https://www.zhihu.com/equation?tex=j) 个神经元结点，则有 ![[公式]](https://www.zhihu.com/equation?tex=Z_j%5Cin+%5Cmathbb%7BR%7D%5E%7B1%5Ctimes+m%7D) 。我们当前维度进行规范化：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_j%3D%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5Em+Z_j%5E%7B%28i%29%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E2_j%3D%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5Em%28Z_j%5E%7B%28i%29%7D-%5Cmu_j%29%5E2)

![[公式]](https://www.zhihu.com/equation?tex=%5Chat%7BZ%7D_j%3D%5Cfrac%7BZ_j-%5Cmu_j%7D%7B%5Csqrt%7B%5Csigma_j%5E2%2B%5Cepsilon%7D%7D)

> 其中 ![[公式]](https://www.zhihu.com/equation?tex=%5Cepsilon) 是为了防止方差为0产生无效计算。

![img](https://pic1.zhimg.com/80/v2-084e9875d10896369e09af5a60e56250_1440w.jpg)

![img](https://pic3.zhimg.com/80/v2-c37bda8f138402cc7c3dd62c509d36f6_1440w.jpg)

通过上面的变换，**我们解决了第一个问题，即用更加简化的方式来对数据进行规范化，使得第 ![[公式]](https://www.zhihu.com/equation?tex=l)层的输入每个特征的分布均值为0，方差为1。**

如同上面提到的，Normalization操作我们虽然缓解了ICS问题，让每一层网络的输入数据分布都变得稳定，但却导致了数据表达能力的缺失。也就是我们通过变换操作改变了原有数据的信息表达（representation ability of the network），使得底层网络学习到的参数信息丢失。

另一方面，通过让每一层的输入分布均值为0，方差为1，会使得输入在经过sigmoid或tanh激活函数时，容易陷入非线性激活函数的线性区域。

因此，BN又引入了两个可学习（learnable）的参数 ![[公式]](https://www.zhihu.com/equation?tex=%5Cgamma) 与 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbeta) 。

这两个参数的引入是**为了恢复数据本身的表达能力**，对规范化后的数据进行线性变换，即 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctilde%7BZ_j%7D%3D%5Cgamma_j+%5Chat%7BZ%7D_j%2B%5Cbeta_j) 。特别地，当 ![[公式]](https://www.zhihu.com/equation?tex=%5Cgamma%5E2%3D%5Csigma%5E2%2C%5Cbeta%3D%5Cmu) 时，可以实现等价变换（identity transform)并且保留了原始输入特征的分布信息。

**通过上面的步骤，我们就在一定程度上保证了输入数据的表达能力。**

以上就是整个Batch Normalization在模型训练中的算法和思路。

#### 计算公式

对于神经网络中的第 ![[公式]](https://www.zhihu.com/equation?tex=l) 层，我们有：

![[公式]](https://www.zhihu.com/equation?tex=Z%5E%7B%5Bl%5D%7D%3DW%5E%7B%5Bl%5D%7DA%5E%7B%5Bl-1%5D%7D%2Bb%5E%7B%5Bl%5D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu%3D%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5EmZ%5E%7B%5Bl%5D%28i%29%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E2%3D%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5Em%28Z%5E%7B%5Bl%5D%28i%29%7D-%5Cmu%29%5E2)

![[公式]](https://www.zhihu.com/equation?tex=%5Ctilde%7BZ%7D%5E%7B%5Bl%5D%7D%3D%5Cgamma%5Ccdot%5Cfrac%7BZ%5E%7B%5Bl%5D%7D-%5Cmu%7D%7B%5Csqrt%7B%5Csigma%5E2%2B%5Cepsilon%7D%7D%2B%5Cbeta)

![[公式]](https://www.zhihu.com/equation?tex=A%5E%7B%5Bl%5D%7D%3Dg%5E%7B%5Bl%5D%7D%28%5Ctilde%7BZ%7D%5E%7B%5Bl%5D%7D%29)

### 测试阶段使用BatchNormalization

利用BN训练好模型后，我们保留了每组mini-batch训练数据在网络中每一层的 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_%7Bbatch%7D) 与 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E2_%7Bbatch%7D)。此时我们使用整个样本的统计量来对Test数据进行归一化，具体来说使用均值与方差的无偏估计：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_%7Btest%7D%3D%5Cmathbb%7BE%7D+%28%5Cmu_%7Bbatch%7D%29)

![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E2_%7Btest%7D%3D%5Cfrac%7Bm%7D%7Bm-1%7D%5Cmathbb%7BE%7D%28%5Csigma%5E2_%7Bbatch%7D%29)

得到每个特征的均值与方差的无偏估计后，我们对test数据采用同样的normalization方法：

![[公式]](https://www.zhihu.com/equation?tex=BN%28X_%7Btest%7D%29%3D%5Cgamma%5Ccdot+%5Cfrac%7BX_%7Btest%7D-%5Cmu_%7Btest%7D%7D%7B%5Csqrt%7B%5Csigma%5E2_%7Btest%7D%2B%5Cepsilon%7D%7D%2B%5Cbeta)

### Batch Normalization的优势

Batch Normalization在实际工程中被证明了能够缓解神经网络难以训练的问题，BN具有的优势可以总结为以下三点：

**（1）BN使得网络中每层输入数据的分布相对稳定，加速模型学习速度**

BN通过规范化与线性变换使得每一层网络的输入数据的均值与方差都在一定范围内，使得后一层网络不必不断去适应底层网络中输入的变化，从而实现了网络中层与层之间的解耦，允许每一层进行独立学习，有利于提高整个神经网络的学习速度。

**（2）BN使得模型对网络中的参数不那么敏感，简化调参过程，使得网络学习更加稳定**

在神经网络中，我们经常会谨慎地采用一些权重初始化方法（例如Xavier）或者合适的学习率来保证网络稳定训练。

当学习率设置太高时，会使得参数更新步伐过大，容易出现震荡和不收敛。但是使用BN的网络将不会受到参数数值大小的影响。例如，我们对参数 ![[公式]](https://www.zhihu.com/equation?tex=W) 进行缩放得到 ![[公式]](https://www.zhihu.com/equation?tex=aW) 。对于缩放前的值 ![[公式]](https://www.zhihu.com/equation?tex=Wu) ，我们设其均值为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_1) ，方差为 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E2_1) ；对于缩放值 ![[公式]](https://www.zhihu.com/equation?tex=aWu) ，设其均值为 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_2) ，方差为 ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E2_2) ，则我们有：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_2%3Da%5Cmu_1) ， ![[公式]](https://www.zhihu.com/equation?tex=%5Csigma%5E2_2%3Da%5E2%5Csigma%5E2_1)

我们忽略 ![[公式]](https://www.zhihu.com/equation?tex=%5Cepsilon) ，则有：

![[公式]](https://www.zhihu.com/equation?tex=BN%28aWu%29%3D%5Cgamma%5Ccdot%5Cfrac%7BaWu-%5Cmu_2%7D%7B%5Csqrt%7B%5Csigma%5E2_2%7D%7D%2B%5Cbeta%3D%5Cgamma%5Ccdot%5Cfrac%7BaWu-a%5Cmu_1%7D%7B%5Csqrt%7Ba%5E2%5Csigma%5E2_1%7D%7D%2B%5Cbeta%3D%5Cgamma%5Ccdot%5Cfrac%7BWu-%5Cmu_1%7D%7B%5Csqrt%7B%5Csigma%5E2_1%7D%7D%2B%5Cbeta%3DBN%28Wu%29)

![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Cpartial%7BBN%28%28aW%29u%29%7D%7D%7B%5Cpartial%7Bu%7D%7D%3D%5Cgamma%5Ccdot%5Cfrac%7BaW%7D%7B%5Csqrt%7B%5Csigma%5E2_2%7D%7D%3D%5Cgamma%5Ccdot%5Cfrac%7BaW%7D%7B%5Csqrt%7Ba%5E2%5Csigma%5E2_1%7D%7D%3D%5Cfrac%7B%5Cpartial%7BBN%28Wu%29%7D%7D%7B%5Cpartial%7Bu%7D%7D)

![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Cpartial%7BBN%28%28aW%29u%29%7D%7D%7B%5Cpartial%7B%28aW%29%7D%7D%3D%5Cgamma%5Ccdot%5Cfrac%7Bu%7D%7B%5Csqrt%7B%5Csigma%5E2_2%7D%7D%3D%5Cgamma%5Ccdot%5Cfrac%7Bu%7D%7Ba%5Csqrt%7B%5Csigma%5E2_1%7D%7D%3D%5Cfrac%7B1%7D%7Ba%7D%5Ccdot%5Cfrac%7B%5Cpartial%7BBN%28Wu%29%7D%7D%7B%5Cpartial%7BW%7D%7D)

> 注：公式中的 ![[公式]](https://www.zhihu.com/equation?tex=u) 是当前层的输入，也是前一层的输出

我们可以看到，经过BN操作以后，权重的缩放值会被“抹去”，因此保证了输入数据分布稳定在一定范围内。另外，权重的缩放并不会影响到对 ![[公式]](https://www.zhihu.com/equation?tex=u) 的梯度计算；

当权重越大时，即 ![[公式]](https://www.zhihu.com/equation?tex=a) 越大， ![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B1%7D%7Ba%7D) 越小，意味着权重 ![[公式]](https://www.zhihu.com/equation?tex=W) 的梯度反而越小，这样BN就保证了梯度不会依赖于参数的scale，使得参数的更新处在更加稳定的状态。

因此，在使用Batch Normalization之后，抑制了参数微小变化随着网络层数加深被放大的问题，使得网络对参数大小的适应能力更强，此时我们可以设置较大的学习率而不用过于担心模型divergence的风险。

**（3）BN允许网络使用饱和性激活函数（例如sigmoid，tanh等），缓解梯度消失问题**

在不使用BN层的时候，由于网络的深度与复杂性，很容易使得底层网络变化累积到上层网络中，导致模型的训练很容易进入到激活函数的梯度饱和区；通过normalize操作可以让激活函数的输入数据落在梯度非饱和区，缓解梯度消失的问题；另外通过自适应学习 ![[公式]](https://www.zhihu.com/equation?tex=%5Cgamma) 与 ![[公式]](https://www.zhihu.com/equation?tex=%5Cbeta) 又让数据保留更多的原始信息。

**（4）BN具有一定的正则化效果**

在Batch Normalization中，由于我们使用mini-batch的均值与方差作为对整体训练样本均值与方差的估计，尽管每一个batch中的数据都是从总体样本中抽样得到，但不同mini-batch的均值与方差会有所不同，这就为网络的学习过程中增加了随机噪音，与Dropout通过关闭神经元给网络训练带来噪音类似，在一定程度上对模型起到了正则化的效果。

另外，原作者通过也证明了网络加入BN后，可以丢弃Dropout，模型也同样具有很好的泛化效果。