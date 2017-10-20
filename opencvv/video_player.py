import cv2
cap=cv2.VideoCapture('‪D:\movie\Addicted to Fresno (2015).avi')
while(cap.isOpened()):
    ret,frame=cap.read()
   # grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('video1',cv2.EVENT_MOUSEWHEEL)
    cv2.imshow("video1",frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()