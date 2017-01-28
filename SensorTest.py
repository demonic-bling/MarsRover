import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1A = 17	#Left Side Motor In1
Motor1B = 18	#Left Side Motor In2
Motor2A = 22	#Right Side Motor In1
Motor2B = 23	#Right Side Motor In2

FrontUSSTrig = 9	#Front Sensor Trigger
FrontUSSEcho = 25	#Front Sensor Echo

BackUSSTrig = 11	#Back Sensor Trigger
BackUSSEcho = 8		#Back Sensor Echo

LeftUSSTrig = 30	#Left Sensor Trigger
LeftUSSEcho = 30	#Left Sensor Echo

RightUSSTrig = 30	#Right Sensor Trigger
RightUSSEcho = 30	#Right Sensor Echo

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
	
GPIO.setup(FrontUSSTrig, GPIO.OUT)
GPIO.setup(FrontUSSEcho, GPIO.IN)
GPIO.setup(BackUSSTrig, GPIO.OUT)
GPIO.setup(BackUSSEcho, GPIO.IN)

GPIO.output(FrontUSSTrig, False)
GPIO.output(BackUSSTrig, False)
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
		
def FrontUSSDistance():	
	time.sleep(1)
	GPIO.output(FrontUSSTrig, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(FrontUSSTrig, GPIO.LOW)

	while GPIO.input(FrontUSSEcho) == 0:
		pulse_start = time.time()

	while GPIO.input(FrontUSSEcho) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return distance

def LeftUSSDistance():	
	time.sleep(1)
	GPIO.output(LeftUSSTrig, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(LeftUSSTrig, GPIO.LOW)

	while GPIO.input(LeftUSSEcho) == 0:
		pulse_start = time.time()

	while GPIO.input(LeftUSSEcho) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return distance

def RightUSSDistance():	
	time.sleep(1)
	GPIO.output(RightUSSTrig, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(RightUSSTrig, GPIO.LOW)

	while GPIO.input(RightUSSEcho) == 0:
		pulse_start = time.time()

	while GPIO.input(RightUSSEcho) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return distance

def BackUSSDistance():	
	time.sleep(1)
	GPIO.output(BackUSSTrig, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(BackUSSTrig, GPIO.LOW)

	while GPIO.input(BackUSSEcho) == 0:
		pulse_start = time.time()

	while GPIO.input(BackUSSEcho) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return distance

try:
	while True:
		forward()
		fwdDist = FrontUSSDistance()
		bwdDist = BackUSSDistance()
		leftDist = LeftUSSDistance()
		rightDist = RightUSSDistance()

		print "Front", fwdDist
		print "Back", bwdDist
		print "Left", leftDist
		print "Right", rightDist

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