import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

for i in range(10):
    GPIO.output(8,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(8,GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()