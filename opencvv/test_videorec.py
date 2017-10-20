import cv2
cap=cv2.VideoCapture(0)
fcc=cv2.VideoWriter_fourcc(*'DIVX')
file=cv2.VideoWriter('video1.avi',fcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        frame=cv2.flip(frame,90)
        file.write(frame)
        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break
cap.release()
file.release()
cv2.destroyAllWindows()