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

USSTrig2 = 11
USSEcho2 = 8

print "Distance Measurement In Progress"

GPIO.cleanup()

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)


pwm1 = GPIO.PWM(Motor1A, 1000)
pwm2 = GPIO.PWM(Motor2A, 1000)
pwm3 = GPIO.PWM(Motor1B, 1000)
pwm4 = GPIO.PWM(Motor2B, 1000)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
	
GPIO.setup(USSTrig1, GPIO.OUT)
GPIO.setup(USSEcho1, GPIO.IN)
GPIO.setup(USSTrig2, GPIO.OUT)
GPIO.setup(USSEcho2, GPIO.IN)

GPIO.output(USSTrig1, False)
GPIO.output(USSTrig2, False)
print 'Waiting for sensors to settle'
time.sleep(2)

def forward():
	pwm1.ChangeDutyCycle(40)
	pwm2.ChangeDutyCycle(40)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(0)

def reverse():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(40)
	pwm4.ChangeDutyCycle(40)

def stop():
	GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor2A, GPIO.LOW)
	GPIO.output(Motor2B, GPIO.LOW)

def Left():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(99)
	pwm3.ChangeDutyCycle(99)
	pwm4.ChangeDutyCycle(0)
		
def Right():
	pwm1.ChangeDutyCycle(99)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(99)
		
def USS1Distance():	
	time.sleep(1)
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

def USS2Distance():	
	time.sleep(1)
	GPIO.output(USSTrig2, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(USSTrig2, GPIO.LOW)

	while GPIO.input(USSEcho2) == 0:
		pulse_start = time.time()

	while GPIO.input(USSEcho2) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return distance

try:
	while True:
		forward()
		fwdDist = USS1Distance()
		bwdDist = USS2Distance()
		print "Front", fwdDist
		print "Back", bwdDist
		if(fwdDist < 70):
			if(bwdDist > 50):
				reverse()
				time.sleep(0.75)
				Left()
				time.sleep(0.75)
				stop()
			else:
				Left()
				time.sleep(1)
				stop()
				
except KeyboardInterrupt:
	pass

pwm1.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()
GPIO.cleanup()