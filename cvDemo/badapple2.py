#! encoding: UTF-8
import os
import numpy as np
import struct

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#import matplotlib.pyplot as plt # plt 用于显示图片

import time  # 引入time模块


import Adafruit_SSD1306


#利用bin数据来显示图片，从而播放。好处，快，同时占用空间小。


# from PIL import Image
# import numpy as np
# im = Image.open('badapple_62.jpg')
# a = np.asarray(im)
# im = im.convert("1")
# b = np.asarray(im)
# print(type(a))
# print(a)
# pic = np.zeros((64,128,3))
# print(type(pic))
# print(pic)

#Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width #128
height = disp.height #64
image = Image.new('1', (width, height)) #创建一个图片
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

filepath = "resource/badapple.bin"



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
    
def process_bin():
    document = open(filepath, "rb") #二进制读写.可以在Arduino的oled上直接使用
    size = os.path.getsize(filepath)  #获得文件大小
    count = 0
    r = 0
    c = 0
    #二进制文件的结束，可以根据文件大小来判断是否读取结束。
    for x in range(size):
        a = document.read(1) # each byte.
        a = struct.unpack('B', a)[0]
        for i in range(7,-1,-1):
            if(get_bit_val(a,i) == 1):
                #这样进行draw.point 太慢，调用太多次。
                draw.point((c%128,r), "#FFFFFF")
            else:
                draw.point((c%128,r),"#000000")
            c = c+1
        if(c%width == 0):
            r = r+1
        if(r == height):
            r = 0
            c = 0
            #image.show()
            #plt.imshow(image)
            #plt.axis('off')
            #plt.show()
            # Display image.
            disp.image(image)
            disp.display()
    document.close()


#不知道为什么显示混乱
def process_bin2():
    pic = np.zeros((height,width))
    document = open(filepath, "rb") #二进制读写.可以在Arduino的oled上直接使用
    size = os.path.getsize(filepath)  #获得文件大小
    r = 0
    c = 0
    #二进制文件的结束，可以根据文件大小来判断是否读取结束。
    for x in range(size):
        a = document.read(1) # each byte.
        a = struct.unpack('B', a)[0]
        dataTable += a.to_bytes(1,'big')
        for i in range(7,-1,-1):
            if(get_bit_val(a,i) == 1):
                pic[r][c%width] = 255
            else:
                pic[r][c%width] = 0
            c = c + 1
        if(c%width == 0):
            r = r+1
        if(r == height):
            r = 0
            c = 0
            picImage = Image.fromarray(pic,"1")
            #picImage.show()
            disp.image(picImage)
            disp.display()
    document.close()


#这个速度更快了。比直接载入img显示更快
def process_bin3():
    pic = np.zeros((height,width))
    document = open(filepath, "rb") #二进制读写.可以在Arduino的oled上直接使用
    size = os.path.getsize(filepath)  #获得文件大小
    r = 0
    c = 0

    frameSize = int(height*width/8)
    for i in range(0,size,frameSize):
        a = document.read(frameSize)
        tImg = Image.frombytes("1",(width,height),a)
        disp.image(tImg)
        disp.display()
    # dataTable=bytes()
    # #二进制文件的结束，可以根据文件大小来判断是否读取结束。
    # for x in range(size):
    #     a = document.read(1) # each byte.
    #     a = struct.unpack('B', a)[0]
    #     dataTable += a.to_bytes(1,'big')
    #     if((x+1) % int(height*width/8) == 0):
    #         tImg = Image.frombytes("1",(width,height),dataTable)
    #         dataTable=bytes()
    #         #tImg.show()
    #         #picImage.show()
    #         disp.image(tImg)
    #         disp.display()
    document.close()

def main():
    start = time.time()
    #process_bin()
    #process_bin2()
    process_bin3()
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()