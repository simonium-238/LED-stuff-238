#!/usr/bin/python

#This controllers purpose is to manage the inputs for a RGB LED strip
#The setup you can find on the following website:
#German: https://dordnung.de/raspberrypi-ledstrip/de
#English: https://dordnung.de/raspberrypi-ledstrip/en
#This script was build for educational purposes

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
from thread import start_new_thread

pi=pigpio.pi()

def setLights(pin, brightness):
	pi.set_PWM_dutycycle(pin, brightness)

def getCh():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)

	try:
		tty.setraw(fd)
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

	return ch

def checkKey():
	global abort

	while True:
		c = getCh()
		if c == 1:
			r=input('Value for red (0 to 255): ')
			g=input('Value for green (0 to 255): ')
			b=input('Value for blue (0 to 255): ')
			setColor(r, g, b)
		if c == 2:
			r=input('Value for red (0 to 255): ')
			g=input('Value for green (0 to 255): ')
			b=input('Value for blue (0 to 255): ')
			breakTime = input('Give the break time in second. Eg.: 1.5 (1.5 seconds): ')
			blink(r, g, b, breakTime)
		if c == 3:
			policeLight()
		if c == 4:
			breakTime = input('Give the break time in second. Eg.: 1.5 (1.5 seconds): ')
			randomColor(breakTime)
		if c == 'c' and not abort:
			abort = True

start_new_thread(checkKey, ())

print('1: static color')
print('2: blinking static color')
print('3: police effect... WARNING FLASHING LIGHTS')
print('4: random colors')

def setColor(red, green, blue):

	if red > 255 and red < 0:
		if red > 255:
			setLights(RED_PIN, 255)
		if red < 0:
			setLights(RED_PIN, 0)
	else:
		setLights(RED_PIN, red)

	if green > 255 and green < 0:
		if green > 255:
			setLights(GREEN_PIN, 255)
		if green < 0:
			setLights(GREEN_PIN, 0)
	else:
		setLights(GREEN_PIN, green)

	if blue > 255 and blue < 0:
		if blue > 255:
			setLights(BLUE_PIN, 255)
		if blue < 0:
			setLights(BLUE_PIN, 0)
	else:
		setLights(BLUE_PIN, blue)

def blink(red, green, blue, breakTime):

	while abort == False:
		setColor(red, green, blue)

		time.sleep(breakTime)

		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,0)

		time.sleep(breakTime)

def policeLight():

	while abort == False:
		setLights(RED_PIN,0)
		setLights(GREEN_PIN,0)
		setLights(BLUE_PIN,255)

		time.sleep(0.20)

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

		time.sleep(0.20)

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

def randomColor(breakTime):
	while abort == False:
		setLights(RED_PIN,randint(0,255))
		setLights(GREEN_PIN,randint(0,255))
		setLights(BLUE_PIN,randint(0,255))
		time.sleep(0.5)

print ('Aborting...')

setLights(RED_PIN,0)
setLights(GREEN_PIN,0)
setLights(BLUE_PIN,0)

time.sleep(0.5)

pi.stop()
