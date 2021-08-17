import cv2
import numpy as np

img = cv2.imread("img.jpg")

width, height = 580, 380

point1 = np.float32([[190, 177], [715, 175], [151, 544], [747, 543]])
point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(point1, point2)

output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Img", img)
cv2.imshow("Output", output)

file = "WarpImage.jpg"
cv2.waitKey(0)
