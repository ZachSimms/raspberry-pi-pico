from machine import Pin
import time

# create LED object from Pin 25, Set Pin 25 to output
# https://docs.micropython.org/en/latest/library/machine.Pin.html
led = Pin(25, Pin.OUT)   

try:
    while True:
        led.value(1)    # Set led turn on
        time.sleep(0.5) # Sleep 0.5s
        led.value(0)    # Set led turn off
        time.sleep(0.5) # Sleep 0.5s
except:
    pass
