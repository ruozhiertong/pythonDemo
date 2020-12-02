#! encoding: UTF-8
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time  # 引入time模块
import Adafruit_SSD1306


# 直接使用opencv 处理视频，在此基础上 直接显示图片，从而播放。


class PICShow():
    """docstring for PICShow"""
    def __init__(self):
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
        # image = Image.new('1', (width, height)) #创建一个图片
        # Get drawing object to draw on image.
        # draw = ImageDraw.Draw(image)
        self.disp = disp

    def showViaPath(self, filePath, width = 0, height = 0, x = 0, y =0):
        image = Image.open(sys.argv[1])
        self.showViaImage(image, width, height, x, y)

    def showViaImage(self, image, width = 0, height = 0, x = 0, y =0):
        if(width == 0):
            width = self.disp.width
        if(height == 0):
            height = self.disp.height
        #这个图片只能是充满这个那个屏幕的。
        self.disp.image(image.resize((width, height)).convert('1'))
        self.disp.display()

def main():
    print(sys.argv)
    if(len(sys.argv) == 1):
         sys.exit()
    start = time.time()
    pICShow = PICShow()
    pICShow.showViaPath(sys.argv[1])
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()