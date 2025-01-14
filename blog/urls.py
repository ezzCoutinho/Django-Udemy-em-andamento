from django.urls import path
from blog import views as blog_views 

app_name = "blog" # É um name_space de urls

#blog/
urlpatterns = [   
    path("", blog_views.blog, name="blog"), # São url's.
    path("<int:post_id>/", blog_views.post, name="post"), 
    path("exemplo/", blog_views.exemplo, name="exemplo"), # São url's.
]
