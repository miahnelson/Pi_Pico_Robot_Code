__version__ = '0.0.1'
__author__ = 'Jeremiah Nelson'
__license__ = 'MIT License. https://www.mit.edu/~amini/LICENSE.md'

from machine import Pin
from utime import sleep_us, ticks_us

class Find_Distance():
    def __init__(self, trigger_pin = 14, echo_pin = 15, off_time = 2, on_time = 10):
        # Initialize Sensor
        self.__echo_pin = Pin(echo_pin, Pin.IN)
        self.__trigger_pin = Pin(trigger_pin, Pin.OUT)
        self.__off_time = off_time
        self.__on_time = on_time
    
    ''' In order to calculate distance, we need to know how much time it takes for the ultrasonic
        soundwave to traverse from the sensor to the obstruction and back'''
    def ping(self):
        # time is in microseconds
        # Ensure the the trigger pin is low then wait n microseconds
        self.__trigger_pin.low()
        sleep_us(self.__off_time)
        # Set the trigger pin to high then wait n microseconds
        self.__trigger_pin.high()
        sleep_us(self.__on_time)
        # Set trigger pin to low
        self.__trigger_pin.low()

        # Acquire new ultrasonic burst time
        burst_off = 0
        burst_on = 0
        # Get the start time
        while self.__echo_pin.value() == 0:
            burst_off = ticks_us()
        # Get the received time
        while self.__echo_pin.value() == 1:
            burst_on = ticks_us()

        # Return the round trip time in microseconds
        return float(burst_on - burst_off)

    ''' The speed of sound in dry air at 20 °C is 343.21 m/s or 34321 cm/s or 0.034321 cm/µs
        To calculate the distance we can take the time elapsed and divide by 2 to account for the round trip '''
    def ping_cm(self):
        # Calculate the distance in centimeters
        distance = (self.ping() * 0.034321) / 2
        return distance

    ''' The speed of sound is 1126.01 f/s or 13512.21 in/s or 0.01351221 in/µs
        To calculate the distance we can take the time elapsed and divide by 2 to account for the round trip'''
    def ping_in(self):
        # Calculate the distance in inches
        distance = (self.ping() * 0.01351221) / 2
        return distance

if __name__ == '__main__':
    while True:
        distance = (Find_Distance().ping_cm())
        print(f'The distance measured is {distance} centimeters')
        distance = (Find_Distance().ping_in())
        print(f'The distance measured is {distance} inches')
        sleep_us(1000000)
