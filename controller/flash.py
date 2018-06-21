#Initialization

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

red = sys.argv[1]
green = sys.argv[2]
blue = sys.argv[3]

if sys.argv[4] == "slow":
	STEPS = 0.001
elif sys.argv[4] == "medium":
	STEPS = 0.01
elif sys.argv[4] == "fast":
	STEPS = 0.05
	
bright = 255

#define functions

def setLights(pin, brightness, bright):
	realBrightness = int(int(brightness) * (float(bright) / 255.0))
	pi.set_PWM_dutycycle(pin, realBrightness)

#run program
	
while True:
	setLights(RED_PIN, red, bright)
	setLights(GREEN_PIN, green, bright)
	setLights(BLUE_PIN, blue, bright)
	if(bright > 0):
		bright = bright - STEP
	else:
		bright = 255