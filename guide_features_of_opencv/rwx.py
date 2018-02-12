## rwx means read,write and exicute


import cv2
import numpy as np
img=cv2.imread('saa.jpg',0)#used to read image in gray scale
cv2.imwrite('prudhvi.png',img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

