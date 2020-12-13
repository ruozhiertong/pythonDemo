import numpy as np
import pyaudio
from pydub import AudioSegment, effects
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# ref: https://www.cnblogs.com/darkchii/p/11827461.html

p = pyaudio.PyAudio()
sound = AudioSegment.from_file(file='../1/Fenn.mp3')
left = sound.split_to_mono()[0] # 单身道。 mono单声道。
fs = left.frame_rate
size = len(left.get_array_of_samples())
#时长： size/fs  ==>秒
channels = left.channels
print(left)
print(fs)
print(size)
print(channels)
stream = p.open(
    format=p.get_format_from_width(left.sample_width,),
    channels=channels,
    rate=fs,
    # input=True,
    output=True,
)

stream.start_stream()
fig = plt.figure()
ax1, ax2 = fig.subplots(2, 1)

# ax1.set_ylim(0, 2)
ax1.set_axis_off()
# ax2.set_ylim(-15, 15)
ax2.set_axis_off()

time_spacing = 0.02
window = int(time_spacing*fs) # 20ms

t = np.linspace(0, time_spacing, window) #采样。 0.02秒采样window个点。 以left.frame_rate频率采样。

f = np.fft.fftfreq(t.size,t[1]-t[0]) #这里频率范围是left.frame_rate
#f = np.linspace(0, 2000, window)

#音乐波形图。
lf1, = ax1.plot(t, np.zeros(window))
# lf1, = ax1.plot([], [])
ax1.title.set_text('ax1')

#频谱图
lf2, = ax2.plot(f[:f.size//2], np.zeros(window//2))
# lf2, = ax1.plot([],[])
ax2.title.set_text('ax2')

def update(frames):
    if stream.is_active():
        #print(time.time())
        slice = left.get_sample_slice(frames, frames + window)
        data = slice.raw_data
        stream.write(data)  # 播放流
        # 这里为什么要归一化？？
        y = np.array(slice.get_array_of_samples()) #/ 10000 # 归一化 可调整。 时域
        # print(len(y))
        yft = np.fft.fft(y) #傅立叶变换。 频域。
        mag = np.abs(yft) * 2 / window  # 振幅
        #print(len(yft))
        #time.sleep(3)
        #ax1.plot(t, y)
        #ax2.plot(f[:f.size // 2], mag[:window//2])
        ax1.set_ylim(y.min(), y.max())
        lf1.set_ydata(y)

        ax2.set_ylim(mag[:window // 2].min(), mag[:window // 2].max())
        #TOOD 为什么在下面的axes会在axes最上面有残留一条线？？？
        lf2.set_ydata(mag[:window // 2])
        # print(y.min())
        # print(y.max())
        # print(mag.min())
        # print(mag.max())

        return lf1, lf2,

        # 因为下面效率不高，声音播放卡顿。
        # #plt.clf()
        # #plt.subplot(211)
        # plt.sca(ax1)
        # plt.cla()
        # # ax1.set_ylim(0, 2)
        # # ax1.set_axis_off()
        # plt.title("ax1")
        # plt.plot(f[:f.size//2], mag[:window//2], label='Channel 1')
        #
        # #plt.subplot(212)
        # plt.sca(ax2)
        # plt.cla()
        # # ax2.set_ylim(-15, 15)
        # # ax2.set_axis_off()
        # plt.title("ax2")
        # plt.plot(t, y, label='Channel 2')



ani = FuncAnimation(fig, update, frames=range(0, size, window), interval=1, blit=True)
plt.show()


# import scipy.io.wavfile as wf
#
# # 读取音频文件
# sample_rate, noised_sigs = wf.read('../2/1.wav')
# print(sample_rate)  # sample_rate：采样率44100
# print(noised_sigs.shape)    # noised_sigs:存储音频中每个采样点的采样位移(220500,)
# print(noised_sigs.size/noised_sigs.shape[1])
# times = np.arange(noised_sigs.size/noised_sigs.shape[1]) / sample_rate
#
# plt.figure('Filter')
# plt.subplot(221)
# plt.title('Time Domain', fontsize=16)
# plt.ylabel('Signal', fontsize=12)
# plt.tick_params(labelsize=10)
# plt.grid(linestyle=':')
# plt.plot(times[:500], noised_sigs[:500], c='orangered', label='Noised')
# plt.show()