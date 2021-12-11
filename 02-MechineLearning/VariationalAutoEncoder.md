# Variational AutoEncoder

我这几天比较好奇VAE模型和简单AE之间的区别，就是为什么要引入$/mu$和$sigma$，看了一上午，似懂非懂。

## AutoEncoder

### Encoder
Produce the new features representation from the old features representation, from the initial space to latent space, as dimensionality reduction. 
Aim: **keep the maximum of information when encoding**

### Decoder

Decompress the latent vector back to the initial space, and recover more information as far as possioble. 
Aim: **keep the minimum of reconstruction error when decoding**


At each iteration, the loss function could be illustrated as

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12smkasdj60z20j6jsh02.jpg)

Indeed, if our encoder and decoder have enough degrees of freedom, we can reduce any initial dimensionality to $1~N$ with a small loss.

We should however keep two things in mind:

1. An important dimensionality reduction with no reconstrction loss often comes with a price: the lack of regularity in the latent space. ( dimension 1 )
2. Most of the time the final purpose of dimensionality reduction is not to only reduce the number of dimensions of the data but to **reduce this number of dimensions while keeping the major part of the data structure information in the reduced representations**.

For these two reasons, the dimension of the latent space and the “depth” of autoencoders (that define degree and quality of compression) have to be carefully controlled and adjusted depending on the final purpose of the dimensionality reduction.

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12svzy46j61ef0jydhc02.jpg)


### Limitations

If the latent space is regular enough, we could take a point randomly from that latent space and decode it to get a new content we may need. The decoder would then act more or less like the generator of GAN.

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12t4npt4j612l0k30tx02.jpg)

The quality and relevance of generated content depend on the regularity of the latent space. But actually it is difficult to ensure that the encoder will organize the latent space to keep its regularity for autoencoder.

From the image as follow, it illustrates that a good model aims to find a correct mapping from the datasets distribution to the source distribution, in other words, it likes a brige between distributions. 

![](https://tva1.sinaimg.cn/large/008i3skNly1gu0y8zpjx8j60or0c775702.jpg)

我卡住了，用中文吧：

这个模型能够将原来的概率分布映射到训练集的概率分布，也就是说，**它们的目的都是进行分布之间的变换**。生成模型的难题就是判断生成分布与真实分布的相似度。如果两者无法尽可能拟合，将导致生成分布sample出来的随机变量无法生成出合适的结果。

overfitting也是表现之一，即生成分布与真实分布相似度太低了。

The high degree of freedom of the autoencoder that makes possible to encode and decode with no infomation loss leads to a severe **overfitting**, implying that some points of the latent space will give meaningless content once decoded. Irregular latent space prevent us from using autoencoder for new content generation.

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12ti5wznj61e40gojsv02.jpg)

**the autoencoder is solely trained to encode and decode with as few loss as possible, no matter how the latent space is organised.** Thus, if we are not careful about the definition of the architecture, it is natural that, during the training, the network takes advantage of any overfitting possibilities to achieve its task as well as it can…


## Variational autoencoder

To overcome the aforementioned drawbacks, we have to be sure that the latent space is regular enough.

### Definition

**A variational autoencoder can be defined as being an autoencoder whose training is regularised to avoid overfitting and ensure that the latent space has good properties that enable generative process**.

In order to introduce some regularisation of the latent space, instead of encoding an input as a single point, **we encode it as a distribution over the latent space**!!!!

The model is trained as follows:
1. The input is encoded as distribution over the latent space
2. A point from the latent space is sampled from that distribution
3. The sampled point is decoded and the reconstruction error can be computed
4. The reconstruction error is backpropageted through the network

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12tphkgmj61e40gk0tq02.jpg)

The distribution returned by the encoder are enforced to be close to a standard normal distribution so as the latent space regularisation.


### Loss function

The loss function is composed of a "reconstrucion term" and a "regularisation term", the later item which tends to regularise the organisation of the latent space by making the distributions returned by the encoder close to a standard normal distribution, is expressed by KLD loss.

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12uaw5f6j612w0iw3zq02.jpg)


### About regularisation

The regularity that is expected from the latent space in order to make generative process possible can be expressed through two main properties: 
1. **continuity** (two close points in the latent space should not give two completely different contents once decoded)
3. **completeness** (for a chosen distribution, a point sampled from the latent space should give “meaningful” content once decoded).

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12uid1jpj61fz0izta702.jpg)

The only fact that VAEs encode inputs as distributions instead of simple points is not sufficient to ensure continuity and completeness. Without a well defined regularisation term, the model can learn, in order to minimise its reconstruction error, **to “ignore” the fact that distributions are returned and behave almost like classic autoencoders** (leading to overfitting). To do so, the encoder can either return distributions with tiny variances (that would tend to be punctual distributions) or return distributions with very different means (that would then be really far apart from each other in the latent space). In both cases, distributions are used the wrong way (cancelling the expected benefit) and continuity and/or completeness are not satisfied.

So, in order to avoid these effects **we have to regularise both the covariance matrix and the mean of the distributions returned by the encoder**. In practice, this regularisation is done by enforcing distributions to be close to a standard normal distribution (centred and reduced). This way, we require the covariance matrices to be close to the identity, preventing punctual distributions, and the mean to be close to 0, preventing encoded distributions to be too far apart from each others.

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12uu15pnj61fz0izq3u02.jpg)


We can observe that continuity and completeness obtained with regularisation **tend to create a “gradient” over the information encoded in the latent space**. For example, a point of the latent space that would be halfway between the means of two encoded distributions coming from different training data should be decoded in something that is somewhere between the data that gave the first distribution and the data that gave the second distribution as it may be sampled by the autoencoder in both cases.

![](https://tva1.sinaimg.cn/large/008i3skNly1gu12zaueibj60z60izwf102.jpg)


## References
1. https://zhuanlan.zhihu.com/p/34998569
2. https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73
3. https://zhuanlan.zhihu.com/p/27549418