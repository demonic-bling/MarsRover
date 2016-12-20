import webiopi
from time import sleep

GPIO = webiopi.GPIO

Motor1A = 17
Motor1B = 18
Motor2A = 22
Motor2B = 23

def setup():
	GPIO.setFunction(Motor1A, GPIO.OUT)
	GPIO.setFunction(Motor2A, GPIO.OUT)
	GPIO.setFunction(Motor1B, GPIO.OUT)
	GPIO.setFunction(Motor2B, GPIO.OUT)

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

@webiopi.macro
def GetSpeed(speed):
	GPIO.PulseRatio(Motor3A, float(speed))

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

