from django.urls import path
from home import views as home_views
from home import views as base_views

# /
urlpatterns = [   
    path("", home_views.home, name= "home"),
    path("global/", base_views.base, name= "global")

]
