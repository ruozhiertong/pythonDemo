#! encoding: UTF-8
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cv2
import time  # 引入time模块
import Adafruit_SSD1306


class OLEDPlayer(object):


    def __initSSD1306__(self):
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
        w = disp.width #128
        h = disp.height #64
        # image = Image.new('1', (width, height)) #创建一个图片
        # Get drawing object to draw on image.
        # draw = ImageDraw.Draw(image)
        return disp
    
    """docstring for OLEDPlayer"""
    def __init__(self):
        self.disp = self.__initSSD1306__()

    def play(self,filepath,width = 0, height =0, x =0, y =0):
        if(width == 0):
            width = self.disp.width
        if(height == 0):
            self.height = self.disp.height


        cap = cv2.VideoCapture(filepath)
        #处理每一帧
        while(True):
            success, frame = cap.read()
            if success == False:
                break
            #resize
            frame=cv2.resize(frame,(width,height),interpolation=cv2.INTER_AREA)
            #print(type(frame)) #<class 'numpy.ndarray'>
            
            #灰度
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # print(type(gray)) #<class 'numpy.ndarray'>
            # cv2.imshow('gray', gray) 
            # cv2.waitKey(1)

            #二值化. 其实和gray差不多，只是不是灰度，值是0，或 255， 白或黑
            # ret,picImage = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
            # print(type(picImage)) #<class 'numpy.ndarray'>
            # cv2.imshow('binary', picImage) 
            # cv2.waitKey(1) 

            # picImage = Image.fromarray(gray,"1")
            # 因为灰度或二值化图片 都是8位／1字节来表示一个像素，因此用“L”. 
            # 而如果用"1",就是一位表示一个像素。 这里gray 或picImage 是8位表示一个像素的，因此用L。
            picImage = Image.frombytes("L", (width,height), gray.tobytes())
            #picImage.show()
            self.disp.image(picImage.convert("1"))
            self.disp.display()
        cap.release()

def main():
    print(sys.argv)
    if(len(sys.argv) == 1):
         sys.exit()
    start = time.time()
    oledPlayer = OLEDPlayer()
    oledPlayer.play(sys.argv[1])
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()