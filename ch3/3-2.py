import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('../sourceImage/soccer.jpg')
h=cv.calcHist([img], [2], None, [256], [0, 256])
    # 2번 채널인 R 채널에서 히스토그램을 구함
plt.plot(h, color='r', linewidth = 1)
plt.show()