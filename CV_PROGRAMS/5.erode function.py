import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "C://Users//ASHIK C SABU//Desktop//supraaa//supra.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel , iterations = 10)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)
desired_width = 800
desired_height = 600
img_resized = cv2.resize(imgEroded, (desired_width, desired_height))
cv2.imshow("Img Erosion",img_resized)
cv2.waitKey(0)
