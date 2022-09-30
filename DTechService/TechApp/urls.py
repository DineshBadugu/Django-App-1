from django.urls import path
from TechApp import views 
urlpatterns = [
    path('', views.Home,name='home'),
    
]
