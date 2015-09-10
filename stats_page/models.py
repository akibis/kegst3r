from django.db import models

# Contains all user information and stats
class User(models.Model):
  id = models.IntegerField(primary_key=True)
  badge_number = models.IntegerField(default=0)
  username = models.CharField(max_length=20)
  balance = models.IntegerField(default=0)
  beer_count = models.IntegerField(default=0)
 
  # Print out User object contents 
  def __str__(self):
    content = 'ID: '+str(self.id)+'\n'\
      'Badge Number: '+str(self.badge_number)+'\n'\
      'Username: '+self.username+'\n'\
      'Balance: $'+str(self.balance)+'\n'\
      'Beer Count: '+str(self.beer_count)+'\n'
    return content

  # Start getters
  def getBadgeNumber(self):
    return str(self.badge_number)

  def getUsername(self):
    return str(self.username)

  def getBalance(self):
    return str(self.balance)

  def getBeerCount(self):
    return str(self.beer_count)

# Contains beer statistics by type
class BeerData(models.Model):
  id = models.IntegerField(primary_key=True)
  brewery_name = models.CharField(max_length=40)
  beer_type = models.CharField(max_length=40)
  number_dispensed = models.IntegerField(default=0)
  popularity = models.IntegerField(default=0)

  # Print out BeerData object contents
  def __str__(self):
    content = 'ID: '+str(self.id)+'\n'\
      'Brewery Name: '+self.brewery_name+'\n'\
      'Beer Type: '+self.beer_type+'\n'\
      'Number of Beers Dispensed: '+str(self.number_dispensed)+'\n'\
      'Popularity: '+str(self.popularity)+'\n'
    return content

  # Start getters
  def getBreweryName(self):
    return self.brewery_name

  def getBeerType(self):
    return self.beer_type

  def getNumberDispensed(self):
    return self.number_dispensed

  def getPopularity(self):
    return self.popularity 
