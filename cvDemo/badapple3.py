#! encoding: UTF-8
import os
import numpy as np
import struct

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time  # 引入time模块
import cv2
import Adafruit_SSD1306


# 直接使用opencv 处理视频，在此基础上 直接显示图片，从而播放。


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

filepath = "resource/badapple.mp4"

def process():
    cap = cv2.VideoCapture(filepath)
    #处理每一帧
    while(True):
        success, frame = cap.read()
        if success == False:
            break
        #resize
        frame=cv2.resize(frame,(width,height),interpolation=cv2.INTER_AREA)
        #灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #二值化
        ret,picImage = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        picImage = Image.fromarray(picImage,"1")
        disp.image(picImage)
        disp.display()
    cap.release()


def main():
    start = time.time()
    process()
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()