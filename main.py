import cvzone
from cv2 import cv2
'''
bg=cv2.imread('jkr.png')
sunglass = cv2.imread('sunglass.png',cv2.IMREAD_UNCHANGED)
final_image = cvzone.overlayPNG(bg, sunglass, [100, 100])
cv2.imshow('Snap Cheat', final_image)
cv2.waitKey(0)
'''
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('cool.png', cv2.IMREAD_UNCHANGED)
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0, 255, 0),  2)
        overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])

    cv2.imshow('Snap Cheat', frame)
    cv2.imshow('Snap Cheat', frame)
    if cv2.waitKey(10) == ord('q'):
        break
