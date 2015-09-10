from django.contrib import admin

from .models import User, BeerData

# Register your models here.i

class UserAdmin(admin.ModelAdmin):
  fields = ['id', 'username', 'badge_number', 'balance', 'beer_count']
  list_display = ('username', 'badge_number', 'balance')
  search_fields = ['username', 'badge_number']

class BeerDataAdmin(admin.ModelAdmin):
  fields = ['id', 'brewery_name', 'beer_type', 'number_dispensed', 'popularity']
  list_display = ('brewery_name', 'beer_type', 'popularity')
  search_fields = ['brewery_name', 'beer_type', 'popularity']  

admin.site.register(User, UserAdmin)
admin.site.register(BeerData, BeerDataAdmin)
