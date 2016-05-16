import cv2
import numpy as np
img = cv2.imread('Frame3.bmp',0)
img = cv2.medianBlur(img,3)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=40, param2=16, minRadius=15, maxRadius=22)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
     cv2.circle(cimg, (i[0],i[1]),i[2],(0,255,0),2)
cv2.imshow("circles", cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
