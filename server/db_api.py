import sqlite3

# Connect to database
conn = sqlite3.connect('../../keg_dev.sqlite')
c = conn.cursor()

# List Users
def listAllUsers():
  for row in c.execute('select * from users'):
    print row

# User Info
def getUserInfo(id):
  badge = getBadgeNumber(id)
  username = getUsername(id)
  balance = getBalance(id)
  beer_count = getBeerCount(id)

  print("%s's info:" %username)
  print("  id: %s" %id)
  print("  badge #: %s" %badge)
  print("  balance: %s" %balance)
  print("  beer score: %s" %beer_count)

# Get user's badge number
def getBadgeNumber(id):
  badge = 0
  for row in c.execute("select badge_number from users where id='%s'" % id):
    badge = row[0]
  return badge

# Get username
def getUsername(id):
  username = 0
  for row in c.execute("select username from users where id='%s'" % id):
    username = row[0]
  return username

# Get user's beer count
def getBeerCount(id):
  beer_count = 0
  for row in c.execute("select beer_count from users where id='%s'" % id):
    beer_count = row[0]
  return beer_count

# Update user's beer count
def setBeerCount(id, amount):
  new_count = getBeerCount(id) + amount
  c.execute("update users set beer_count='%s' where id='%s'" % (new_count, id))  

# Update user balance
def updateBalance(id, amount):
  cur_balance = getBalance(id)
  new_balance = cur_balance + amount
  c.execute("update users set balance='%s' where id ='%s'" % (new_balance, id))

# Get user balance
def getBalance(id):
  balance = 0
  for row in c.execute("select balance from users where id='%s'" % id):
    balance = row[0]
  return balance

# Get user id by badge number
def getUserId(badge_number):
  id = 0
  for row in c.execute("select id from users where badge_number='%s'" % badge_number):
    id = row[0]
  return id
