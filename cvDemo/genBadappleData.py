#! encoding: UTF-8
import os
import cv2

#生成用于oled显示的数据。图片，bin数据。


def set_bit_val(byte, index, val):
    """
    更改某个字节中某一位（Bit）的值

    :param byte: 准备更改的字节原值
    :param index: 待更改位的序号，从右向左0开始，0-7为一个完整字节的8个位
    :param val: 目标位预更改的值，0或1
    :returns: 返回更改后字节的值
    """
    if val:
        return byte | (1 << index)
    else:
        return byte & ~(1 << index)


OLED_WIDTH = 128
OLED_HEIGHT = 64

#video_full_path = "badapple128*64-1000.mp4"
video_full_path = "resource/badapple256*128-1000.mp4"
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
document = open("resource/badapple.bin", "wb");#二进制读写.可以在Arduino的oled上直接使用
a=0
idx_a=0
while(success):
    success, frame = cap.read()
    #image.shape[0]为rows
    #image.shape[1]为cols
    #image.shape[2]为channels
    #image.shape = (480,640,3)
    #print(frame.shape)
    if success:
        cv2.imshow('frame', frame)
        cv2.waitKey(1) 
        #resize
        frame=cv2.resize(frame,(OLED_WIDTH,OLED_HEIGHT),interpolation=cv2.INTER_AREA)
        cv2.imwrite("resource/badapple_" + str(frame_count)+ ".jpg", frame)  #生成图片。
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #ret,binary = cv2.threshold(gray,200,256,cv2.THRESH_BINARY)
        #print(type(binary))
        #print(binary)
        #cv2.imshow('binary', binary) 
        #cv2.waitKey(1) 

        #如果没有resize，还要手动抽样成128*64
        # for r in range(0, 128, 2):
        #     for c in range(0, 256, 2):
        #         if gray[r, c] > 200:
        #             a = set_bit_val(a,7 - idx_a,1)
        #             #document.write(0)
        #         else:
        #             a = set_bit_val(a,7 - idx_a,0)
        #             #document.write(1)
        #         #print(a)
        #         idx_a = idx_a + 1
        #         if(idx_a % 8 == 0):
        #             document.write(a.to_bytes(1,"big"))
        #             a=0
        #             idx_a=0

        for r in range(0, OLED_HEIGHT, 1):
            for c in range(0, OLED_WIDTH, 1):
                if gray[r, c] > 200:
                    a = set_bit_val(a,7 - idx_a,1)
                    #document.write(0)
                else:
                    a = set_bit_val(a,7 - idx_a,0)
                    #document.write(1)
                #print(a)
                idx_a = idx_a + 1
                if(idx_a % 8 == 0):
                    document.write(a.to_bytes(1,"big"))
                    a=0
                    idx_a=0
    frame_count = frame_count + 1
#print(frame_count)
cap.release()
document.close()
