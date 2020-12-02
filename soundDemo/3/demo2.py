import numpy as np
import pyaudio
from pydub import AudioSegment, effects
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
 
p = pyaudio.PyAudio()
sound = AudioSegment.from_file(file='../1/Fenn.mp3')
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
ax1, ax2 = fig.subplots(2, 1)


ax1.set_ylim(0, 0.5)
ax2.set_ylim(-15, 15)
ax1.set_axis_off()
ax2.set_axis_off()
window = int(0.02*fs) # 20ms
f = np.linspace(20, 20*1000, window // 2)
t = np.linspace(0, 20, window)
lf1, = ax1.plot(f, np.zeros(window // 2), lw=1)
lf2, = ax2.plot(t, np.zeros(window), lw=1)
 
 
def update(frames):
    if stream.is_active():
        print(time.time())
        slice = left.get_sample_slice(frames, frames + window)
        data = slice.raw_data
        stream.write(data)
        y = np.array(slice.get_array_of_samples()) / 30000 # 归一化
        yft = np.abs(np.fft.fft(y)) / (window // 2)
 
        lf1.set_ydata(yft[:window // 2])
        lf2.set_ydata(y)


    return lf1, lf2,
 
 
ani = FuncAnimation(fig, update, frames=range(0, size, window), interval=0, blit=True)
plt.show()