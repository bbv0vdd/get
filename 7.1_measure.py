import RPi.GPIO as GPIO                                                                 
import time
import matplotlib.pyplot as plt

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
    
    
    measured_data = []
    time_start = time.time()
    GPIO.output(17, GPIO.HIGH)
    voltage = 0
    while voltage <= 0.9*3.3:
        i = adc()
        voltage = 3.3/256*i
        print(voltage, i)
        measured_data.append(voltage)
    
    GPIO.output(17, GPIO.LOW)
    
    print("aaaaaaaaaaaaaaaaaa")
    while voltage >= 0.02*3.3:
        i = adc()
        voltage = 3.3/256*i
        print(voltage, i)
        measured_data.append(voltage)
    
    time_end = time.time()
    delay = time_end - time_start
    plt.plot(measured_data)
    plt.show()
    print(measured_data)
finally:
    GPIO.output(dac, 0)
with open("data.txt", "w") as outfile:
    outfile.write("\n".join(list(map(lambda x: str(x), measured_data))))