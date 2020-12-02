import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from _tkinter import TclError
from pydub import AudioSegment
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
 

# ref:https://www.cnblogs.com/darkchii/p/11827461.html
 
p = pyaudio.PyAudio()
sound = AudioSegment.from_file(file='../1/Fenn.mp3')
left = sound.split_to_mono()[0]
fs = left.frame_rate
size = len(left.get_array_of_samples())
channels = left.channels
stream = p.open(
    format=p.get_format_from_width(left.sample_width,),
    channels=1,
    rate=int(fs*1.2),  # 调整播放速率
    # input=True,
    output=True,
)
stream.start_stream()
fig = plt.figure()
ax = fig.gca(
    # projection='polar'
)
norm2 = plt.Normalize(-1., 1.)
lc = LineCollection([], cmap='gist_ncar', norm=norm2)
ax.set_ylim(-1.5, 1.5)
ax.set_axis_off()
window = int(0.02*fs)
time = np.linspace(0, 20, window)  # time 控制曲线平滑程度
ax.add_collection(lc)
 
 
def update(frames):
    if stream.is_active():
        slice = left.get_sample_slice(frames, frames + window)
        stream.write(slice.raw_data)
        y = np.array(slice.get_array_of_samples()) / 30000
        points = np.array([time, y]).T.reshape(-1, 1, 2)  # 可以使用三角函数来实现多重曲线重叠效果，y 控制曲线振幅
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lc.set_segments(segments)
        lc.set_array(y)  # 控制指定的 colormap 的颜色渐变
 
    return lc,
 
 
ani = FuncAnimation(fig, update, frames=range(0, size, window), interval=0, blit=True)
plt.show()