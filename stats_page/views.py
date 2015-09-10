from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Hello world.")

def users(request, user_id):
  return HttpResponse("User is: %s" % user_id)
