# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 23:19:27 2016

@author: Byungtae
"""

from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

example_file = ("http://upload.wikimedia.org/wikipedia/commons/7/7d/Dog_face.png")
image = imread(example_file, as_grey=True)
plt.imshow(image, cmap=cm.gray)
plt.show()

image2 = image[5:70, 0:70]
plt.imshow(image2, cmap=cm.gray)
plt.show()