from django.shortcuts import render


# Create your views here.
def home(request): # É uma viewer, a viewer faz a ponte entre o usuário e o servidor
  return render(request, "home/index.html")

def base(request):
  return render(request, "global/base.html")