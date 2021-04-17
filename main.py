import cv2
from pygame import mixer

mixer.init()

mixer.music.load("sound.wav")

cameras = cv2.VideoCapture(0)

while cameras.isOpened():
    r, frame = cameras.read()
    r, newFrame = cameras.read()

    difference = cv2.absdiff(frame, newFrame)
    gray = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5) ,0)
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    dilate = cv2.dilate(threshold, None, iterations=3)
    contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contours, -1, (255,0,0),2 )

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(c)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        mixer.music.play()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("Personal Security Camera", frame)
