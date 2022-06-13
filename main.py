from machine import Pin
from utime import sleep_ms
import random
from robot_code import motor_controller as mc, ultrasonic_sensor as us

robot = mc.motors(motor_in1 = 0, motor_in2 = 1 , motor_in3 = 2, motor_in4 = 3, duration = 300)
robot.Forward(150)

led = Pin(25, Pin.OUT)
led.high()
sensor = us.Find_Distance()
collision_distance = 6

sleep_ms(3000)

def distance_check():    
    if sensor.ping_cm_median() < collision_distance:
        robot.all_stop(duration = 500)
        robot.Reverse()
        robot.all_stop(duration = 500)
        if random.randint(1, 2) == 1:
            robot.Turn_Right(1000)
            sleep_ms(1000)
        else:
            robot.Turn_Left(1000)
            sleep_ms(1000)
        distance_check()
    return True

while True:
    if distance_check() == True:
        robot.Forward()