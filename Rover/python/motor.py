import webiopi
from time import sleep

GPIO = webiopi.GPIO

Motor1A = 17	#Left Side Motor In1
Motor1B = 18	#Left Side Motor In2
Motor2A = 22	#Right Side Motor In1
Motor2B = 23	#Right Side Motor In2

USSTrig1 = 9	#Ultrasonic sensor front Trigger
USSEcho1 = 25	#Ultrasonic sensor front Echo

def setup():
	GPIO.setFunction(Motor1A, GPIO.OUT)
	GPIO.setFunction(Motor2A, GPIO.OUT)
	GPIO.setFunction(Motor1B, GPIO.OUT)
	GPIO.setFunction(Motor2B, GPIO.OUT)
	
	GPIO.setFunction(USSTrig1, GPIO.OUT)
	GPIO.setFunction(USSEcho1, GPIO.IN)

	GPIO.digitalWrite(USSTrig1, GPIO.LOW)	#Setting Sensor to Low

def loop():
	distance = USS1Distance()
	if(float(distance) < 30.00):
		forward()
		time.sleep(1)
		Left()
		time.sleep(1)

def forward():
	GPIO.digitalWrite(Motor1A, GPIO.HIGH)
	GPIO.digitalWrite(Motor1B, GPIO.LOW)
	GPIO.digitalWrite(Motor2A, GPIO.HIGH)
	GPIO.digitalWrite(Motor2B, GPIO.LOW)

def reverse():
	GPIO.digitalWrite(Motor1A, GPIO.LOW)
	GPIO.digitalWrite(Motor1B, GPIO.HIGH)
	GPIO.digitalWrite(Motor2A, GPIO.LOW)
	GPIO.digitalWrite(Motor2B, GPIO.HIGH)

def stop():
	GPIO.digitalWrite(Motor1A, GPIO.LOW)
	GPIO.digitalWrite(Motor1B, GPIO.LOW)
	GPIO.digitalWrite(Motor2A, GPIO.LOW)
	GPIO.digitalWrite(Motor2B, GPIO.LOW)

def Left():
	GPIO.digitalWrite(Motor1A, GPIO.LOW)
	GPIO.digitalWrite(Motor2A, GPIO.HIGH)
	GPIO.digitalWrite(Motor1B, GPIO.HIGH)
	GPIO.digitalWrite(Motor2B, GPIO.LOW)
		
def Right():
    GPIO.digitalWrite(Motor1A, GPIO.HIGH)
    GPIO.digitalWrite(Motor2A, GPIO.LOW)
    GPIO.digitalWrite(Motor1B, GPIO.LOW)
    GPIO.digitalWrite(Motor2B, GPIO.HIGH)

def USS1Distance():	
	time.sleep(2)								#Waiting for the trigger to settle in
	GPIO.digitalWrite(USSTrig1, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.digitalWrite(USSTrig1, GPIO.LOW)

	while GPIO.digitalRead(USSEcho1) == 0:
		pulse_start = time.time()

	while GPIO.digitalRead(USSEcho1) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return distance

@webiopi.macro
def ButtonForward():
	forward()

@webiopi.macro
def ButtonReverse():
	reverse()

@webiopi.macro
def ButtonTurnLeft():
	Left()

@webiopi.macro
def ButtonTurnRight():
	Right()

@webiopi.macro
def ButtonStop():
	stop()