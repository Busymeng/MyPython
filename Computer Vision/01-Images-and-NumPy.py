##############################################################################
##  Images and Numpy
##----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open("../DATA/00-puppy.jpg")
pic.show()

type(pic)

pic_arr = np.asarray(pic)
pic_arr.shape

plt.imshow(pic_arr)

pic_red = pic_arr.copy()

plt.imshow(pic_red)
pic_red.shape

# R , G, B
pic_red[:,:,0]
pic_red[:,:,0].shape
plt.imshow(pic_red[:,:,0])

# RED channel values
plt.imshow(pic_red[:,:,0], cmap='gray')

# Green channel values
plt.imshow(pic_red[:,:,1], cmap='gray')

# Blue channel values
plt.imshow(pic_red[:,:,2], cmap='gray')

# Make Green channl 0, no contribution of green
pic_red[:,:,1] = 0
plt.imshow(pic_red)  ## Kind of R+B

# Make Blue channl 0, no contribution of blue
pic_red[:,:,2] = 0
plt.imshow(pic_red)  ## Pure Red
