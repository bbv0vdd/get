import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 0.1)
p.start(0)
p.stop()
try:
    
    duty_cycle = int(input())
    p.start(duty_cycle)
    
    voltage = 3.3*duty_cycle/100
    print(voltage)
    time.sleep(100)
    
    p.stop()
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()