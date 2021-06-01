from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('darslar/', views.darslar, name= 'darslar'),
    path('register', views.register, name='register'),
    path('login/', views.Login, name = 'login'),
    path('video/<int:pk>/', views.VideoDarsDetail.as_view(), name = 'video'),
    path('playlist-vid/<int:pk>/', views.PlaylistDateilView.as_view(), name = 'playlist-dateil'),
   
]