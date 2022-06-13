__version__ = '0.0.1'
__author__ = 'Jeremiah Nelson'
__license__ = 'MIT License. https://www.mit.edu/~amini/LICENSE.md'

from machine import Pin
from utime import sleep_us, ticks_us

class Find_Distance():
    def __init__(self, trigger_pin = 14, echo_pin = 15, off_time = 4, on_time = 10, max_wait = 200000):
        # Initialize Sensor
        self.__echo_pin = Pin(echo_pin, Pin.IN)
        self.__trigger_pin = Pin(trigger_pin, Pin.OUT)
        self.__off_time = off_time
        self.__on_time = on_time
        self.__max_wait = max_wait
    
    ''' In order to calculate distance, we need to know how much time it takes for the ultrasonic
        soundwave to traverse from the sensor to the obstruction and back'''
    def ping(self):
        reset = True
        echo = 0
        while reset == True:
            echo = 0.0
            # time is in microseconds
            self.__trigger_pin.low() # Ensure the the trigger pin is low then wait n microseconds
            sleep_us(self.__off_time)
            self.__trigger_pin.high() # Set the trigger pin to high then wait n microseconds        
            sleep_us(self.__on_time)
            self.__trigger_pin.low() # Set trigger pin to low

            # Acquire new ultrasonic burst time        
            burst_off = 0
            burst_on = 0
            # Get the start time
            delay_timer = ticks_us() + self.__max_wait
            while self.__echo_pin.value() == 0:
                if burst_off > delay_timer:
                    sleep_us(100)
                    reset = True
                    break
                else:
                    burst_off = ticks_us()
                    reset = False
            # Get the received time
            if reset == False:
                delay_timer = ticks_us() + self.__max_wait
                while self.__echo_pin.value() == 1:
                    burst_on = ticks_us()
                    if burst_on > delay_timer:
                        sleep_us(100)
                        reset = True
                        break
                    else:
                        reset = False
                echo = float(burst_on - burst_off)
                if echo < 0: # If negative then reset
                    reset = True
        # Return the round trip time in microseconds        
        return echo

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

    def ping_cm_median(self, samples = 10):
        # Calculate the median distance in centimeters within a given range
        distance = []
        for _ in range(samples):
            dist = (self.ping() * 0.034321) / 2
            distance.append(dist)
        return self.median(distance)

    def ping_in_median(self, samples = 10):
        # Calculate the median distance in centimeters within a given range
        distance = []
        for _ in range(samples):
            dist = (self.ping() * 0.01351221) / 2
            distance.append(dist)
        return self.median(distance)
    
    def median(self, distance_list):
        n = len(distance_list)
        distance_list.sort()        
        if n % 2 == 0:
            median1 = distance_list[n//2]
            median2 = distance_list[n//2 - 1]
            median = (median1 + median2)/2
        else:
            median = distance_list[n//2]
        return median

if __name__ == '__main__':
    from utime import sleep_ms
    while True:
        # print(f'The distance measured is {Find_Distance().ping_cm()} centimeters')
        # print(f'The distance measured is {Find_Distance().ping_in()} inches')
        print(f'The distance measured is {Find_Distance().ping_cm_median()} centimeters median')
        # print(f'The distance measured is {Find_Distance().ping_in_median()} inches median')
        # sleep_ms(500)
