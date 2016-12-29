import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 9

ECHO = 25

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

def USS1Distance():	
	time.sleep(2)								#Waiting for the trigger to settle in
	GPIO.output(USSTrig1, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(USSTrig1, GPIO.LOW)

	while GPIO.digitalRead(USSEcho1) == 0:
		pulse_start = time.time()

	while GPIO.digitalRead(USSEcho1) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return distance

while True:
	status = USS1Distance()
	print status

GPIO.cleanup()