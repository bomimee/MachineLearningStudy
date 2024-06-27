import cv2
src = cv2.imread('../images/namecard1.jpg', cv2.IMREAD_GRAYSCALE)
th, src_bin = cv2.threshold(src, 0, 255,cv2.THRESH_BINARY)
cv2.imshow('src', src)
cv2.imshow('dst', src)
cv2.waitKey()
cv2.destroyAllWindows()
