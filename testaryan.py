import cv2
import urllib.request
import numpy as np
import time

url = 'http://192.168.155.241/'
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
car_cascade = cv2.CascadeClassifier('Car.xml')
t_end = time.time() + 10 * 1
while time.time() < t_end:
    img_resp = urllib.request.urlopen(url + 'cam-lo.jpg')
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    cnt = 0

    # To draw a rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cnt += 1

    # Display frames in a window
    cv2.imshow('video2', img)
    key = cv2.waitKey(5)
    # Wait for Esc key to stop
    if key == ord('q'):
        break


print(cnt, " cars found")

def cars():
    return cnt

cv2.destroyAllWindows()