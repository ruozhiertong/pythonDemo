#! encoding: UTF-8
import time  # 引入time模块
import showPicVideo

# 直接使用opencv 处理视频，在此基础上 直接显示图片，从而播放。

filepath = "resource/badapple.mp4"

def main():
    start = time.time()
    showPicVideo.process(filepath)
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()