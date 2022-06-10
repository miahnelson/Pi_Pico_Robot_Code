from robot_code import ultrasonic_sensor as us
from utime import sleep_ms

if __name__ == '__main__':
    while True:
        distance = (us.Find_Distance().ping_cm())
        print(f'The distance measured is {distance} centimeters')
        distance = (us.Find_Distance().ping_in())
        print(f'The distance measured is {distance} inches')
        sleep_ms(1000)