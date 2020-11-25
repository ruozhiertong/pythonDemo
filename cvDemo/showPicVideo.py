#! encoding: UTF-8
import os
import cv2

video_full_path = "badapple256*128-1000.mp4"
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
frame_count = 0
success = True
while(success):
    success, frame = cap.read()
    cv2.imshow('frame', frame) 
    cv2.waitKey(1) 
    frame_count = frame_count + 1
#print(frame_count)
cap.release()