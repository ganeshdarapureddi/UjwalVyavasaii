from django.urls import path
from . import views

urlpatterns = [
    path('', views.funroute3),
    path('buy/', views.buy),
]