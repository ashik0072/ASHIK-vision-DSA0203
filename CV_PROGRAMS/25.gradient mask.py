import cv2
import numpy as np
import matplotlib.pyplot as plt
def sharpen_image_with_gradient(image_path, alpha=1.5):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    gradient_x = cv2.Sobel(original_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(original_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    sharpened_image = cv2.addWeighted(original_image, 1 + alpha, gradient_magnitude, -alpha, 0)
    return original_image, sharpened_image
image_path = "C://Users//ASHIK C SABU//Desktop//supraaa//supra.jpg"
original_image, sharpened_image = sharpen_image_with_gradient(image_path, alpha=1.5)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Image')
plt.tight_layout()
plt.show()
