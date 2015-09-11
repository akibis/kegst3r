import RPi.GPIO as GPIO             ## Import GPIO Library
import time                         ## Import 'time' library (for 'sleep')

blue = 31                            ## These are our LEDs
ourdelay = 1                        ## Delay
# pins 4,17,18,21,22,23,24,25

GPIO.setmode(GPIO.BOARD)            ## Use BOARD pin numbering
GPIO.setup(blue, GPIO.OUT)        ## set output

## function to save code

def activateLED( pin, delay ):
  GPIO.output(pin, GPIO.HIGH)      ## set HIGH (LED ON)
  time.sleep(delay)                ## wait
  GPIO.output(pin, GPIO.LOW)       ## set LOW (LED OFF)
  return;

#while (1):
activateLED(blue,ourdelay)

GPIO.cleanup()
