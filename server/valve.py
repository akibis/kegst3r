import RPi.GPIO as GPIO
import time

# Set GPIO pin an output type
def setupValve():
  pin = 22

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)
  print("Valve initialized.")

  return pin

# Perform valve functionality test
# You should hear an audiable click
# when the solenoid triggers
def runTest():
  valve = setupValve()
  count = 0

  print("Starting Test")
  while (count < 5):
    GPIO.output(valve, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(valve, GPIO.LOW)
    count += 1

  print("Test complete.")
  GPIO.cleanup()
  print("Clean exit.")

# Main function to pour beer
def pourBeer(valve):
  valve = setupValve()
  GPIO.output(valve, GPIO.HIGH)
  # Need to test exact time in order to pour beer perfectly
  print("Pouring a cold one...")
  time.sleep(5)
  print("Beer poured. Stay thirsty my friend!")
  GPIO.output(valve, GPIO.LOW)



