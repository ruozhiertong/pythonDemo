import numpy as np
import pyaudio
from pydub import AudioSegment, effects
import matplotlib.pyplot as plt
from PIL import Image
# import sys
# sys.path.append("..")
# # import ../cvDemo    # wrong
# # import cvDemo／showPicOnPi # wrong
# # from cvDemo import showPicOnPi
# import cvDemo.showPicOnPi as showPicOnPi
#
# pICShow = showPicOnPi.PICShow()



p = pyaudio.PyAudio()
sound = AudioSegment.from_file(file='../2/1.wav')
left = sound.split_to_mono()[0] # 单身道。 mono单声道。
fs = left.frame_rate
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
fig = plt.figure(facecolor='black')
ax2 = fig.subplots()
#ax1.set_ylim(0, 0.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_axis_off()

window = int(0.2*fs) # 0.2 较为流畅。
f = np.linspace(20, 20*1000, window // 2)
t = np.linspace(0, 20, window)
lf2, = ax2.plot(t, np.zeros(window), lw=1)


frames = 0
while stream.is_active():
    slice = left.get_sample_slice(frames, frames + window)
    data = slice.raw_data
    stream.write(data)
    y = np.array(slice.get_array_of_samples()) / 30000 # 归一化
    yft = np.abs(np.fft.fft(y)) / (window // 2)
 
    lf2.set_ydata(y*1.5) # 幅度调大

    fig.canvas.draw()
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    # 重构成w h 4(argb)图像
    buf.shape = (w, h, 4)
    # 转换为 RGBA
    buf = np.roll(buf, 3, axis=2)
    # 得到 Image RGBA图像对象 (需要Image对象的同学到此为止就可以了)
    image = Image.frombytes("RGBA", (w, h), buf.tostring())
    image = image.resize((128, 64),Image.ANTIALIAS)
    image.show()
    #pICShow.showViaImage(image)

    frames +=window

