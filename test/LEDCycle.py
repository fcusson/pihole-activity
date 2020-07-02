#! /usr/bin/env python

#######################################################################
## This Script is built for Raspberry Pi Zero W using wiringPi here: ##
## https://github.com/hardkernel/wiringPi                            ##
## This is a test code to validate the correct wirering in           ##
## accordance to the project pihole-activity:                        ##
## https://github.com/Darkfull-Dante/pihole-activity                 ##
#######################################################################

#######################################################################
## Version: 	1.2.2                                                ##
## Author:      Felix Cusson                                         ##
## Date:        2020-07-02                                           ##
## License:     GPL-3.0                                              ##
#######################################################################

# Import Module
import requests
import time
import RPi.GPIO as GPIO
import math
from configparser import ConfigParser

# establish ConfigParser as a variable
configur = ConfigParser()
configur.read('config.ini')

# config variables
reverseLEDBarGraph = configur.getboolean('LEDBarGraph', 'reverseLEDBarGraph')

# define variables
waitTime = 0.1
onTime = 0.4
ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]
enPin = 35
adPin = 37

# reverse ledPins if required by config.ini
if reverseLEDBarGraph == True :
	ledPins = ledPins.reverse()

# define setup
def setup():
	
	# setup for the LED Bar Graph
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPins, GPIO.OUT)
	GPIO.output(ledPins, GPIO.LOW)

	# setup for the status LED
	GPIO.setup(enPin, GPIO.OUT)
	GPIO.output(enPin, GPIO.LOW)

	# setup for the ad blocked LED
	GPIO.setup(adPin, GPIO.OUT)
	GPIO.output(adPin, GPIO.LOW)

# define the LED Cycle code
def cycle():

	i = 0

	# cycle through every LED in the bar graph
	for pin in ledPins :

		# do somethin only if Index is not 0
		i += 1

		# Open and then close every LED in the bar graph in order
		GPIO.output(pin, GPIO.HIGH)
		print("Bar Graph LED " + str(i) + " on")
		time.sleep(onTime)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(waitTime)

	# open and then close status LED
	GPIO.output(enPin, GPIO.HIGH)
	print("Status LED on")
	time.sleep(onTime)
	GPIO.output(enPin, GPIO.LOW)
	time.sleep(waitTime)

	# open and then close the ad LED
	GPIO.output(adPin, GPIO.HIGH)
	print("ad Blocked LED on")
	time.sleep(onTime)
	GPIO.output(adPin, GPIO.LOW)
	time.sleep(waitTime)

# define GPIO CleanUp
def destroy():
	GPIO.cleanup()

if __name__ == '__main__':

	#Call Setup
	setup()
	try:
		#Call Loop
		cycle()

	except KeyboardInterrupt:
		destroy()
