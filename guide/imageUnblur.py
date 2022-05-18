import cv2
import numpy as np

image = cv2.imread('images/savedBlurImg/1.jpg')
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(image, -25, sharpen_kernel)
cv2.imwrite('yes.jpg', sharpen)

cv2.imshow('sharpen', sharpen)

cv2.waitKey()