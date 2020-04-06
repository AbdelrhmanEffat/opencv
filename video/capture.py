import cv2
# import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
'''
- 0 stands for the index of my camera .. if i have 2 cameras then one of them
are going to be 0 and the other is 1

- aslo we can pass a video path there
'''

# save the video

a = 1

# for showing the face we need firs to creat a frame obj
while True:
    a += 1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # time.sleep(3)
    cv2.imshow('Captturing', gray)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)  # number of frames

video.release()
cv2.destroyAllWindows()
