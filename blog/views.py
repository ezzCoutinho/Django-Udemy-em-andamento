from django.shortcuts import render # HTML
from blog.data import posts


# Create your views here.
# HTTP Request ↔ HTTP Response.
# MVT(MVC)
def blog(request):
  contexto = {
              "text": "Estamos no blog.",
              "title_blog": "BLOG - ",
              "posts": posts
              }
  return render(request, "blog/index.html", contexto)
 
def post(request, id):
  contexto = {
              "text": f"Estamos no id: {id}.",
              "title_id": f"ID: {id}- ",
              "posts": posts
              }
  return render(request, "blog/index.html", contexto) 
                
def exemplo(request):
  contexto = {
              "text": "Estamos no exemplo do blog.",
              "title": "Titulo do Exemplo - "
              }
  return render(request, "blog/exemplo.html", contexto)
                