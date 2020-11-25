#! encoding: UTF-8
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cv2
import time  # 引入time模块
import Adafruit_SSD1306

def initSSD1306():
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

def process(filepath,width,height,x=0,y=0):
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
        picImage = Image.frombytes("L", (128,64), gray.tobytes())
        #picImage.show()
        disp.image(picImage.convert("1"))
        disp.display()
    cap.release()



def main():
    print(sys.argv)
    if(sys.argv.size() == 1):
         sys.exit()
    start = time.time()
    disp = initSSD1306()
    process(sys.argv[1],disp.width, disp.height)
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()