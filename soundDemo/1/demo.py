import matplotlib.pyplot as plt
import librosa.display
 

# ref : https://zhuanlan.zhihu.com/p/127894008

# 音乐文件载入
audio_path = 'Fenn.mp3'
music, sr = librosa.load(audio_path)
 
# 宽高比为14:5的图
plt.figure(figsize=(14, 5))
librosa.display.waveplot(music, sr=sr)
 
# 显示图
plt.show()