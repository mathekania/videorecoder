import cv2
img2=cv2.imread('img3.jpg',0)
#cv2.namedWindow('IRENE', cv2.WINDOW_NORMAL)
cv2.namedWindow('IRENE',cv2.WINDOW_GUI_NORMAL)
cv2.imshow('IRENE',img2)

while(cv2.waitKey(10000000) & 0xFF == ord('q')):
    break




'''''
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('kuku.png',img)
    cv2.destroyAllWindows()
'''''