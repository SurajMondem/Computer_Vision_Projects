import cv2

imgsrc = r'Images\DSC_0002-5.jpg'

img = cv2.imread(imgsrc, cv2.IMREAD_GRAYSCALE)
# img = cv2.imread(imgsrc, 0)
res = cv2.resize(img, (600, 650))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
