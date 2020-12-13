# coding=utf-8

# Another way to do it without clearing the Axis
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

plt.plot([], [], label='Channel 1')
plt.plot([], [], label='Channel 2')


def animate(i):
    data = pd.read_csv('data_6.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    # plt对象的get current axex方法, 返回当前绘制对象的axes轴(也相当于一个plt,它有plt对象几乎所有方法,可以直接像plt对象一样使用它)
    ax = plt.gca()
    # 获得当前绘制的两条曲线对象
    line1, line2 = ax.lines
    # 分别给两条曲线设置其对应的数据(动态刷新)
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    # 分别求出两条曲线在x,y方向上的最小值和最大值
    xlim_low, xlim_high = ax.get_xlim()
    ylim_low, ylim_high = ax.get_ylim()
    # 重新设置当前最小的x和最大的x(沿着横轴最左端和最右端的数据)--> 横轴最左端(起点)不动,而将横轴最右端的数据增加5也就是实现动态向后移动
    ax.set_xlim(xlim_low, (x.max() + 5))
    # 获得动态生成数据集数据的当前最大值
    y1max = y1.max()
    y2max = y2.max()
    # 用一个临时变量保存动态生成数据集两列下所有数据的最大值
    current_ymax = y1max if (y1max > y2max) else y2max
    # 获得动态生成数据集数据的当前最小值
    y1min = y1.min()
    y2min = y2.min()
    # 用一个临时变量保存动态生成数据集两列下所有数据的最小值
    current_ymin = y1min if (y1min < y2min) else y2min
    # 重新设置当前最小的y和最大的y(沿着竖轴最下端和最上端的数据)--> 分别将竖轴最下端的数据和最上端的数据设置成动态数据集中当前最大的数据+5和最小的数据-5(有点难理解....)
    ax.set_ylim((current_ymin - 5), (current_ymax + 5))


# FuncAnimation方法可以在间隔interval时间(ms)后重复运行某个函数(该函数必须要有一个参数,表示的是当前运行该函数第几次了)
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.legend()
plt.tight_layout()
plt.show()
