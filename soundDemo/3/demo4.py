import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack


FS = 1000 #采样频率 理论上2倍于最高分量频率就好，不过五到十倍比较好。    采样频率fs是100，也就是说在一秒内你采样了100个点。
# sample spacing
T = 1.0 / FS  #采样间隔。 采样周期。
# Number of sample points
N = 4 *FS #采样数。 选取的采样点数N 最好应为采样频率fs 的正整数倍。
#N =500

#N点采样。
#以FS频率进行采样。 FFT后的频率是以FS来决定的。
x = np.linspace(0.0, N/FS, N) #在(0,x)这里即2s上 N个采样。  频率是FS。  N/FS或 N*T. 相当于在2秒内做采样，采样N个点。频率为N／2 ==》 FS
y = np.sin(50.0 * 2.0*np.pi*x + 40)+ 0.5*np.sin(80.0 * 2.0*np.pi*x) # fft后没有体现相位40。


plt.subplot(211) # 先指定在哪个图像中绘制
plt.title('origin wave',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表
plt.plot(x,y,'r')

yf = scipy.fftpack.fft(y) #快速傅立叶变换
#xf = x*FS #样本的 频率序列。 因为N和FS是倍数关系，不能直接通过这样来获取频率序列(除非N=FS)，因为这样会导致频率成倍数关系。
# 得到分解波的频率序列. 和采样的FS有关
# xf = scipy.fftpack.fftfreq(x.size, x[1] - x[0])
xf = np.linspace(0, FS, N) # 也可以！！
mag = np.abs(yf)*2/N # 振幅


#fig, ax = plt.subplots()
# 由于对称性，只取一半区间
#ax.plot(xf[:N//2], 2.0/N * np.abs(yf[:N//2])) # 2.0/N * np.abs(yf[:N//2]) 幅度值

plt.subplot(212)
plt.title('fft ',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表
plt.plot(xf[:N//2],mag[:N//2],'g')
plt.show()