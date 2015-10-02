import RPi.GPIO as GPIO
import time

# Setup pin and mode
GPIO.setmode(GPIO.BOARD)
flow_meter = 16
GPIO.setup(flow_meter, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# flow rate monitor setup
pouring = False
lastPinState = False
pinState = 0
lastPinChange = int(time.time() * 1000)
pourStart = 0
pinChange = lastPinChange
pinDelta = 0
hertz = 0
flow = 0
litersPoured = 0
pintsPoured = 0

a = 0

while (a < 100000):
  currentTime = int(time.time() * 1000)
  #print("Time: %s" % str(currentTime))
  if GPIO.input(flow_meter):
    pinState = True
  else:
    pinState = False

  # If we have changed pin states low to high...
  
  if(pinState != lastPinState and pinState == True):
    if(pouring == False):
      pourStart = currentTime
    pouring = True
    # get the current time
    pinChange = currentTime
    pinDelta = pinChange - lastPinChange
   #print("Pin Delta: %s" % str(pinDelta))
   #print("Pin Change: %s" % str(pinChange))
   #print("Last Pin Change: %s" % str(lastPinChange))
    

    if (pinDelta < 1000):
      # calculate the instantaneous speed
      hertz = 1000.0000 / pinDelta
      flow = hertz / (60 * 7.5) # L/s
      litersPoured += flow * (pinDelta / 1000.0000)
      pintsPoured = litersPoured * 2.11338

  if (pouring == True and pinState == lastPinState and (currentTime - lastPinChange) > 3000):
    # set pouring back to false, tweet the current amt poured, and reset everything
    pouring = False
    if (pintsPoured > 0.1):
      pourTime = int((currentTime - pourStart)/1000) - 3
      litersPoured = 0
      pintsPoured = 0

  lastPinChange = pinChange
  lastPinState = pinState
  
  a += 1

# END WHILE LOOP
#print("Herts: $s" % str(hertz))
print("Liters Poured: %s" % str(litersPoured))
print("Pints Poured: %s" % str(pintsPoured))


GPIO.cleanup()

