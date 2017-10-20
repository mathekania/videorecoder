import numpy as np
import matplotlib.pyplot as plt
import cv2

x=np.arange(0,20,2)
y=np.sin(x)
plt.plot(x,y)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    pass
