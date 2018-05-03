#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pins = [2, 3, 4, 14, 15]
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pins, GPIO.OUT)
    
    while True:
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.2)

        for pin in pins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.2)


if __name__ == "__main__":
    main()

