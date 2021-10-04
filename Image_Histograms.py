import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# # Histograms Grayscale
# img = cv.imread('Lenna.png')
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Image Gray',img_gray)

# gray_hist = cv.calcHist([img_gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# cv.waitKey(0)

# Histograms Colors

img = cv.imread('Lenna.png')
cv.imshow('Original Image', img)

colors = ('r', 'g', 'b')

for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])


plt.show()

cv.waitKey(0)