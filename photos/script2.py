import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.imread("mine.jpg")
video = cv2.VideoCapture('Video.mp4')

while True:
    _, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cearing a rectangle around the face
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.5,
                                          minNeighbors=4)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
