from django.urls import path
from . import views

app_name='hotel'

urlpatterns = [
    path('home', views.index, name="home"),
    path('room', views.room, name="room"),
    path('single', views.single, name="single"),
    path('about', views.about, name="about"),
    # path('<int:id>/single', views.single, name="single"),
    
]