0.vscode 对于打开一个目录，作为一个工程。 会在目录下建一个.vscode的目录，作为其工程的配置。
1.https://www.cnblogs.com/Dy1an/p/10130518.html
https://blog.csdn.net/gsls200808/article/details/51222986
https://www.cnblogs.com/DesignerA/p/11604200.html
2.numpy https://github.com/numpy/numpy/tree/master/numpy
3.要想完成切片操作，要实现_getItem__.
4.TODO 如何查看numpy源码。 其中关于defcharacter.py中 定义了 def array()。 __getitem__ 调用的ndarray.getitem。 问题是没法跳到ndarray，就无法知道getitem的实现。 也无法查看python中list dictionary的源码。 其实我就想知道这些数据结构的[]索引的底层原理，想看看是底层getItem是如何实现的。大概知道[]中索引的类型要求会在getitem方法中做判断，主要是想通过源码验证一下。但是就是死活找不到numpy中ndarray getitem的方法，如果知道，那么就可以分析 numpy array的索引 切片的操作。 一般[]中的类型可以是int slice类型。 一些三方库中的数据有时候也可以有tuple类型。


4.pip3 安装的 路径在 /usr/local/lib/python3.7/site-packages/numpy
