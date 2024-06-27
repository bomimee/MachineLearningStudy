import sys
import cv2

img = cv2.imread('../images/cat.bmp')

if img is None:
    print('img load error')
    sys.exit()

print(type(img))
print(img.shape)

cv2.namedWindow('imgshow1')
cv2.imshow('imgshow2', img)
cv2.waitKey()

cv2.destroyAllWindows()