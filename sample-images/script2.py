import cv2
import glob

images = glob.glob("*.jpg")
# create this  [path:\firstphoto, path:\\secondone, ...]

for i in images:
    img = cv2.imread(i, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Showing", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+i, re)

'''
What glob does is that it finds the path names of some files,
 given a certain pattern

'''
