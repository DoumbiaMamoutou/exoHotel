from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('home', views.index, name="home"),
    path('single', views.single, name="single"),
    # path('<int:id>/single', views.single, name="single"),
    
]