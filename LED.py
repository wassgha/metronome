import RPi.GPIO as GPIO
import time

blue = 4
green = 17
red = 21

def turnOn(colorNum):
    GPIO.setwarnings(False)
    GPIO.setup(colorNum, GPIO.OUT)
    GPIO.output(colorNum, False)

def turnOff(colorNum):
    GPIO.setwarnings(False)
    GPIO.output(colorNum, True)

def turnOnWithCertainNum(numPassengers):
    GPIO.setmode(GPIO.BCM)
    turnOn(green)
    if numPassengers > 50:
        turnOff(green)
        turnOn(red)
    elif numPassengers > 20:
        turnOn(red)

    
    

