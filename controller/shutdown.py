#initialization

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

import os
import sys
import termios
import tty
import pigpio
import time

pi=pigpio.pi()

#define functions

def setLights(pin, brightness):
	pi.set_PWM_dutycycle(pin, brightness)

#run program
	
setLights(RED_PIN, 0)
setLights(GREEN_PIN, 0)
setLights(BLUE_PIN, 0)

pi.stop()