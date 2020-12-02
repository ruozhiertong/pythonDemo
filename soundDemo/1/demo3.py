import matplotlib.pyplot as plt
import librosa.display
import numpy as np
from pydub import AudioSegment

# 1秒=1000毫秒
SECOND = 1000
# 音乐文件
AUDIO_PATH = 'Fenn.mp3'
def split_music(begin, end, filepath):

	# 导入音乐
	song = AudioSegment.from_mp3(filepath)

	# 取begin秒到end秒间的片段
	song = song[begin*SECOND: end*SECOND]

	# 存储为临时文件做备份
	temp_path = 'backup/'+filepath
	song.export(temp_path)

	return temp_path
 
music, sr = librosa.load(split_music(0, 1, AUDIO_PATH))

# 放大
n0 = 9000
n1 = 10000
 
music = np.array([mic for mic in music if mic > 0])
plt.figure(figsize=(14, 5))
plt.plot(music[n0:n1])
plt.grid()
 
# 显示图
plt.show()