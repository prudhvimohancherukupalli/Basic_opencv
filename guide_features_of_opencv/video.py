import numpy as np
import cv2

cap = cv2.VideoCapture(0) # here 0 indicates that the video is taken through web cam

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	

    # Display the resulting frame
    cv2.imshow('frame',gray)
    #p=cap.get(3)
    #q=cap.get(4)
         
    #print(p)
    #print(q)	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
# here the video will have 0 to 18 properts where as 3rd and 4th are hight and width of the . we can know them by using cap.get()
# and set them by using cap.set()


