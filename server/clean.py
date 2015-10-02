import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

blue = 29
green = 31
yellow = 32
red = 33
button = 36

GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

GPIO.cleanup()
