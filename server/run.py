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
import RPi.GPIO as pigpio
import time
#import threading
#import queue
#import traceback
#from random import randint

#pi=pigpio.pi()

# CLIIO class -> handles all command line input/output
class CLIIO:

	# run!
	@classmethod
	def run(cls):

		cls.print_to_shell(BLINK.commands('help'[0])()[0])

		for cmd in cls.get_ch('>> '):
			cmd = cmd.split(' ', 1)
			cls.print_to_shell(BLINK.commands(cmd[0][0])(*cmd)[0])

	@staticmethod
	def get_ch(placeholder):
		while True:
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)

			try:
				tty.setraw(fd)
				ch = sys.stdin.read(1)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

			yield ch

	@staticmethod
	def get_cmd(placeholder):
		while True:
			yield input(placeholder)

	@staticmethod
	def get_input(placeholder):
		return input(placeholder)

	@staticmethod
	def print_to_shell(output_str):
		print(output_str)


# BOX object
class BLINK:

	# meths
	@classmethod
	def commands(cls, cmd):
		return{
			'a': lambda: cls.check_key,
			'h': lambda: cls.help,
			'e': lambda: os.sys.exit()
		}.get(cmd, lambda: cls.help)()
	'''
	def setLights(pin, brightness):
		pi.set_PWM_dutycycle(pin, brightness)

	@classmethod
	def check_key(cls, *args):
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

	@classmethod
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

	@classmethod
	def blink(red, green, blue, breakTime):

		while abort == False:
			setColor(red, green, blue)

			time.sleep(breakTime)

			setLights(RED_PIN,0)
			setLights(GREEN_PIN,0)
			setLights(BLUE_PIN,0)

			time.sleep(breakTime)

	@classmethod
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

	@classmethod
	def randomColor(breakTime):
		while abort == False:
			setLights(RED_PIN,randint(0,255))
			setLights(GREEN_PIN,randint(0,255))
			setLights(BLUE_PIN,randint(0,255))
			time.sleep(0.5)
	'''
	@classmethod
	def help(cls, *args):

		help_text=  'useable commands and arguments are: \n'\
					'\t1: static color \n'\
					'\t2: blinking static color \n'\
					'\t3: police effect... WARNING FLASHING LIGHTS\n'\
					'\t4: random colors\n'

		return (help_text, 1)


try:
	if __name__ == '__main__':
		os.sys.exit(CLIIO.run())

except Exception as e:
	CLIIO.print_to_shell('Oh no! Something has gone wrong. {e}\n{traceback.format_exc()}')

finally:
	CLIIO.print_to_shell('Aborting...')
	'''
	setLights(RED_PIN,0)
	setLights(GREEN_PIN,0)
	setLights(BLUE_PIN,0)

	time.sleep(0.5)

	pi.stop()
	'''
