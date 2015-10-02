# Smart keg application for Raspberry Pi/2
#
# by: Aleksandr Kibis
# 9/7/15
#
# MIT License

import RPi.GPIO as GPIO	# Raspberry Pi GPIO pin library
import time            	# For time keeping
from db_api import *   	# LOADS KEG API
from poll import getUID	# parses libnfc polling
from valve import *	# valve functions


# Use RPi2 board pin numbering scheme
GPIO.setmode(GPIO.BOARD)

# Setup pins
blue = 32   # INFO
green = 36  # SUCCESS
yellow = 38 # BEER FLOW
red = 40    # ERROR
button = 18 # Start poll button
valve = 22  # Solenoid valve

# Initialize IO
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(valve, GPIO.OUT)

# Reset pins
GPIO.output(blue, GPIO.LOW)
GPIO.output(green, GPIO.LOW)
GPIO.output(yellow, GPIO.LOW)
GPIO.output(red, GPIO.LOW)

# Run dispense loop
while 1:
  try:
    # Wait for button trigger
    input_state = GPIO.input(button)
    if input_state == False:
      GPIO.output(blue, GPIO.HIGH)
      print('Polling initiated')
      card_id = getUID()
      print(card_id)    
 
      # Pull up account
      id = getUserId(card_id)
      print(id)
      account_balance = getBalance(id)
      print(account_balance)
      # time.sleep(0.2)

      # Exit if you're broke
      if account_balance < 1:
        GPIO.output(red, GPIO.HIGH)
        print('Insufficient account balance!')
        time.sleep(0.5)
        GPIO.output(red, GPIO.LOW)
        GPIO.cleanup()
        exit(0)
    
      # Otherwise quench your thirst
      else:
        GPIO.output(green, GPIO.HIGH)
        print('Let the beer flow!')
        GPIO.output(yellow, GPIO.HIGH)
      
        # update user balance
        updateBalance(id, -1)
        account_balance = getBalance(id)
      
        # trigger solenoid and flow meter here
        pourBeer(valve)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(yellow, GPIO.LOW)
      
        # update user beer count
        setBeerCount(id, 1)

        # commit changes so they persist in 
        # future sessions
        conn.commit()

        # show user stats
        getUserInfo(id)

      GPIO.output(blue, GPIO.LOW) 
  
  # Exit cleanly on CTRL+C press
  except KeyboardInterrupt:
    GPIO.cleanup()
    print('\n\n')
    print("Exiting. Happy stumble home!")
    print('\n')
    exit(0)
