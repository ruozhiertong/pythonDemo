import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt

# ref: https://blog.csdn.net/ouening/article/details/71079535
#   https://www.cnblogs.com/LXP-Never/p/11558302.html


# example1
# Fs = 1000;            # Sampling frequency
# T = 1/Fs;             # Sampling period
# L = 1000;             # Length of signal
# #t = (0:L-1)*T;        # Time vector
# t=np.linspace(0,(L-1),L)
#
# S = 0.2+0.7*np.cos(2*np.pi*50*t+20/180*np.pi) + 0.2*np.cos(2*np.pi*100*t+70/180*np.pi) ;
# plt.plot(t[1:50],S[1:50])
# plt.title('Signal Corrupted with Zero-Mean Random Noise')
# plt.xlabel('t (milliseconds)')
# plt.ylabel('X(t)')
# plt.show()


#采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
x=np.linspace(0,1,2800)

#设置需要采样的信号，频率分量有180，390和600
y=7*np.sin(2*np.pi*180*x) + 2.8*np.sin(2*np.pi*390*x)+5.1*np.sin(2*np.pi*600*x)
#y = np.sin(2*np.pi*x)

plt.subplot(221)
plt.title('Original wave')
plt.plot(x[0:50],y[0:50])


xf = np.arange(len(y))        # 频率 [0,len(y)) 间隔1
yf=abs(fft(y))                # 取绝对值
# yf = fft(y) #  不取绝对值 看看


plt.subplot(222)
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表
plt.plot(xf,yf,'r')


yy=fft(y)                     #快速傅里叶变换
yreal = yy.real               # 获取实数部分
yimag = yy.imag               # 获取虚数部分

yf1=abs(fft(y))/len(x)           #归一化处理
yf2 = yf1[range(int(len(x)/2))]  #由于对称性，只取一半区间

xf1 = xf
xf2 = xf[range(int(len(x)/2))]  #取一半区间

plt.subplot(223)
plt.title('FFT of Mixed wave(normalization)',fontsize=9,color='r')
plt.plot(xf1,yf1,'g')

plt.subplot(224)
plt.title('FFT of Mixed wave)',fontsize=10,color='#F08080')
plt.plot(xf2,yf2,'b')


plt.show()