#Initialization

RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

import os
import sys
import termios
import tty
import pigpio
import time

pi=pigpio.pi()

STEPS=0.0

if sys.argv[1] == "slow":
	STEPS = 0.001
elif sys.argv[1] == "medium":
	STEPS = 0.01
elif sys.argv[1] == "fast":
	STEPS = 0.05

bright = 255.0
r = 255.0
g = 0.0
b = 0.0

pi = pigpio.pi()

brightChanged = False
state = True

#define functions

def updateColor(color, step):
	color += step
	
	if color > 255:
		return 255
	if color < 0:
		return 0
		
	return color


def setLights(pin, brightness):
	realBrightness = int(int(brightness) * (float(bright) / 255.0))
	pi.set_PWM_dutycycle(pin, realBrightness)

#run program
	
setLights(RED_PIN, r)
setLights(GREEN_PIN, g)
setLights(BLUE_PIN, b)


while True:
	if state and not brightChanged:
		if r == 255 and b == 0 and g < 255:
			g = updateColor(g, STEPS)
			setLights(GREEN_PIN, g)
		
		elif g == 255 and b == 0 and r > 0:
			r = updateColor(r, -STEPS)
			setLights(RED_PIN, r)
		
		elif r == 0 and g == 255 and b < 255:
			b = updateColor(b, STEPS)
			setLights(BLUE_PIN, b)
		
		elif r == 0 and b == 255 and g > 0:
			g = updateColor(g, -STEPS)
			setLights(GREEN_PIN, g)
		
		elif g == 0 and b == 255 and r < 255:
			r = updateColor(r, STEPS)
			setLights(RED_PIN, r)
		
		elif r == 255 and g == 0 and b > 0:
			b = updateColor(b, -STEPS)
			setLights(BLUE_PIN, b)
	

