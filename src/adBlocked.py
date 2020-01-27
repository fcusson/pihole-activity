#! /usr/bin/env python

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

