import numpy as np
import pyaudio
from pydub import AudioSegment, effects
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from PIL import Image
import sys
sys.path.append("../../")
# import ../cvDemo    # wrong
# import cvDemo／showPicOnPi # wrong
from cvDemo import showPicOnPi
import cvDemo.showPicOnPi as showPicOnPi

pICShow = showPicOnPi.PICShow()

# 这里只是显示音频的信号图像，不是做频谱图。所以不需要做傅立叶变换。 音乐波形图。


p = pyaudio.PyAudio()
sound = AudioSegment.from_file(file='../1/Fenn.mp3')
left = sound.split_to_mono()[0] # 单身道。 mono单声道。
fs = left.frame_rate #帧率。 一秒多少帧。
size = len(left.get_array_of_samples())
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
ax1,ax2 = fig.subplots(2,1)
# ax1.set_axis_off()

time_spacing = 0.02
window = int(time_spacing*fs) # 0.2 较为流畅。取200ms。
t = np.linspace(0, time_spacing, window) # 200ms
lf1, = ax1.plot(t, np.zeros(window), lw=1)
f = np.linspace(0, fs, window)
lf2, = ax2.plot(f[:window//2], np.zeros(window//2), lw=1)


frames = 0
while stream.is_active():
    slice = left.get_sample_slice(frames, frames + window)
    data = slice.raw_data
    stream.write(data)
    y = np.array(slice.get_array_of_samples())
    ax1.set_ylim(y.min(),y.max())
    lf1.set_ydata(y)

    yft = np.fft.fft(y)  # 傅立叶变换。 频域。
    mag = np.abs(yft) * 2 / window  # 振幅
    ax2.set_ylim(mag.min(),mag.max())
    lf2.set_ydata(mag[:window//2])

    fig.canvas.draw()
    #plt.show()
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    # 重构成w h 4(argb)图像
    buf.shape = (w, h, 4)
    # 转换为 RGBA
    buf = np.roll(buf, 3, axis=2)
    # 得到 Image RGBA图像对象 (需要Image对象的同学到此为止就可以了)
    image = Image.frombytes("RGBA", (w, h), buf.tostring())
    image = image.resize((128, 64),Image.ANTIALIAS)
    #image.show()
    pICShow.showViaImage(image)
    frames +=window


# def update(frames):
#     if stream.is_active():
#         slice = left.get_sample_slice(frames, frames + window)
#         data = slice.raw_data
#         stream.write(data)  # 播放流
#         y = np.array(slice.get_array_of_samples())
#         ax1.set_ylim(y.min(),y.max())
#         lf1.set_ydata(y)
#
#     return lf1,
#
#
# ani = FuncAnimation(fig, update, frames=range(0, size, window), interval=1, blit=True)
# plt.show()