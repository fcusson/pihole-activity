#! /usr/bin/env python

#######################################################################
## This Script is built for Raspberry Pi Zero W using wiringPi here: ##
## https://github.com/hardkernel/wiringPi                            ##
## Built for interaction with the pi-hole FTL api                    ##
## This is a test code. For the production version, see /src/ folder ##
#######################################################################

#######################################################################
## Version: 	1.1.2                                                ##
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
		# request pi-hole api summaryRaw in json format
		pihole = requests.get("http://127.0.0.1/admin/api.php?summaryRaw").json()
		# get number of ads blocked since last check
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

			# print that an ad was blocked
			print("ad Blocked")

		# wait before new refresh
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

