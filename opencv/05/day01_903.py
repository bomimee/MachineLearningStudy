import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('../images/cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BayerGB2BGR)
plt.axis('off')
plt.imshow(imgRGB)
plt.show()

#한번에 두개의 영상
imgGray = cv2.imread('../images/cat.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off')
plt.imshow(imgRGB)

plt.subplot(121)
plt.axis('off')
plt.imshow(imgRGB)
plt.show()