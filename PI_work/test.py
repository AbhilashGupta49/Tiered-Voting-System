import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (480, 360)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('me.jpg')
    time.sleep(2)
    camera.capture('me2.jpg')