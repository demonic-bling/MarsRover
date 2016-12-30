import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1A = 17	#Left Side Motor In1
Motor1B = 18	#Left Side Motor In2
Motor2A = 22	#Right Side Motor In1
Motor2B = 23	#Right Side Motor In2

USSTrig1 = 9
USSEcho1 = 25

print "Distance Measurement In Progress"

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
	
GPIO.setup(USSTrig1, GPIO.OUT)
GPIO.setup(USSEcho1, GPIO.IN)

GPIO.output(USSTrig1, False)
sleep(2)

def forward():
	GPIO.output(Motor1A, GPIO.HIGH)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor2A, GPIO.HIGH)
	GPIO.output(Motor2B, GPIO.LOW)

def reverse():
	GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.HIGH)
	GPIO.output(Motor2A, GPIO.LOW)
	GPIO.output(Motor2B, GPIO.HIGH)

def stop():
	GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor2A, GPIO.LOW)
	GPIO.output(Motor2B, GPIO.LOW)

def Left():
	GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor2A, GPIO.HIGH)
	GPIO.output(Motor1B, GPIO.HIGH)
	GPIO.output(Motor2B, GPIO.LOW)
		
def Right():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def USS1Distance():	
	GPIO.output(USSTrig1, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(USSTrig1, GPIO.LOW)

	while GPIO.input(USSEcho1) == 0:
		pulse_start = time.time()

	while GPIO.input(USSEcho1) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return distance

while True:
	forward()
	status = USS1Distance()
	print status
	if(status < 30):
		reverse()
		sleep(0.75)
		Left()
		sleep(0.75)
		stop()

GPIO.cleanup()