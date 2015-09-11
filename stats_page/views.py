from django.shortcuts import render

from .models import User

# Create your views here.

def index(request):
  return HttpResponse("Welcome to Kegst3r!")

def users(request):
  user_list = User.objects.order_by('id')
  context = {'user_list': user_list}
  return render(request, 'stats_page/index.html', context)
  
