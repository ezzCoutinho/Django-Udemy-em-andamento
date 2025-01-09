from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): # É uma viewer, a viewer faz a ponte entre o usuário e o servidor
  print("HOME")
  return HttpResponse("home do app")

