__version__ = '0.0.1'
__author__ = 'Jeremiah Nelson'
__license__ = 'MIT License. https://www.mit.edu/~amini/LICENSE.md'

from machine import Pin
from utime import sleep_ms


pin = Pin(25, Pin.OUT)
while True:
    pin.toggle()
    sleep_ms(500)