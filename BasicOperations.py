# GOAL:
# Access pixel values and modify them
# Access image properties
# Setting Region of Image (ROI)
# Splitting and Merging images

import cv2

imgSrc = r'Images\DSC_0002-5.jpg'

img = cv2.imread(imgSrc)

# Pixel value in the form of BGR
pixel = img[100,100]
print("[Blue, Green, Red]: ", pixel)

# Accessing pixel value of only Blue - 0
blue = img[100, 100, 0]
print("blue: ", blue)

# Accessing pixel value of only Green - 1
green = img[100, 100, 1]
print("green: ", green)

# Accessing pixel value of only Red - 2
red = img[100,100,2]
print("red: ", red)

# Image Shape
print("Shape: ", img.shape)

# Total number of pixels
print("Size: ", img.size)

# Image datatype
print("Image DataType: ", img.dtype)

res = cv2.resize(img, (1148, 765))
print(res.shape)

section = res[100:400, 100:400]
res[400:700, 300:600] = section

cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
