import cv2
import numpy as np
import matplotlib.pyplot as plt
def high_boost_sharpening(image_path, k=1.5):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred_image = cv2.GaussianBlur(original_image, (5, 5), 0)
    high_pass = original_image - blurred_image
    sharpened_image = original_image + k * high_pass
    return original_image, sharpened_image
image_path = "C://Users//ASHIK C SABU//Desktop//supraaa//supra.jpg"
original_image, sharpened_image = high_boost_sharpening(image_path, k=1.5)
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Image')
plt.subplot(1, 3, 3)
plt.imshow(original_image - sharpened_image, cmap='gray')
plt.title('Detail (High-Pass)')
plt.tight_layout()
plt.show()
