import cv2
cap=cv2.VideoCapture()
fcc=cv2.VideoWriter_fourcc(*'DIVX')
file=cv2.VideoWriter('anto.avi',fcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        file.write(frame)
        cv2.imshow('video2',frame)
        if  cv2.waitKey(10000) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
file.release()
cv2.destroyAllWindows()

