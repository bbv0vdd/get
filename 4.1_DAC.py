import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal_to_bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

print(decimal_to_bin(3))

try:
    print("Введите целое число от 0 до 255")
    inp = input()
    if inp.isdigit() != 1:
        print("Вы ввели нецелое число")
        exit(0)
    elif int(inp) > 255:
        print("Вы ввели число большее 255")
    elif int(inp) < 0:
        print("Вы ввели число меньшее 0")
        exit(0)
    

    GPIO.output(dac, decimal_to_bin(int(inp)))
    voltage = 3.3/256*int(inp)
    print(voltage)
    stop = input()
    
    if stop == "q":
        exit(0)
    
except ValueError: 
    print("Вы ввели не число")

finally:
    GPIO.output(dac, 0)