from django.shortcuts import render # HTML
from blog.data import posts
from typing import Any
from django.http import Http404, HttpRequest

# Create your views here.
# HTTP Request ↔ HTTP Response.
# MVT(MVC)
def blog(request):
  contexto = {
              "text": "Estamos no blog.",
              "title": "BLOG - ",
              "posts": posts
              }
  return render(request, "blog/index.html", contexto)
 
def post(request: HttpRequest, post_id: int):
  found_post: dict[str, Any] | None = None
  for post in posts:
    if post["id"] == post_id:
      found_post = post
      break
  if found_post is None:
  # Se o post não for encontrado, você pode retornar uma página 404
    raise Http404("Post não encontrado")    
  contexto = {
              "text": f"Estamos no id: {post_id}.",
              "title": found_post["title"] + " - ",
              "post": found_post
              }
  return render(request, "blog/post.html", contexto) 
                
def exemplo(request):
  contexto = {
              "text": "Estamos no exemplo do blog.",
              "title": "Titulo do Exemplo - "
              }
  return render(request, "blog/exemplo.html", contexto)
                