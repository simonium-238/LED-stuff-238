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

red = sys.argv[1]
green = sys.argv[2]
blue = sys.argv[3]

if(red == ''):
	red=100
if(green == ''):
	green=100
if(blue == ''):
	blue=100

#define functions
	
def setLights(pin, brightness):
	pi.set_PWM_dutycycle(pin, brightness)

#run program
	
setLights(RED_PIN,red)
setLights(GREEN_PIN,green)
setLights(BLUE_PIN,blue)