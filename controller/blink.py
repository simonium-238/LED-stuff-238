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

hex = sys.argv[1]
breakTime = float(sys.argv[2])
rgb = []
rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
red = rgb[0]
green = rgb[1]
blue = rgb[2]

def setLights(pin, brightness):
	pi.set_PWM_dutycycle(pin, brightness)	

while True:
		setLights(RED_PIN,red)
		setLights(GREEN_PIN,green)
		setLights(BLUE_PIN,blue)
		
		time.sleep(breakTime)
		
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(breakTime)