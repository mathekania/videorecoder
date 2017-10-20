import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    #if ret==True:
       # fram = cv2.flip(frame,90)


        # write the flipped frame
    out.write(frame)
        #grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.namedWindow('frame',cv2.WINDOW_FULLSCREEN)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #else:
     #   break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()