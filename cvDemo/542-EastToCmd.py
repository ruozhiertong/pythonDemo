#! encoding: UTF-8
import os
import cv2
video_full_path = "541-badapple-256*128.mp4"
#video_full_path = "541-badapple.mp4"
cap = cv2.VideoCapture(video_full_path)
# 获取视频帧的宽
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# 获取视频帧的高
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 获取视频帧的帧率
fps = cap.get(cv2.CAP_PROP_FPS)
print(w)
print(h)
print(fps)
frame_count = 1
success = True
document = open("testfile.txt", "w+");
while(success):
    success, frame = cap.read() 
    #print(success)
    #print(frame.shape) # 查看图片矩阵形状.矩阵：（384，512，3） 分辨率，通道数。
    #t=[[0,0,0,0,0][1,1,1,1,1]]
    #t =  [[0 for col in range(5)] for row in range(6)]
    #print(t)
    #print(t[0][0])
    #print(frame)

    if  success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print(type(frame))
        # print(type(gray))
        # print(gray)
        s = ''
        #360*480
        # for r in range(0, 360, 6): #行 60 -> 40
        #     for c in range(0, 480, 4): #列 160 -> 120
        #         if gray[r, c] > 200:
        #             s += ' '
        #         else:
        #             s += '0'
        #     s += '\n'

        for r in range(0, 128, 4):
            for c in range(0, 256, 4):
                if gray[r, c] > 200:
                    s += ' '
                else:
                    s += '0'
            s += '\n'
        print(s)
        print('\033c',end='') #清屏
        #i = os.system("clear") #清屏
        document.write(s)
    params = []
    params.append(1)
    frame_count = frame_count + 1
cap.release()
document.close()
