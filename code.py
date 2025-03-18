# Created by: Michael Bruneau
# Created on: March 2025
#
# This module is a Raspberrypy Pico program that sends power to RGB LED to create a color then pauses for one second and switches to the next colour and then loops after all colors have been produced

import time
import board
import pwmio
from adafruit_motor import servo

# variables
blink_delay = 0.05

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP13 , duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(blink_delay)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(blink_delay)