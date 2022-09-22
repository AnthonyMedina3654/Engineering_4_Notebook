# type: ignore
import time
import board
import digitalio
led = digitalio.DigitalInOut(board.GP21)
led2 = digitalio.DigitalInOut(board.GP22)
led.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
for x in range(10, 0, -1):
    print(x) 
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
led2.value = True
time.sleep(10)