#! encoding: UTF-8
import os
import cv2
import numpy as np
import struct


def get_bit_val(byte, index):
    """
    得到某个字节中某一位（Bit）的值

    :param byte: 待取值的字节值
    :param index: 待读取位的序号，从右向左0开始，0-7为一个完整字节的8个位
    :returns: 返回读取该位的值，0或1
    """
    if byte & (1 << index):
        return 1
    else:
        return 0


filepath = "badapple.bin";

document = open(filepath, "rb");#二进制读写.可以在Arduino的oled上直接使用

frameSize = int(64*128/8)

pic = np.zeros((64, 128))

# video = cv2.VideoCapture("street.mp4")
# fps = video.get(cv2.CAP_PROP_FPS)
# size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# opencv支持不同的编码格式
fourcc = cv2.VideoWriter_fourcc(*'X264')
video_writer = cv2.VideoWriter('outputVideo.mp4', fourcc , 20.0, (128,64),False)


count = 0
r = 0
c = 0
size = os.path.getsize(filepath) #获得文件大小

#二进制文件的结束，可以根据文件大小来判断是否读取结束。
for x in range(size):
    a = document.read(1) # each byte.
    a = struct.unpack('B', a)[0]
    #print(a)
    #print(type(a))
    
    for i in range(7,-1,-1):
        if(get_bit_val(a,i) == 1):
            pic[r][c%128] = 255
        else:
            pic[r][c%128] = 0
        c = c+1
    if(c%128 == 0):
        r = r+1
    if(r == 64):
        r = 0
        c = 0
        video_writer.write(pic)
        cv2.imshow('binary', pic) 
        cv2.waitKey(1)


print("done")
video_writer.release()
document.close()
