import cv2 as cv
import numpy as np

## ----------------------------------------------------------------
# 1. Read an image using OPENCV
# img = cv.imread('seeds.png')
# cv.imshow('Seeds', img)
# cv.waitKey(0)
## ----------------------------------------------------------------

# 2. Re-scale an image using a function
# img = cv.imread('seeds.png')
# cv.imshow('Seeds', img)

# # Function to rescale the image
# def rescaleFigure(figure, scale=0.75):
#     width = int(figure.shape[1] * scale)
#     height = int(figure.shape[0] * scale)
#     dimensions = (width,height)

#     return cv.resize(figure, dimensions, interpolation=cv.INTER_AREA)

# img_rescale=rescaleFigure(img)
# cv.imshow('Seeds Resize', img_rescale)
# cv.waitKey(0)
## ----------------------------------------------------------------

# 3. Grayscale
# img = cv.imread('Lenna.png')
# cv.imshow('Lenna', img)

# # Convert to Grayscale levels
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray Scale', gray_img)
#cv.waitKey(0)
## ----------------------------------------------------------------

# 4. Blur
# img = cv.imread('Lenna.png')
#cv.imshow('Color', img)

# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Lenna Blur', blur)

# cv.waitKey(0)
## ----------------------------------------------------------------

# 5. Canny Edge Detector

# canny = cv.Canny(img, 125, 175)
#cv.imshow('Lenna Canny', canny)

# # Using the Blur Image
# canny_blur = cv.Canny(blur, 125, 175)
# cv.imshow('Lenna Blur Canny ', canny_blur)

# # Using the Gray Image
# # canny_gray = cv.Canny(gray_img, 125, 175)
# # cv.imshow('Lenna Gray Canny ', canny_gray)

# cv.waitKey(0)
## ----------------------------------------------------------------

# 6. Dilating
# dilated = cv.dilate(canny_blur, (10,10), iterations=3)
# cv.imshow('Dilated', dilated)

#cv.waitKey(0)
## ----------------------------------------------------------------

# 7. Eroding
# eroded = cv.erode(dilated, (10,10), iterations=3)
# cv.imshow('Eroded', eroded)

# cv.waitKey(0)
## ----------------------------------------------------------------

# 8. Resize and Crop an Image
# Why use interpolation? Because its importance to keep the image proporcion with correct aspect ratio
# resized = cv.resize(img, (240,240), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# # Crop
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

# cv.waitKey(0)
## ----------------------------------------------------------------
