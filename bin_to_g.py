import numpy as np
import imageio
from PIL import Image
import os
import cv2
import random


images_gray=[]

path = '/home/zahid/Malware/0NEW/Malware/Blacksoul/'
output = '/home/zahid/Malware/0NEW/0GRAY/newData/'

w, h= 224,224
files=os.listdir(path)
for name in files:
  print(name)
  # Read file using numpy "fromfile()"
  with open(path + name, mode='rb') as f:
    d = np.fromfile(f,dtype=np.uint8,count=w*h).reshape(h,w)
  #gray = Image.fromarray(d).convert("L")
  gray=cv2.cvtColor(d,cv2.COLOR_GRAY2RGB)
  images_gray.append(gray)

for index, image in enumerate(images_gray):
  im=np.array(image)
  imageio.imwrite(output+'Blacksoul_'+str(index)+'.png',im)
  print(index)
