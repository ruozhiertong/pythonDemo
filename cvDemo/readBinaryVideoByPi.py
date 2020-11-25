#! encoding: UTF-8
import os
import numpy as np
import struct

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt # plt 用于显示图片


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


filepath = "badapple.bin"

document = open(filepath, "rb") #二进制读写.可以在Arduino的oled上直接使用

frameSize = int(64*128/8)


count = 0
r = 0
c = 0
size = os.path.getsize(filepath)  #获得文件大小

image = Image.new('1', (128, 64)) #创建一个图片

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

#二进制文件的结束，可以根据文件大小来判断是否读取结束。
for x in range(size):
    a = document.read(1) # each byte.
    a = struct.unpack('B', a)[0]
    for i in range(7,-1,-1):
        if(get_bit_val(a,i) == 1):
            draw.point((r,c%128), "#00FFFF")
        else:
            draw.point((r,c%128),"#FF0000")
        c = c+1
    if(c%128 == 0):
        r = r+1
    if(r == 64):
        r = 0
        c = 0
        #image.show()
        #plt.imshow(image)
        #plt.axis('off')
        #plt.show()
document.close()
