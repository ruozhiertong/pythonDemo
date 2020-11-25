import time
 
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#直接利用显示图片来播放。速度挺快的，就是图片太多，空间消耗大。 


RST = None
 
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
 
# Initialize library.
disp.begin()
 
# Clear display.
disp.clear()
disp.display()
start = time.time()
for I_image in range(0,1000):
    image = Image.open('resource/badapple_'+str(I_image)+'.jpg').convert('1')
    disp.image(image)
    disp.display()
end = time.time()

print(end - start)