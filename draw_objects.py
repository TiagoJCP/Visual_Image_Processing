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
# cv.rectangle(black_img, (155,155), (165,165), (255,255,255), thickness=1)
# cv.imshow('Center Retangle', black_img)

# # or a method to get the center of the image
# cv.rectangle(black_img, (((black_img.shape[1]//2) - 5), ((black_img.shape[0]//2) - 5)), (((black_img.shape[1]//2)+5), ((black_img.shape[0]//2) +5)), (255,255,255), thickness=1)
# cv.imshow('Center Function Retangle', black_img)

# create variables to simplify your code
x_image_center = black_img.shape[1]//2
y_image_center = black_img.shape[0]//2

x_image = black_img.shape[1]
y_image = black_img.shape[0]

# cv.rectangle(black_img, (x_image_center-5,y_image_center-5), (x_image_center+5,y_image_center+5), (255,255,255), thickness=1)
# cv.imshow('Center Function Variable Retangle', black_img)
# ===============================================================================================

# 6. Draw a Circle
# cv.circle(black_img, (x_image_center,y_image_center), 100, (255,255,255), thickness=1)
# cv.imshow('Circle Center', black_img)
# ===============================================================================================

# 7. Draw a Line
# cv.line(black_img, (x_image_center,y_image_center-10), (x_image_center,y_image_center+10), (255,255,255), thickness=1)
# cv.imshow('Line', black_img)
# ===============================================================================================

# 8. Write Text
# cv.putText(black_img, 'Hello World', (x_image_center-90,y_image_center), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
# cv.imshow('Text', black_img)


# ===============================================================================================

cv.waitKey(0)