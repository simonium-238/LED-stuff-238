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

rgb = []
rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
red = rgb[0]
green = rgb[1]
blue = rgb[2]

def setLights(pin, brightness):
	pi.set_PWM_dutycycle(pin, brightness)
	
setLights(RED_PIN,red)
setLights(GREEN_PIN,green)
setLights(BLUE_PIN,blue)