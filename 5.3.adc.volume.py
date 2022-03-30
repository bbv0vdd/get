import RPi.GPIO as GPIO                                                                 
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
troykaModule = 17
comp = 4
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def decimal_to_bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    value = 0

    for i  in range(8):
        value = value + 2**(7-i)
        GPIO.output(dac, decimal_to_bin(int(value)))
        time.sleep(0.01)
        if int( GPIO.input(comp)) == 0:
            value = value - 2**(7-i)

    return value


try:
    while True:
        i = adc()
        time.sleep(0.1)
        voltage = 3.3/256*i
        print(voltage, i)
        if i <= 0:
            GPIO.output(leds, decimal_to_bin(int(0)))
        elif i <= 32:
            GPIO.output(leds, decimal_to_bin(int(1)))
        elif i <= 64:
            GPIO.output(leds, decimal_to_bin(int(3)))
        elif i <= 96:
            GPIO.output(leds, decimal_to_bin(int(7)))
        elif i <= 128:
            GPIO.output(leds, decimal_to_bin(int(15)))
        elif i <= 160:
            GPIO.output(leds, decimal_to_bin(int(31)))
        elif i <= 192:
            GPIO.output(leds, decimal_to_bin(int(63)))
        elif i <= 224:
            GPIO.output(leds, decimal_to_bin(int(127)))
        else:
            GPIO.output(leds, decimal_to_bin(int(255)))
    
    
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)