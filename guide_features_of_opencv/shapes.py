import cv2
import numpy as np
# Create a black image
img=cv2.imread('saa.jpg',0)
#img = np.zeros((512,512,3), np.uint8)#attributees are rows ,coloums, dimensins
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)#attribues are start_pint,end_point,colour,width
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)#top_left_coner,bottem_right_corner,colour,boder_width
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)#attriutes are center_of_circle,radius,colour,it may be -1 or 1
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)#
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)#text,position,font_style,font_size,colour,width,line_type
#cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

