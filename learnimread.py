# Python program to explain cv2.imread() method

# importing cv2
import cv2

# path


# Using cv2.imread() method
img = cv2.imread(r'C:\Users\Maker Lab\Pictures\Camera Roll\WIN_20201130_115910.JPG',cv2.cv2.IMREAD_UNCHANGED)

# Displaying the image
cv2.imshow('image', img)
img.shape
cv2.waitKey(0)
