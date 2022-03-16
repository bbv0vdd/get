import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal_to_bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

try:
    t =float(input())
    while True:
        for i in range(256):
            GPIO.output(dac, decimal_to_bin(i))
            time.sleep(t/512)
        for i in range(256):
            GPIO.output(dac, decimal_to_bin(255-i))
            time.sleep(t/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
