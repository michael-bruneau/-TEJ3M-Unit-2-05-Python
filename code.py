# Created by: Michael Bruneau
# Created on: March 2025
#
# This module is a Raspberrypy Pico program causes micro Servo to to turn back and forth from 180 degress to 0 degrees

import board
import pwmio
from adafruit_motor import servo

# variables
blink_delay = 0.05

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP12 , duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(blink_delay)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(blink_delay)