import cv2
import numpy as np
import matplotlib.pyplot as plt

def prewitt_edge_detection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    img_prewittx = cv2.filter2D(gray_image, -1, kernelx)
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    img_prewitty = cv2.filter2D(gray_image, -1, kernely)

    img_prewitt = cv2.addWeighted(img_prewittx, 0.5, img_prewitty, 0.5, 0)
    return img_prewitt
image = cv2.imread('input_image.jpg')
edge_detected_image = prewitt_edge_detection(image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edge_detected_image, cmap='gray')
plt.title('Prewitt Edge Detection')
plt.axis('off')

plt.show()
