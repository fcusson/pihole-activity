#! /usr/bin/env python

#######################################################################
## This Script is built for Raspberry Pi Zero W using wiringPi here: ##
## https://github.com/hardkernel/wiringPi                            ##
## Built for interaction with the pi-hole FTL api                    ##
## This is a test code, for production version see /src/ folder      ##
#######################################################################

#######################################################################
## Version: 	1.2.4                                                ##
## Author:      Felix Cusson                                         ##
## Date:        2020-07-02                                           ##
# ## License:   GPL-3.0                                              ##
#######################################################################

# Import Module
import requests
import time
import RPi.GPIO as GPIO
import math
from configparser import ConfigParser

# establish ConfigParser as a variable
configur = ConfigParser()
configur.read('/home/pi/pihole-activity/test/config.ini')

# config variables
reverseLEDBarGraph = configur.getboolean('LEDBarGraph', 'reverseLEDBarGraph')
onStateBG = configur.getboolean('LEDBarGraph', 'highModeBarGraph')
onStateSL = configur.getboolean('StatusLED', 'highModeStatus')

# define variables
waitTime = 5
ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]
enPin = 35

# determine the on and off value for Bar Graph
if onStateBG == True :
	onValueBG = GPIO.HIGH
	offValueBG = GPIO.LOW

elif onStateBG == False :
	onValueBG = GPIO.LOW
	offValueBG = GPIO.HIGH

# determine the on and off state for the Status LED
if onStateSL == True :
	onValueSL = GPIO.HIGH
	offValueSL = GPIO.LOW
elif onStateSL == False :
	onValueSL = GPIO.LOW
	offValueSL = GPIO.HIGH

# define the reversing function
def Reverse(lst):
	lst.reverse()
	return lst

# define setup
def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPins, GPIO.OUT)
	GPIO.output(ledPins, offValueBG)

	GPIO.setup(enPin, GPIO.OUT)
	GPIO.output(enPin, offValueSL)

	# reverse LEDPins if reverseLEDBarGraph is true
	if reverseLEDBarGraph == True :
		Reverse(ledPins)

# define Infinite Loop
def loop():

	percentOld=0
	statusOld="disabled"

	while True:
		# Get percent Blocked
		pihole = requests.get("http://127.0.0.1/admin/api.php?summaryRaw").json()
		percentNew = int(round(pihole['ads_percentage_today']))
		statusNew = str(pihole['status'])
		print(statusNew)


		print(percentNew)
		numberOfLed = int(round(percentNew/10))

		# Check if percentNew is different from percentOld
		if percentNew != percentOld :

			# refresh percentOld
			percentOld = percentNew
			i = 0
			
			# loop through pins
			for pin in ledPins :

				# do something only if Index is not 0
				i += 1

				# Open Led only if pin index is lower or equal to percentNew
				if i <= numberOfLed :
					GPIO.output(pin, onValueBG)
					print("pin " + str(i) + " on, pin no : " + str(pin))
				
				elif i > (numberOfLed + 1) :
					GPIO.output(pin, offValueBG)
					print("pin " + str(i) + " off, pin no : " + str(pin))

		if statusNew != statusOld :

			#refresh statusOld
			statusOld = statusNew

			#change led status depending on status of Pi-Hole
			if statusNew == "enabled" :
				GPIO.output(enPin, onValueSL)
				print("Pi-Hole is enabled")
			else :
				GPIO.output(enPin, offValueSL)
				print("Pi-Hole is disabled")

		# Wait before refresh
		time.sleep(waitTime)

# define GPIO CleanUp
def destroy():
	GPIO.cleanup()

if __name__ == '__main__':

	#Call Setup
	setup()
	try:
		#Call Loop
		loop()

	except KeyboardInterrupt:
		destroy()
