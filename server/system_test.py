import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

blue = 32
green = 36
red = 38
yellow = 40
valve = 22

GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(valve, GPIO.OUT)

def runTest(pinNum, count):
  while(count > 0):
    GPIO.output(pinNum, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pinNum, GPIO.LOW)
    time.sleep(1)
    count -= 1

runTest(blue, 1)
runTest(green, 1)
runTest(red, 1)
runTest(yellow, 1)
runTest(valve, 3)

GPIO.cleanup()
