#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

chanel = [3,5,7,8,10,11,12,13]
times = 2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(chanel, GPIO.OUT) 


def clean():
    GPIO.output(chanel, GPIO.LOW)
    
def gpio():
    one = [10,11]
    two = [3,8,11,12,13]
    three = [3,8,10,11,13]
    four = [3,5,10,11]
    five = [3,5,8,10,13]
    six = [3,5,8,10,12,13]
    return six

def HIGH(times):
    chanels = gpio()
    GPIO.output(chanels, GPIO.HIGH)
    time.sleep(times)
    clean()



HIGH(times)

time.sleep(2)
GPIO.cleanup