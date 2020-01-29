#! /usr/bin/env python

#######################################################################
## This Script is built for Raspberry Pi Zero W using wiringPi here: ##
## https://github.com/hardkernel/wiringPi                            ##
## Built for interaction with the pi-hole FTL api                    ##
## This code is built to flash an LED when ads_blocked_today is      ##
## different from last value.                                        ##
#######################################################################

#######################################################################
## Version: 	1.1.1                                                ##
## Author:      Felix Cusson                                         ##
## Date:        2020-01-28                                           ##
## License:     GPL-3.0                                              ##
#######################################################################

# Import Module
import requests
import time
import RPi.GPIO as GPIO
import math

# define variables
waitTime = 2
adPin = 37

# define setup
def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(adPin, GPIO.OUT)
	GPIO.output(adPin, GPIO.LOW)

# define Infinite Loop
def loop():

	blockedOld = 0

	while True:
		# Get blockedQuerry
		pihole = requests.get("http://127.0.0.1/admin/api.php?summaryRaw").json()
		blockedNew = int(pihole['ads_blocked_today'])

		# Check if percentNew is different from percentOld
		if blockedNew != blockedOld :

			# refresh percentOld
			blockedOld = blockedNew

			# Blink adPin
			GPIO.output(adPin, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(adPin, GPIO.LOW)
			time.sleep(0.1)

		# wait before next refresh
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

