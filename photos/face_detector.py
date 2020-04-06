import cv2

# creat a Cascade Classifier obj
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# without passing a parameter means .. color image
# however a good idea to use grayscale images when searching for face
# its for accuracy
img = cv2.imread("mine.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cearing a rectangle around the face
faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.05,
                                      minNeighbors=5)

'''
1> create a window searcehs for faces in the image and reduce the searching
 scale by .05 each time till goes to a final size

2> tell python how many neighbors to search around the window
'''

# drae a rectangle around the face
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# (x, y), (x+w, y+h) >> start and end point of the rectangle
# (0, 255, 0) >> color of the rectangle
# 2 >> rectangle line size

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray", img)
cv2.waitKey(0)
