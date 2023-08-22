import cv2
import numpy as np
image_path = "C://Users//ASHIK C SABU//Desktop//supraaa//supra.jpg"
image = cv2.imread(image_path)
rows, cols, _ = image.shape
transformation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
affine_image = cv2.warpAffine(image, transformation_matrix, (cols, rows))
img = cv2.resize(image,(600,600))
img2 = cv2.resize(affine_image,(600,600))
cv2.imshow('Original Image', img)
cv2.imshow('Affine Transformed Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
