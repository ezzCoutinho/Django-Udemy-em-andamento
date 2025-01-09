from django.urls import path
from blog import views as blog_views 

#blog/
urlpatterns = [   
    path("", blog_views.my_view), # São url's.
    path("exemplo/", blog_views.exemplo), # São url's.
]
