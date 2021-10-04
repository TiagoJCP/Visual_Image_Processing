import cv2 as cv

## ----------------------------------------------------------------
## 1 step - read an image
# img = cv.imread('seeds.png')

# cv.imshow('Seeds', img)

# cv.waitKey(0)

## ----------------------------------------------------------------
## 2 step - rescale an image using a function
img = cv.imread('seeds.png')
cv.imshow('Seeds', img)

# Function to rescale the image
def rescaleFigure(figure, scale=0.75):
    width = int(figure.shape[1] * scale)
    height = int(figure.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(figure, dimensions, interpolation=cv.INTER_AREA)

img_rescale=rescaleFigure(img)
cv.imshow('Seeds Resize', img_rescale)


cv.waitKey(0)