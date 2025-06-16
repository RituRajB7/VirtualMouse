import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7
##########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)  # Use 0 if 1 doesn't work
cap.set(3, wCam)
cap.set(4, hCam)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

detector = htm.handDetector()
wScr, hScr = autopy.screen.size()

while True:
    success, img = cap.read()

    if not success or img is None:
        print("Failed to capture image from camera.")
        continue

    # 1. Find hand Landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()

        # 4. Draw rectangle on screen
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        # 5. Only Index Finger: Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 6. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # 7. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 8. Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 9. Both Index and Middle Fingers Up: Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 10. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)

            # 11. Click mouse if distance is short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    # 12. Frame Rate Display
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # 13. Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
