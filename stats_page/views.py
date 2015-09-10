from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import User

# Create your views here.

def index(request):
  return HttpResponse("Welcome to Kegst3r!")

def users(request):
  user_list = User.objects.order_by('id')
  template = loader.get_template('stats_page/index.html')
  context = RequestContext(request, {
    'user_list': user_list,
  })
  return HttpResponse(template.render(context))
  
