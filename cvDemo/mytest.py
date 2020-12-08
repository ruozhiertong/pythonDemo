import numpy as np
from PIL import Image


pic = np.zeros((64,128),np.uint8)

picImage = Image.frombytes("L",(128,64),pic.tobytes())

type(picImage)


tmp = picImage.convert("1")

type(tmp)
