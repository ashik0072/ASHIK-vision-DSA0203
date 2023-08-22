import cv2
import numpy as np
cap = cv2.VideoCapture("C://Users//ASHIK C SABU//Desktop//supraaa//supra.jpg")
while True:
    ret, frame = cap.read()
    pts1 = np.float32([[200,300], [5, 2],[0, 4], [6, 0]])
    pts2 = np.float32([[0, 0], [4, 0],[0, 1], [4, 6]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (0, 0))
    img = cv2.resize(result,(600,600))
    cv2.imshow('frame', frame) 
    cv2.imshow('frame1', img)
    if cv2.waitKey(24) == 27:
        break
cap.release()
cv2.destroyAllWindows()
