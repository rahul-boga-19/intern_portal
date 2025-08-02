from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard/', views.dashboard),
    path('leaderboard/', views.leaderboard),
    path('api/intern/', views.api_intern),
]
