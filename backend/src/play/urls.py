from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('host/<str:game_id>/', views.host, name='host'),
    path('join/<str:game_token>/', views.join, name='join'),
]