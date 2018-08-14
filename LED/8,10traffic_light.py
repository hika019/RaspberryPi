import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)#Red
GPIO.setup(10,GPIO.OUT) #blue

for i in range(5):
    GPIO.output(8,GPIO.HIGH)
    time.sleep(6)
    
    GPIO.output(8,GPIO.LOW)
    GPIO.output(10,GPIO.HIGH)
    time.sleep(4)
    
    for f in range(2):
        GPIO.output(10,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(10,GPIO.HIGH)
        time.sleep(0.5)
    GPIO.output(10,GPIO.LOW)

GPIO.cleanup()