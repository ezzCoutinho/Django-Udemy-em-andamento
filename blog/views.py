from django.shortcuts import render # HTML
from django.http import HttpResponse

# Create your views here.
# HTTP Request ↔ HTTP Response.
# MVT(MVC)
def my_view(request):
  print("my_view")
  return HttpResponse("blog do app")