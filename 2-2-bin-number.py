import RPi.GPIO as GPIO
import time
#from random import randint

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0]*8
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
 
#for i in range(8):
#    number[i] = randint(0,1)
#GPIO.output(dac, number)
#time.sleep(15)
GPIO.output(dac, 0)
number = [0, 1, 0, 1, 0, 0, 0, 0]
GPIO.output(dac, number)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()