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

GPIO.output(USSTrig1, False)
print 'Waiting for sensors to settle'
time.sleep(2)

def forward():
	pwm1.ChangeDutyCycle(50)
	pwm2.ChangeDutyCycle(50)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(0)

def reverse():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(50)
	pwm4.ChangeDutyCycle(50)



def stop():
	GPIO.output(Motor1A, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor2A, GPIO.LOW)
	GPIO.output(Motor2B, GPIO.LOW)

def Left():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(90)
	pwm3.ChangeDutyCycle(90)
	pwm4.ChangeDutyCycle(0)
		
def Right():
    pwm1.ChangeDutyCycle(90)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(90)
		
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

while True:
	forward()
	status = USS1Distance()
	print status
	if(status < 40):
		reverse()
		time.sleep(0.75)
		Left()
		time.sleep(0.75)
		stop()

GPIO.cleanup()