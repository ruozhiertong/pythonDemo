#! encoding: UTF-8
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time  # 引入time模块
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
# image = Image.new('1', (width, height)) #创建一个图片
# Get drawing object to draw on image.
# draw = ImageDraw.Draw(image)

def main():
    print(sys.argv)
    if(sys.argv.size() == 1):
         sys.exit()
    start = time.time()
    image = Image.open(sys.argv[1]).convert('1')
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()