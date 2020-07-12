import cv2

imgsrc = r'I:\D5600 Pictures\Exports\DSC_0521.jpg'

img = cv2.imread(imgsrc, cv2.IMREAD_GRAYSCALE)
# img = cv2.imread(imgsrc, 0)
res = cv2.resize(img, (600, 650))
cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
