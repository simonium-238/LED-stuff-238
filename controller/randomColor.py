RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

import os
import sys
import termios
import tty
import pigpio
import time
from random import randint

pi=pigpio.pi()

breakTime = float(sys.argv[1])

def setLights(pin, brightness):
	pi.set_PWM_dutycycle(pin, brightness)

while True:
	setLights(RED_PIN,randint(0,255))
	setLights(GREEN_PIN,randint(0,255))
	setLights(BLUE_PIN,randint(0,255))
	time.sleep(breakTime)