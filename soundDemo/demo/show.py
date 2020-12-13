# coding=utf-8

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#学习 plt绘图： https://zhuanlan.zhihu.com/p/93423829
#  https://www.jianshu.com/p/88238e34c689


#plt整个图表。可以包含多个fig。
#fig 图表。每个fig中包含一套坐标系 axes。
#每个坐标系可以包含多个axis坐标轴。
#具体画图 可以 plt，fig， 可以axes。前两个都是在当前工作的axes中绘制。 axes是在具体哪个axes中绘图。

plt.style.use('fivethirtyeight')
fig = plt.figure() #图表／画布。 指定最多2个subplot。
ax1, ax2 = fig.subplots(2, 1) #生成2*1子图表


# 利用itertools里的count创建一个迭代器对象,默认从0开始计数, 是一个"无限大"的等差数列
index = count()
x_vals = []
y_vals = []


def animate(i):
    print(i)
    # i表示的是经历过的"时间", 即每调用一次animate函数, i的值会自动加一
    # 我们从一个动态生成数据的csv文件中获取数据来模拟动态数据
    data = pd.read_csv('data_6.csv')
    # 获得该动态数据的所有列的所有数据(当前生成的), 到下一次运行时该数据如果变动了, 绘出来的图形自然也变动了
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    # plt对象的cla方法: clear axes: 清除当前轴线(前面说过axes对象表示的是plt整个figure对象下面的一个绘图对象, 一个figure可以有多个axes, 其实就是当前正在绘图的实例).
    # 我们可以不清除当前的axes而沿用前面的axes, 但这样会产生每次绘出来的图形都有很大的变化(原因是重新绘制的时候,颜色,坐标等都重新绘制,可能不在同一个地方了,所以看上去会时刻变化).
    # 因此必须要清除当前axes对象,来重新绘制.
    plt.subplot(211)
    plt.
    plt.cla()
    #plt.clf()
    plt.title("ax1")
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.legend(loc='upper left')
    plt.subplot(212)
    plt.cla()
    plt.title("ax2")
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()


# FuncAnimation可以根据给定的interval(时间间隔, ms为单位)一直重复调用某个函数来进行绘制, 从而模拟出实时数据的效果.
# animate后的参数作为animate函数的参数传入。
ani = FuncAnimation(fig, animate,frames=range(0, 1000, 50), interval=1000)

plt.show()