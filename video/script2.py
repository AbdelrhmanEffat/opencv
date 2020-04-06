import cv2
# import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# save the video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Output.avi", fourcc, 20, (640, 480))

'''
print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
'''

# for showing the face we need firs to creat a frame obj
while True:
    check, frame = video.read()

    if check is True:

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # time.sleep(3)
        cv2.imshow('Captturing', gray)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break

video.release()
out.release()
cv2.destroyAllWindows()
