from django.shortcuts import render # HTML


# Create your views here.
# HTTP Request ↔ HTTP Response.
# MVT(MVC)
def my_view(request):
  return render(request, "blog/home.html")

def exemplo(request):
  return render(request, "blog/exemplo.html")