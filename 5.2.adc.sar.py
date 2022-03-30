import RPi.GPIO as GPIO                                                                 
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
troykaModule = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

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
        
        
    
    
finally:
    GPIO.output(dac, 0)