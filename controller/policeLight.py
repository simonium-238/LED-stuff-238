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
	
while True:
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,255)
		
		time.sleep(0.15)
		
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,255)
		setLights(GREEN_PIN,255)
		setLights(BLUE_PIN,255)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,255)
		setLights(GREEN_PIN,255)
		setLights(BLUE_PIN,255)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,255)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(0.15)
		
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,255)
		setLights(GREEN_PIN,255)
		setLights(BLUE_PIN,255)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,255)
		setLights(GREEN_PIN,255)
		setLights(BLUE_PIN,255)
		
		time.sleep(0.1)
		
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)
		
		time.sleep(0.1)