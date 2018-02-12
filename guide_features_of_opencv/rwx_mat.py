import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('saa.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()
#the reasion behind it is . the opencv load and display images in BGR format . where as matplotlib in RGB
# so we have to change the formate
#img2 = img[:,:,::-1] .. can also used insted of split and merge commands
#cv2.cvtColor(img, cv2.COLOR_BGR2RGB) .... can also be used
