import cv2 as cv
import numpy as np

# 1. Create a black image
black_img = np.zeros((320,320,3), dtype='uint8')
cv.imshow('Black Image', black_img)

# 2. Draw a white point (1 pixel) in the Black Image
# black_img[159:160 , 160:161] = 255
# cv.imshow('Pixel', black_img)
# ===============================================================================================

# 3. Draw a square in the Black Image
# cv.rectangle(black_img, (0,0), (160,160), (255,255,255), thickness=1)
# cv.imshow('Retangle', black_img)
# ===============================================================================================

# 4. If we want to fill the square, we need to make a "FILLED"
# cv.rectangle(black_img, (0,0), (160,160), (255,255,255), thickness=cv.FILLED)
# cv.imshow('Retangle_Fill', black_img)
# ===============================================================================================

# 5. Draw a square or retangle on the image center
cv.rectangle(black_img, (155,155), (165,165), (255,255,255), thickness=1)
cv.imshow('Center Retangle', black_img)

# or a method to get the center of the image
cv.rectangle(black_img, (((black_img.shape[1]//2) - 5), ((black_img.shape[0]//2) - 5)), (((black_img.shape[1]//2)+5), ((black_img.shape[0]//2) +5)), (255,255,255), thickness=1)
cv.imshow('Center Function Retangle', black_img)

# create variables to simplify your code
x_image = black_img.shape[1]//2
y_image = black_img.shape[0]//2

cv.rectangle(black_img, (x_image-5,y_image-5), (x_image+5,y_image+5), (255,255,255), thickness=1)
cv.imshow('Center Function Variable Retangle', black_img)
# ===============================================================================================

# 6. Draw a Circle
cv.circle(black_img, ())


cv.waitKey(0)