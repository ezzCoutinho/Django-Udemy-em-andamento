from django.shortcuts import render

# Create your views here.
def home(request): # É uma viewer, a viewer faz a ponte entre o usuário e o servidor
  contexto = {
            "text": "Estamos na home.",
            "title": "HOME - "
            }
  return render(request,
                "home/index.html",
                contexto
                )

def base(request):
  contexto = {
            "text": "Estamos na home.",
            "title": "BASE - "
            }
  return render(request,
                "global/base.html",
                contexto
                )