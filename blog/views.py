from django.shortcuts import render # HTML
from blog.data import posts


# Create your views here.
# HTTP Request ↔ HTTP Response.
# MVT(MVC)
def my_view(request):
  contexto = {
              "text": "Estamos no blog.",
              "title_blog": "BLOG - ",
              "posts": posts
              }
  return render(request, "blog/index.html", contexto) 
                
def exemplo(request):
  contexto = {
              "text": "Estamos no exemplo do blog.",
              "title": "Titulo do Exemplo - "
              }
  return render(request, "blog/exemplo.html", contexto)
                