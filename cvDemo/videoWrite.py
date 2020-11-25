import numpy as np
import cv2

cap = cv2.VideoCapture(0) #摄像头

fourcc = cv2.VideoWriter_fourcc(*'X264')

out = cv2.VideoWriter('testwrite001.mp4',fourcc, 24.0, (1920,1080),True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        cv2.imshow('frame',frame)
        out.write(frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()