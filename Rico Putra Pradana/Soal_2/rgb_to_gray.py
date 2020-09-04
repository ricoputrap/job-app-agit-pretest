import cv2

# read the original image
img_rgb = cv2.imread('img/hilih.png')

# convert image from rgb to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# save the converted image
cv2.imwrite('img/hilih-gray.png', img_gray)

# show the converted image
cv2.imshow("Output", img_gray)
cv2.waitKey(0)