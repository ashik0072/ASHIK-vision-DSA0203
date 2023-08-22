import cv2
import numpy as np
img = cv2.imread("C://Users//ASHIK C SABU//Desktop//supraaa//supra.jpg")
img = cv2.resize(img,(255, 255))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_img = cv2.filter2D(gray_img, -1, laplacian_kernel)
sharpened_img = cv2.cvtColor(sharpened_img, cv2.COLOR_GRAY2BGR)
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
