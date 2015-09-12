from django.shortcuts import render
#from django.http import HttpResponse

from .models import User, BeerData

# Create your views here.

#def index(request):
#  return HttpResponse("Welcome to Kegst3r!")

def users(request):
  user_list = User.objects.order_by('id')
  context = {'user_list': user_list}
  return render(request, 'stats_page/index.html', context)

def gauges(request):
  beer_data = BeerData.objects.order_by('id')
  context = {'beer_data': beer_data}
  return render(request, 'stats_page/gauges.html', context)  
