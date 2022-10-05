import numpy as np
from math import sqrt, ceil
import cv2
import os

#Input file name (random file I found in my folder).
filepath = '/home/zahid/Malware/MAL-SAMPLES/samples/Families/GandCrab'

os.chdir(filepath)

for filename in os.listdir(os.getcwd()):
   with open(os.path.join(os.getcwd(), filename), 'rb') as binary_file:
    print(filename)        
    data = binary_file.read()

# Data length in bytes
    data_len = len(data)

# d is a verctor of data_len bytes
    d = np.frombuffer(data, dtype=np.uint8)

# Assume image shape should be close to square
    sqrt_len = int(ceil(sqrt(data_len)))  # Compute square toot and round up

# Requiered length in bytes.
    new_len = sqrt_len*sqrt_len

# Number of bytes to pad (need to add zeros to the end of d)
    pad_len = new_len - data_len

# Pad d with zeros at the end.
# padded_d = np.pad(d, (0, pad_len))
    padded_d = np.hstack((d, np.zeros(pad_len, np.uint8)))

# Reshape 1D array into 2D array with sqrt_len pad_len x sqrt_len (im is going to be a Grayscale image).
    im = np.reshape(padded_d, (sqrt_len, sqrt_len))

# Save image
    cv2.imwrite(f'{filename}.png', im)