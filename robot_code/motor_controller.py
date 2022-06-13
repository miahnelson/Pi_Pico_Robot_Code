__version__ = '0.0.1'
__author__ = 'Jeremiah Nelson'
__license__ = 'MIT License. https://www.mit.edu/~amini/LICENSE.md'

from machine import Pin
from utime import sleep_ms


class motors():
    default_duration = 300
    def __init__(self, motor_in1, motor_in2, motor_in3, motor_in4, duration = 300):
        default_duration = duration
        self.__motorA1 = Pin(motor_in1, Pin.OUT)
        self.__motorA2 = Pin(motor_in2, Pin.OUT)
        self.__motorB1 = Pin(motor_in3, Pin.OUT)
        self.__motorB2 = Pin(motor_in4, Pin.OUT)
    
    def all_stop(self, duration = 0):
        self.__motorA1.low()
        self.__motorA2.low()
        self.__motorB1.low()
        self.__motorB2.low()
        sleep_ms(duration)

    def Forward(self, duration = default_duration):
        self.all_stop()
        self.__motorA1.high()
        self.__motorA2.low()
        self.__motorB1.high()
        self.__motorB2.low()
        sleep_ms(duration)
        self.all_stop()
    
    def Reverse(self, duration = default_duration):
        self.all_stop()
        self.__motorA1.low()
        self.__motorA2.high()
        self.__motorB1.low()
        self.__motorB2.high()
        sleep_ms(duration)
        self.all_stop()
    
    def Turn_Left(self, duration = default_duration):
        self.all_stop()
        self.__motorA1.high()
        self.__motorA2.low()
        self.__motorB1.low()
        self.__motorB2.high()
        sleep_ms(duration)
        self.all_stop()

    def Turn_Right(self, duration = default_duration):
        self.all_stop()
        self.__motorA1.low()
        self.__motorA2.high()
        self.__motorB1.high()
        self.__motorB2.low()
        sleep_ms(duration)
        self.all_stop()