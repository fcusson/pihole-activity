#! /usr/bin/env python

#######################################################################
## This Script is built for Raspberry Pi Zero W using wiringPi here: ##
## https://github.com/hardkernel/wiringPi                            ##
## Built for interaction with the pi-hole FTL api                    ##
## This is a test code, for production version see /src/ folder      ##
#######################################################################

#######################################################################
## Version: 	1.0.2                                                ##
## Author:      Felix Cusson                                         ##
## Date:        2020-01-28                                           ##
# ## License:   GPL-3.0                                              ##
#######################################################################

# Import Module
import requests
import time
import RPi.GPIO as GPIO
import math

# define variables
waitTime = 5
ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]
enPin = 35

# define setup
def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPins, GPIO.OUT)
	GPIO.output(ledPins, GPIO.LOW)

	GPIO.setup(enPin, GPIO.OUT)
	GPIO.output(enPin, GPIO.LOW)

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
					GPIO.output(pin, GPIO.HIGH)
					print("pin " + str(i) + " on, pin no : " + str(pin))
				
				if i > (numberOfLed + 1) :
					GPIO.output(pin, GPIO.LOW)
					print("pin " + str(i) + " off, pin no : " + str(pin))

		if statusNew != statusOld :

			#refresh statusOld
			statusOld = statusNew

			#change led status depnding on status of Pi-Hole
			if statusNew == "enabled" :
				GPIO.output(enPin, GPIO.HIGH)
				print("Pi-Hole is enabled")
			else :
				GPIO.output(enPin, GPIO.LOW)
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
