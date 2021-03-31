# import openCv package
import cv2

# store image to img var
img = cv2.imread('img.jpg')

# make a gray image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# invert image
inv = cv2.bitwise_not(img_gray)

# Blur image
img_blur = cv2.GaussianBlur(inv, (21, 21), 0)

# sketch/draw image
draw = cv2.divide(img_gray, cv2.bitwise_not(img_blur), scale=256.0)

# save image
cv2.imwrite('draw.png', draw)





