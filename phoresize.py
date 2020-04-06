import cv2

# we can pass here 2 arguments .. 1 as it is, 2 B&W'grayscale' having 1 band
# -1 >> color image ... will have transparency capabilities
img = cv2.imread('photoname', 1)  # values of 0 differ from 1


# height .... width
resized_img = cv2.resize(img, (200, 200))

cv2.imshow("sis.jfif", resized_img)
cv2.imwrite("sister_resized.jpg", resized_img)
cv2.waitKey(0)  # miliseconds
cv2.destroyAllWindows()
