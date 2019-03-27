#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

chanel = [3,5,7,8,10,11,12,13]
times = 0.8
counter =-1
count = 15 +1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(chanel, GPIO.OUT) 


def clean():
    GPIO.output(chanel, GPIO.LOW)
   
    
def pin(counter):
    zero = [5,8,10,11,12,13]
    one = [10,11]
    two = [3,8,11,12,13]
    three = [3,8,10,11,13]
    four = [3,5,10,11]
    five = [3,5,8,10,13]
    six = [3,5,8,10,12,13]
    seven = [10,11,13]
    eight = [3,5,8,10,11,12,13]
    nign = [3,5,8,10,11,13]
    
    if counter == 0:
        return zero
    elif counter == 1:
        return one
    elif counter ==2:
        return two
    elif counter == 3:
        return three
    elif counter ==4:
        return four
    elif counter == 5:
        return five
    elif counter == 6:
        return six
    elif counter == 7:
        return seven
    elif counter == 8:
        return eight
    elif counter == 9:
        return nign


def HIGH(times, count):
    global counter
    for i in range(count):
        counter = counter + 1
        channels = pin(counter)
        GPIO.output(channels, GPIO.HIGH)
        time.sleep(times)
        clean()
        if counter == 9:
            counter =-1



HIGH(times,count)

time.sleep(0.2)
GPIO.cleanup
