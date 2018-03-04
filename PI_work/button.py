import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    inputs=GPIO.input(18)
    if inputs==False:
        print('pressed')
        time.sleep(0.2)
        