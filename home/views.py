from django.shortcuts import render


# Create your views here.
def home(request): # É uma viewer, a viewer faz a ponte entre o usuário e o servidor
  print("HOME")
  return render(request, "home/home.html")

