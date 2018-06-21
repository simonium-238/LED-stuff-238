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
breakTime = float(sys.argv[4])

if(red == ''):
	red=100
if(green == ''):
	green=100
if(blue == ''):
	blue=100
if(breakTime == ''):
	breakTime = float(1)

#define functions
	
def setLights(pin, brightness):
	pi.set_PWM_dutycycle(pin, brightness)	

#run program
	
while True:
		setLights(RED_PIN,red)
		setLights(GREEN_PIN,green)
		setLights(BLUE_PIN,blue)
		
		time.sleep(breakTime)
		
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(breakTime)